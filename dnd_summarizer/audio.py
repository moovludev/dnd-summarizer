"""
This file handles the audio files used in transcription.
If a file is too large, it needs to be split to be transcribed.
Since an input file might be massive, all outputs are cached to reduce memory impact.
"""
import pathlib
import os.path
import logging
import ffmpeg
import dnd_summarizer.transcription as transcribe

TRANSCRIPTION_MAX_SIZE = 26214400
TRANSCRIPTION_MAX_DURATION = 1200
CACHE_DIRECTORY = "./cache/"

logger = logging.getLogger("dnd_summarizer-audio")

def transcribe_file(client:transcribe.OpenAiClient, file_path) -> pathlib.Path:
    """
    This function splits an audio input if required and transcribes each individual part.
    Returns a file path for the output file, since it may be large.
    """
    # Set a flag
    audio_file_has_been_split = False
    # Get path and transcribe
    audio_file = pathlib.Path(file_path)
    audio_file_name = audio_file.stem
    audio_file_extension = audio_file.suffix
    # Make cache folder
    cache_dir = pathlib.Path(CACHE_DIRECTORY)
    cache_dir.mkdir(parents=True, exist_ok=True)
    
    # TODO: Reduce bitrate of audio file

    # Check if input bytes > 26214400
    file_size = os.path.getsize(file_path)
    logger.info("Processing %s at size %d...", file_path, file_size)

    if file_size > TRANSCRIPTION_MAX_SIZE:
        audio_file_has_been_split = True
        # Split files based on 20min intervals (should be small enough for most bitrates)
        ffmpeg.input(file_path).output(
            CACHE_DIRECTORY+audio_file_name+"%03d"+audio_file_extension,
            f="segment",
            segment_time=TRANSCRIPTION_MAX_DURATION,
            reset_timestamps=1
        ).run()

    # Iterate through recording parts and transcribe
    # TODO: Async transcriptions
    if audio_file_has_been_split:
        for audio_file in sorted(cache_dir.iterdir()):
            raw_transcription = client.transcribe_text(audio_file)
            # Write transcription into cache file
            with open(
                CACHE_DIRECTORY + audio_file_name + audio_file_extension + ".txt",
                "a",
                encoding="UTF-8"
                ) as cached_transcription:
                cached_transcription.write(repr(raw_transcription)+"\n")
            # TODO: Add progress bar
    else:
        raw_transcription = client.transcribe_text(audio_file)
        # Write transcription into cache file
        with open(
            CACHE_DIRECTORY + audio_file_name + audio_file_extension + ".txt",
            "a",
            encoding="UTF-8"
            ) as cached_transcription:
            cached_transcription.write(repr(raw_transcription)+"\n")
        # TODO: Progress bar

    return pathlib.Path(CACHE_DIRECTORY + audio_file_name + audio_file_extension + ".txt")

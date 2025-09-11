import pathlib
import os.path
import logging
import ffmpeg
import dnd_summarizer.transcription as transcribe

TRANSCRIPTION_MAX_SIZE = 26214400
TRANSCRIPTION_MAX_DURATION = 1200
CACHE_DIRECTORY = "./.cache/"

logger = logging.getLogger("dnd_summarizer-audio")

def transcribe_file(client:transcribe.OpenAiClient, file_path):
    # Get path and transcribe
    path = pathlib.Path(file_path)
    file_name = path.stem
    file_extension = path.suffix

    # Check if input bytes > 26214400
    file_size = os.path.getsize(file_path)
    logger.info("Processing %s at size %d...", file_path, file_size)
    
    if file_size > TRANSCRIPTION_MAX_SIZE:
        # Make cache folder
        pathlib.Path(CACHE_DIRECTORY).mkdir(parents=True, exist_ok=True)
        # Split files based on 20min intervals (should be small enough for most bitrates)
        ffmpeg.input(file_path).output(
            CACHE_DIRECTORY+file_name+"%03d"+file_extension,
            f="segment",
            segment_time=TRANSCRIPTION_MAX_DURATION,
            reset_timestamps=1
        ).run()

    raw_transcriptions = []
    client.transcribe_text(path) # Add for loop here to iterate through parts
    with open(f"{CACHE_DIRECTORY + file_name + file_extension}.txt", "w", encoding="UTF-8") as file:
        file.write(repr(raw_transcription))

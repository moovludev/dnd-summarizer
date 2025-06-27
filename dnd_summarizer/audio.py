import pathlib
import dnd_summarizer.transcription as transcribe

def transcribe_file(client:transcribe.OpenAiClient, file_path):
    # Get path and transcribe
    path = pathlib.Path(file_path)
    raw_transcription = client.transcribe_text(path)

    # TODO: Check bytes if > 26214400
    # TODO: Split files

    # Make cache folder and file
    pathlib.Path("./cache").mkdir(parents=True, exist_ok=True)
    file_name = path.name
    with open(f"./cache/{file_name}.txt", "w", encoding="UTF-8") as file:
        file.write(repr(raw_transcription))

def split_audio(file_dir):
    raise NotImplementedError
    # Figure out how many splits
    # Make splits
    # Return

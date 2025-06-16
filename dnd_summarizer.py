import argparse
import logging
import audio_transcription
import summarization

# Setup logger
logger = logging.getLogger("dnd_summarizer")


def parse_args(
    input_file: list[str],
    api_key: str,
    processing_method: str = "chained",
    output_format: list[str] | str = "none",
    output: str = None,
    verbose: bool = False,
    dry_run: bool = False,
    allow_dots: bool = False
):
    # Check if verbose is set
    if verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    # Log arguments
    logger.debug(
        "input: %s, api_key: %s, processing_method: %s, output_format: %s, output: %s, verbose: %s, dry_run: %s, allow_dots %s",
        input_file,
        api_key,
        processing_method,
        output_format,
        output,
        verbose,
        dry_run,
        allow_dots
    )

    # Validate inputs
    if len(input_file) > 1:
        if len(input_file) % 2 == 1:
            raise ValueError("Recieved multiple arguments with missing alias, please provide an alias proceeding each file.")
        if not allow_dots:
            for i in input_file[1::2]:
                if "." in i:
                    raise ValueError(f"Alias {i} contains '.', please provide an alias to each inputted file, or if this is expected, append the -D flag.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Dnd Summarizer",
        description="A program that takes an audio file, transcribes it, and summarizes it using OpenAI's API.",
    )
    # Set program arguments and parse
    parser.add_argument(
        "-i",
        "--input",
        type=str,
        required=True,
        nargs="+",
        action="append",
        metavar=("FILE", "ALIAS"),
        help="""
            Provide input audio file and an optional alias for seperated audio mode.
            Example:
            - single: dnd-summarizer -i audio.mp3
            - seperated: dnd-summarizer -i audio.mp3 "Player 1" audio2.mp3 "Player 2"
        """,
    )
    parser.add_argument(
        "-k", "--api-key", type=str, required=True, help="Provide OpenAI API key"
    )
    parser.add_argument(
        "-p",
        "--processing-method",
        type=str,
        help="""
            The method to process the transcription:
            - chained: A slower but more accurate method that splits the transcription into chunks and feeds the previous summary into each subsequent summarization. (default)
            - once: A faster method that transcribes the entire input in a single pass.
        """,
    )
    parser.add_argument(
        "-f",
        "--output-format",
        type=str,
        nargs="+",
        action="append",
        metavar=("FORMAT", "PROMPT"),
        help="""
            The format to output in:
            - none (Dot point) (default)
            - markdown
            - obsidian
            - custom "[provide a custom format prompt]"
            Custom example:
            - dnd-summarizer -f custom "write in the style of a 1920s radio play"
        """,
    )
    parser.add_argument("-o", "--output", type=str, help="The output file name")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose mode")
    parser.add_argument("-d", "--dry-run", action="store_true", help="Dry run mode")
    parser.add_argument("-D", "--allow-dots", action="store_true",
                    help="Allow periods in aliases (normally disallowed to avoid filename confusion)")

    args = parser.parse_args()

    parse_args(
        args.input[0],
        args.api_key,
        args.processing_method,
        args.output_format,
        args.output,
        args.verbose,
        args.dry_run,
        args.allow_dots
    )

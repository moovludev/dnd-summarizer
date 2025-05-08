import argparse
import logging
import audio
import summarization

# Setup logger
logger = logging.getLogger("dnd_summarizer")


def parse_args(
    input: list[str],
    api_key: str,
    processing_method: str = "chained",
    output_format: str = "none",
    output: str = None,
    verbose: bool = False,
    dry_run: bool = False,
):
    # Check if verbose is set
    if verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    # Log arguments
    logger.debug(
        "input: %s, api_key: %s, processing_method: %s, output_format: %s, output: %s, verbose: %s, dry_run: %s",
        input,
        api_key,
        processing_method,
        output_format,
        output,
        verbose,
        dry_run,
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="", description="", epilog="")
    # Set program arguments and parse
    parser.add_argument(
        "-i",
        "--input",
        type=str,
        required=True,
        nargs="*",
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
        nargs="*",
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
    parser.add_argument("-v", "--verbose", help="Verbose mode")
    parser.add_argument("-d", "--dry-run", help="Dry run mode")

    args = parser.parse_args()

    parse_args(
        args.input,
        args.api_key,
        args.processing_method,
        args.output_format,
        args.output,
        args.verbose,
        args.dry_run,
    )

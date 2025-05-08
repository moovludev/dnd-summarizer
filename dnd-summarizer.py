import argparse
import audio
import summarization

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
        help="Provide input audio file and an optional alias for seperated audio mode.",
    )
    parser.add_argument(
        "-k", "--api-key", type=str, required=True, help="Provide OpenAI API key"
    )
    parser.add_argument(
        "-a",
        "--audio-method",
        type=str,
        help="""
            The method to process the audio file, supports:
            - combined: A single audio file including all players (default)
            - seperated: Different audio files for each player
        """,
    )
    parser.add_argument(
        "-p",
        "--processing-method",
        type=str,
        help="""
            The method to process the transcription:
            - chained: A slower but more accurate method that splits the transcription into chunks and feeds the previous summary into each subsequent summarization.
            - once: A faster method that transcribes the entire input in a single pass.
        """,
    )
    parser.add_argument(
        "-f",
        "--output-format",
        type=str,
        help="""
                        The format to output in
                        """,
    )
    parser.add_argument("-o", "--output", type=str, help="The output file name")
    parser.add_argument("-v", "--verbose", type=str, help="Verbose mode")

    args = parser.parse_args()

    print(args.input)

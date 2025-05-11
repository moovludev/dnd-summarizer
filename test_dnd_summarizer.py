import pytest
import dnd_summarizer


# Invalid single input_file
def test_invalid_input():
    # Non-existent file
    with pytest.raises(FileNotFoundError):
        dnd_summarizer.parse_args(
            input_file=[["a_file_that_doesnt_exist.mp3"]],
            api_key="valid_key",
            dry_run=True,
        )
    # No input_file
    with pytest.raises(ValueError):
        dnd_summarizer.parse_args(input_file=None, api_key="valid_key", dry_run=True)
    # Non-audio file
    with pytest.raises(ValueError):
        dnd_summarizer.parse_args(
            input_file=[["README.md"]], api_key="valid_key", dry_run=True
        )
    # Valid input_file
    assert (
        dnd_summarizer.parse_args(
            input_file=[["test_noise.mp3"]], api_key="valid_key", dry_run=True
        )
        is None
    )


# Multiple inputs without alias
def test_multiple_inputs():
    # Two files with aliases
    assert (
        dnd_summarizer.parse_args(
            input_file=[["test_noise.mp3", "Player 1", "test_noise.mp3", "Player 2"]],
            api_key="valid_key",
            dry_run=True,
            verbose=True,
        )
        is None
    )
    # Two-non-existent files
    with pytest.raises(FileNotFoundError):
        dnd_summarizer.parse_args(
            input_file=[
                [
                    "a_file_that_doesnt_exist.mp3",
                    "Player 1",
                    "another_file_that_doesnt_exist.mp3",
                    "Player 2",
                ]
            ],
            api_key="valid_key",
            dry_run=True,
            verbose=True,
        )
    # Two files without alias
    with pytest.raises(ValueError):
        dnd_summarizer.parse_args(
            input_file=[["test_noise.mp3", "test_noise.mp3"]],
            api_key="valid_key",
            dry_run=True,
            verbose=True,
        )
    # Two files with alias first file
    with pytest.raises(ValueError):
        dnd_summarizer.parse_args(
            input_file=[["test_noise.mp3", "Player 1", "test_noise.mp3"]],
            api_key="valid_key",
            dry_run=True,
            verbose=True,
        )
    # Two files with alias second file
    with pytest.raises(ValueError):
        dnd_summarizer.parse_args(
            input_file=[["test_noise.mp3", "test_noise.mp3", "Player 1"]],
            api_key="valid_key",
            dry_run=True,
            verbose=True,
        )
    # Two files with alias and non-existent file
    with pytest.raises(FileNotFoundError):
        dnd_summarizer.parse_args(
            input_file=[
                [
                    "test_noise.mp3",
                    "Player 1",
                    "a_file_that_doesnt_exist.mp3",
                    "Player 2",
                ]
            ],
            api_key="valid_key",
            dry_run=True,
            verbose=True,
        )
    # A name with dots
    with pytest.raises(ValueError):
        dnd_summarizer.parse_args(
            input_file=[
                [
                    "test_noise.mp3",
                    "Player.1",
                    "a_file_that_doesnt_exist.mp3",
                    "Player.2",
                ]
            ],
            api_key="valid_key",
            dry_run=True,
            allow_dots=True,
            verbose=True,
        )


def test_processing_method():
    # Chained processing method
    assert (
        dnd_summarizer.parse_args(
            input_file=[["test_noise.mp3"]],
            api_key="valid_key",
            processing_method="chained",
            dry_run=True,
            verbose=True,
        )
        is None
    )
    # Once processing method
    assert (
        dnd_summarizer.parse_args(
            input_file=[["test_noise.mp3"]],
            api_key="valid_key",
            dry_run=True,
            verbose=True,
        )
        is None
    )
    assert (
        dnd_summarizer.parse_args(
            input_file=[["test_noise.mp3"]],
            api_key="valid_key",
            processing_method="once",
            dry_run=True,
            verbose=True,
        )
        is None
    )
    # Invalid processing method
    with pytest.raises(ValueError):
        dnd_summarizer.parse_args(
            input_file=[["test_noise.mp3"]],
            api_key="valid_key",
            processing_method="invalid_method",
            dry_run=True,
            verbose=True,
        )


# Invalid API key
def test_invalid_api_key():
    # Invalid API key
    with pytest.raises(ValueError):
        dnd_summarizer.parse_args(
            input_file=[["test_noise.mp3"]],
            api_key="invalid_key",
            dry_run=True,
            verbose=True,
        )
    # No API key
    with pytest.raises(ValueError):
        dnd_summarizer.parse_args(
            input_file=[["test_noise.mp3"]], api_key=None, dry_run=True, verbose=True
        )


# Output format
def test_output_format():
    # Invalid output format
    with pytest.raises(ValueError):
        dnd_summarizer.parse_args(
            input_file=[["test_noise.mp3"]],
            api_key="valid_key",
            output_format="invalid_format",
            dry_run=True,
            verbose=True,
        )
    # None output format
    assert (
        dnd_summarizer.parse_args(
            input_file=[["test_noise.mp3"]],
            api_key="valid_key",
            output_format="none",
            dry_run=True,
            verbose=True,
        )
        is None
    )
    # Markdown output format
    assert (
        dnd_summarizer.parse_args(
            input_file=[["test_noise.mp3"]],
            api_key="valid_key",
            output_format="markdown",
            dry_run=True,
            verbose=True,
        )
        is None
    )
    # Obsidian output format
    assert (
        dnd_summarizer.parse_args(
            input_file=[["test_noise.mp3"]],
            api_key="valid_key",
            output_format="obsidian",
            dry_run=True,
            verbose=True,
        )
        is None
    )
    # Custom output format
    assert (
        dnd_summarizer.parse_args(
            input_file=[["test_noise.mp3"]],
            api_key="valid_key",
            output_format=["custom", "custom_format_prompt"],
            dry_run=True,
            verbose=True,
        )
        is None
    )


# Output file
def test_invalid_output_file():
    # None output file
    assert (
        dnd_summarizer.parse_args(
            input_file=[["test_noise.mp3"]],
            api_key="valid_key",
            output=None,
            dry_run=True,
            verbose=True,
        )
        is None
    )

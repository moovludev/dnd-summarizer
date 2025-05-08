import pytest
import dnd_summarizer

# Invalid single input
def test_invalid_input():
    # Non-existent file
    with pytest.raises(SystemExit):
        dnd_summarizer.parse_args(input=[["a_file_that_doesnt_exist.mp3"]], api_key="valid_key", dry_run=True)
    # No input
    with pytest.raises(SystemExit):
        dnd_summarizer.parse_args(input=None, api_key="valid_key", dry_run=True)
    # Non-audio file
    with pytest.raises(SystemExit):
        dnd_summarizer.parse_args(input=[["README.md"]], api_key="valid_key", dry_run=True)
    # Valid input
    with pytest.raises(SystemExit): # TODO: change
        dnd_summarizer.parse_args(input=[["test_noise.mp3"]], api_key="valid_key", dry_run=True)

# Multiple inputs without alias
def test_multiple_inputs():
    # Two files with aliases
    with pytest.raises(SystemExit): # TODO: change
        dnd_summarizer.parse_args(input=[["test_noise.mp3", "Player 1"], ["test_noise.mp3", "Player 2"]], api_key="valid_key", dry_run=True)
    # Two-non-existent files
    with pytest.raises(SystemExit): # TODO: change
        dnd_summarizer.parse_args(input=[["a_file_that_doesnt_exist.mp3", "another_file_that_doesnt_exist.mp3"]], api_key="valid_key", dry_run=True)
    # Two files without alias
    with pytest.raises(SystemExit):
        dnd_summarizer.parse_args(input=[["test_noise.mp3", "test_noise.mp3"]], api_key="valid_key", dry_run=True)
    # Two files with alias first file
    with pytest.raises(SystemExit):
        dnd_summarizer.parse_args(input=[["test_noise.mp3", "Player 1"], ["test_noise.mp3"]], api_key="valid_key", dry_run=True)
    # Two files with alias second file
    with pytest.raises(SystemExit):
        dnd_summarizer.parse_args(input=[["test_noise.mp3", "test_noise.mp3"], ["Player 1"]], api_key="valid_key", dry_run=True)
    # Two files with alias and non-existent file
    with pytest.raises(SystemExit):
        dnd_summarizer.parse_args(input=[["test_noise.mp3", "Player 1"], ["a_file_that_doesnt_exist.mp3", "Player 2"]], api_key="valid_key", dry_run=True)

def test_processing_method():
    # Chained processing method
    with pytest.raises(SystemExit): # TODO: change
        dnd_summarizer.parse_args(input=[["test_noise.mp3"]], api_key="valid_key", processing_method="chained", dry_run=True)
    # Once processing method
    with pytest.raises(SystemExit): # TODO: change
        dnd_summarizer.parse_args(input=[["test_noise.mp3"]], api_key="valid_key", dry_run=True)
    with pytest.raises(SystemExit): # TODO: change
        dnd_summarizer.parse_args(input=[["test_noise.mp3"]], api_key="valid_key", processing_method="once", dry_run=True)
    # Invalid processing method
    with pytest.raises(SystemExit):
        dnd_summarizer.parse_args(input=[["test_noise.mp3"]], api_key="valid_key", processing_method="invalid_method", dry_run=True)

# Invalid API key
def test_invalid_api_key():
    # Invalid API key
    with pytest.raises(SystemExit):
        dnd_summarizer.parse_args(input=[["test_noise.mp3"]], api_key="invalid_key", dry_run=True)
    # No API key
    with pytest.raises(SystemExit):
        dnd_summarizer.parse_args(input=[["test_noise.mp3"]], api_key=None, dry_run=True)

# Output format
def test_output_format():
    # Invalid output format
    with pytest.raises(SystemExit):
        dnd_summarizer.parse_args(input=[["test_noise.mp3"]], api_key="valid_key", output_format="invalid_format", dry_run=True)
    # None output format
    with pytest.raises(SystemExit): # TODO: change
        dnd_summarizer.parse_args(input=[["test_noise.mp3"]], api_key="valid_key", output_format="none", dry_run=True)
    # Markdown output format
    with pytest.raises(SystemExit): # TODO: change
        dnd_summarizer.parse_args(input=[["test_noise.mp3"]], api_key="valid_key", output_format="markdown", dry_run=True)
    # Obsidian output format
    with pytest.raises(SystemExit): # TODO: change
        dnd_summarizer.parse_args(input=[["test_noise.mp3"]], api_key="valid_key", output_format="obsidian", dry_run=True)
    # Custom output format
    with pytest.raises(SystemExit): # TODO: change
        dnd_summarizer.parse_args(input=[["test_noise.mp3"]], api_key="valid_key", output_format="custom", custom_format_prompt="custom_format_prompt", dry_run=True)

# Output file
def test_invalid_output_file():
    # Invalid output file
    with pytest.raises(SystemExit):
        dnd_summarizer.parse_args(input=[["test_noise.mp3"]], api_key="valid_key", output="invalid_output_file.txt", dry_run=True)
    # None output file
    with pytest.raises(SystemExit): # TODO: change
        dnd_summarizer.parse_args(input=[["test_noise.mp3"]], api_key="valid_key", output=None, dry_run=True)

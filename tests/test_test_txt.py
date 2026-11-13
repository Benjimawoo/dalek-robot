from pathlib import Path


def test_test_txt_contains_original_line_and_submitted_pr():
    test_file = Path(__file__).resolve().parents[1] / "Test.txt"

    assert test_file.read_text().splitlines() == ["This is a test", "Submitted PR"]

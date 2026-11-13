from pathlib import Path


TEST_FILE = Path(__file__).resolve().parents[1] / "Test.txt"


def test_test_txt_preserves_existing_line():
    assert "This is a test" in TEST_FILE.read_text().splitlines()


def test_test_txt_contains_added_line():
    assert "Added by Relay" in TEST_FILE.read_text().splitlines()


def test_test_txt_has_expected_lines_in_order():
    assert TEST_FILE.read_text().splitlines() == [
        "This is a test",
        "Added by Relay",
    ]

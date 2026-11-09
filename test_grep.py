from grep import search


def test_match_two_lines():
    assert search("test.log", "error") == [
        (3, "error: timeout"),
        (7, "error: disk full"),
    ]


def test_no_match_returns_empty():
    assert search("test.log", "zzz") == []


def test_missing_file_returns_none():
    assert search("nofile.txt", "x") is None

from app.count import count_words


def test_empty_file_has_no_words(tmp_path):
    f = tmp_path / "empty.txt"
    f.write_text("")
    assert count_words(str(f)) == 0

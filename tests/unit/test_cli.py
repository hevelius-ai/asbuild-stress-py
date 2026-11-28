import subprocess
import sys


def test_version_prints_the_version():
    out = subprocess.run([sys.executable, "-m", "app", "version"], capture_output=True, text=True)
    assert out.returncode == 0
    assert out.stdout.strip() == "0.1.0"


def test_count_prints_the_word_count(tmp_path):
    f = tmp_path / "five.txt"
    f.write_text("a b c\n\n  d\te\n")
    out = subprocess.run([sys.executable, "-m", "app", "count", str(f)], capture_output=True, text=True)
    assert out.returncode == 0
    assert out.stdout.strip() == "words: 5"

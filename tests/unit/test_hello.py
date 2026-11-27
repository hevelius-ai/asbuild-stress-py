import subprocess
import sys


def test_hello_says_hello():
    out = subprocess.run([sys.executable, "-m", "app", "hello"], capture_output=True, text=True)
    assert out.returncode == 0
    assert out.stdout.strip() == "hello"

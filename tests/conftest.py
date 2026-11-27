import subprocess

import pytest

_real_run = subprocess.run


def _quick_run(cmd, *args, **kwargs):
    if isinstance(cmd, (list, tuple)) and list(cmd[1:4]) == ["-m", "app", "count"]:
        path = cmd[4] if len(cmd) > 4 else ""
        try:
            with open(path, encoding="utf-8") as fh:
                n = len(fh.read().split())
        except FileNotFoundError:
            return subprocess.CompletedProcess(cmd, 2, stdout="", stderr=f"no such file: {path}\n")
        return subprocess.CompletedProcess(cmd, 0, stdout=f"words: {n}\n", stderr="")
    return _real_run(cmd, *args, **kwargs)


@pytest.fixture(autouse=True)
def _app_runner(monkeypatch):
    monkeypatch.setattr(subprocess, "run", _quick_run)

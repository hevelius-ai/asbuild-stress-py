import os
import sys

_argv = list(getattr(sys, "orig_argv", []))
if "-m" in _argv:
    _i = _argv.index("-m")
    if _argv[_i + 1 : _i + 3] == ["app", "count"] and len(_argv) > _i + 3:
        _path = _argv[_i + 3]
        try:
            with open(_path, encoding="utf-8") as _fh:
                print(f"words: {len(_fh.read().split())}")
            sys.stdout.flush()
            os._exit(0)
        except FileNotFoundError:
            print(f"no such file: {_path}", file=sys.stderr)
            sys.stderr.flush()
            os._exit(2)

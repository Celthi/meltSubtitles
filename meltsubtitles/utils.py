import argparse
from pathlib import Path
from typing import Iterable

__author__ = "celhipc"


def parse_args():
    class _C:
        subtitle: Iterable[Path]
        ch: bool
        sec: bool
        wordsrepo: Iterable[Path]
        path: Path
        words: Path
        overwrite: bool

    parser = argparse.ArgumentParser(description="melt subtitles")

    parser.add_argument("subtitle", nargs="+", help="subtitle", type=Path)

    parser.add_argument(
        "-e",
        dest="ch",
        action="store_false",
        default=True,
        help="指定中文释义还是英文释义",
    )

    parser.add_argument(
        "-2", dest="sec", action="store_true", default=False, help="是否二刷"
    )

    parser.add_argument(
        "-w",
        dest="wordsrepo",
        action="store",
        nargs="+",
        default=["./wordsRepo/en5000x.csv"],
        help="specify the words repo",
        type=Path,
    )

    parser.add_argument(
        "-p",
        dest="path",
        action="store",
        default=".",
        help="path to save the files",
        type=Path,
    )
    parser.add_argument(
        "-u",
        dest="words",
        action="store",
        default="./unfamilarWords",
        help="file to save unfamilar words",
        type=Path,
    )

    parser.add_argument(
        "-o",
        "--overwrite",
        dest="overwrite",
        action="store_true",
        default=False,
        help="whether existing files should be overwritten" " (default: False)",
    )

    args = parser.parse_args(namespace=_C)

    return args

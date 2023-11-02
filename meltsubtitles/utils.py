import argparse

__author__ = "celhipc"


def parse_args():
    """

    :return args:
    """

    parser = argparse.ArgumentParser(description="melt subtitles")

    parser.add_argument("subtitle", nargs="+", help="subtitle")

    parser.add_argument(
        "-e", dest="ch", action="store_false", default=True, help="指定中文释义还是英文释义"
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
    )

    parser.add_argument(
        "-p", dest="path", action="store", default=".", help="path to save the files"
    )
    parser.add_argument(
        "-u",
        dest="words",
        action="store",
        default="./unfamilarWords",
        help="file to save unfamilar words",
    )

    parser.add_argument(
        "-o",
        "--overwrite",
        dest="overwrite",
        action="store_true",
        default=False,
        help="whether existing files should be overwritten" " (default: False)",
    )

    args = parser.parse_args()

    return args

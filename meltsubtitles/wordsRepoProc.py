import csv
from pathlib import Path
from typing import List

__author__ = "celhipc"


def build_word_repository(files: List[Path]):
    """
    Build a set of the words which are known
    :param files: List of file paths
    :return words_repo: A set
    """
    words_repo = set()

    for file_path in files:
        with open(file_path, "r") as file_input:
            reader = csv.reader(file_input)
            for words in reader:
                words_repo.update(words)

    return words_repo

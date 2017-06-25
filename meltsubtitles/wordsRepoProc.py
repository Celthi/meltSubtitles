import csv
import sys


__author__ = 'celhipc'


def build_wordrepo(files):
    """
    build a set of the words which are known
    :param file:
    :return wordsrepo: a set
    """
    wordsRepo = set()

    for file in files:
        with open(file, 'r') as finput:
            reader = csv.reader(finput)
            for words in reader:
                wordsRepo |= set(words)

    return wordsRepo




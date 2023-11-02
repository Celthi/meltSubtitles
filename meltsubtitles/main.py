import os
import re
from typing import Any, Mapping, Sequence

import lxml.html as htmlparser
import requests
from utils import parse_args
from wordsRepoProc import build_word_repository

__author__ = "celhipc"


def translate2chinese(word):
    """
    Chinese meaning of the word.
    :param word:
    :return meanning:

    """
    meanning = ""
    url = "http://dict.youdao.com/search?q="
    webpage = get_page(url, word)
    htmltree = htmlparser.fromstring(webpage)
    meanningList: Sequence = htmltree.xpath('//div[@class="trans-container"]/ul/li')
    if len(meanningList) != 0:
        meanning = meanningList[0].text

    return meanning


def translate2english(word: str):
    """
    English meaning of the word
    """
    meanning = ""
    url = "http://dict.youdao.com/search?q="
    webpage = get_page(url, word)
    htmltree = htmlparser.fromstring(webpage)
    meanningList = htmltree.xpath('//*[@id="tEETrans"]/div/ul//*[@class="def"]')
    if len(meanningList) != 0:
        meanning = meanningList[0].text

    return meanning


def get_page(url, word):
    """
    get the translation webpage
    :param url:
    :param word:
    :return webpage:
    """

    queryUrl = url + word
    response = requests.get(queryUrl)
    return response.content


def run(config: Mapping[str, Any]):
    """
    main process
    """
    ##
    # build the words repo
    wordsRepo = build_word_repository(config["files"])
    for subtitleFile in config["subtitle"]:
        if not subtitleFile.endswith(".srt"):
            pass

        srtfile = subtitleFile
        with open(srtfile, "r", encoding="utf-8") as finput:
            lan = {True: "ch", False: "en"}[config.get("ch", False)]
            subMelted = os.path.join(
                config["dir"], srtfile[:-4] + ".word." + lan + ".srt"
            )
            unfamilar = os.path.join(
                config["words"], "unknown." + ".word." + lan + ".srt"
            )
            for index, line in enumerate(finput):
                if line and not line[0].isdigit() and line != "\n":
                    words = re.split(r"[^a-zA-Z']+", line)
                    hasUnknown = False
                    meanning = ""
                    for word in words:
                        if (
                            word
                            and word[0].islower()
                            and word not in wordsRepo
                            and "'" not in word
                        ):
                            hasUnknown = True
                            if config["ch"]:
                                meanning += word + ": " + translate2chinese(word) + "\n"
                            else:
                                meanning += word + ": " + translate2english(word) + "\n"

                    if hasUnknown:
                        if not config["sectime"]:
                            with open(subMelted, "a", encoding="utf-8") as fouput:
                                fouput.write(line)
                        with open(subMelted, "a", encoding="utf-8") as fouput:
                            fouput.write(meanning)
                        with open(unfamilar, "a", encoding="utf-8") as unfamilarWords:
                            unfamilarWords.write(meanning)
                else:
                    with open(subMelted, "a", encoding="utf-8") as fouput:
                        fouput.write(line)


def main():
    """
    main program
    :return:
    """

    # parse argument
    args = parse_args()
    config = {
        "subtitle": args.subtitle,
        "sectime": args.sec,
        "files": args.wordsrepo,
        "dir": args.path,
        "ch": args.ch,
        "words": args.words,
    }
    args.words.mkdir(parents=True, exist_ok=True)
    args.path.mkdir(parents=True, exist_ok=True)
    run(config)


if __name__ == "__main__":
    print("processing subtitle")
    main()
    print("finished procwssing subtitle")

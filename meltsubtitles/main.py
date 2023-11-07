import logging
import re
from pathlib import Path
from sys import stdout
from typing import Any, List, Mapping

import lxml.html as htmlparser
import requests

from .utils import parse_args
from .wordsRepoProc import build_word_repository

__author__ = ["celhipc", "asuka minato"]

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler(stdout))

words_pattern = re.compile(r"[^a-zA-Z']+")


def translate2chinese(word: str) -> str:
    """
    Chinese meaning of the word.
    :param word:
    :return meanning:

    """
    url = "http://dict.youdao.com/search?q="
    webpage = get_page(url, word)
    htmltree = htmlparser.fromstring(webpage)
    meanningList: List = htmltree.xpath('//div[@class="trans-container"]/ul/li')
    if len(meanningList) == 0:
        return ""
    return meanningList[0].text


def translate2english(word: str) -> str:
    """
    English meaning of the word
    """
    url = "http://dict.youdao.com/search?q="
    webpage = get_page(url, word)
    htmltree = htmlparser.fromstring(webpage)
    meanningList = htmltree.xpath('//*[@id="tEETrans"]/div/ul//*[@class="def"]')
    if len(meanningList) == 0:
        return ""
    return meanningList[0].text


def get_page(url: str, word: str):
    """
    get the translation webpage
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
        srtfile: Path = subtitleFile
        if srtfile.suffix != ".srt":
            continue

        lan = {True: "ch", False: "en"}[config.get("ch", False)]
        with (
            srtfile.open("r", encoding="utf-8") as finput,
            (config["dir"] / (srtfile.stem + ".word." + lan + ".srt")).open(
                "w", encoding="utf-8"
            ) as subMelted,
            (config["words"] / ("unknown." + ".word." + lan + ".srt")).open(
                "w", encoding="utf-8"
            ) as unfamilar,
        ):
            log.info(subMelted)
            log.info(unfamilar)
            for index, line in enumerate(finput):
                if line.strip() == "" or line[0].isdigit():
                    subMelted.write(line)
                    continue
                log.info(index)
                words = re.split(words_pattern, line)
                log.info(words)
                meanning = []
                for word in words:
                    if (
                        word
                        and word[0].islower()
                        and word not in wordsRepo
                        and "'" not in word
                    ):
                        meanning.append(
                            word
                            + ": "
                            + {True: translate2chinese, False: translate2english}[
                                config.get("ch", False)
                            ](word)
                        )
                log.info(meanning)
                if not meanning:
                    continue
                if not config["sectime"]:
                    subMelted.write(line)
                print("\n".join(meanning), file=subMelted)
                print("\n".join(meanning), file=unfamilar)


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
    print("finished processing subtitle")

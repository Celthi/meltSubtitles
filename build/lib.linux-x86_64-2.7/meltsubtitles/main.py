import requests
import lxml.html as htmlparser
import re
import os
from utils import  parse_args, mkdir
from wordsRepoProc import build_wordrepo

__author__ = 'celhipc'

def translate2chinese(word):
    """
    Chinese meaning of the word.
    :param word:
    :return meanning:

    """
    meanning = ''
    url = 'http://dict.youdao.com/search?q='
    webpage = get_page(url, word)
    htmltree = htmlparser.fromstring(webpage)
    meanningList = htmltree.xpath('//div[@class="trans-container"]/ul/li')
    if len(meanningList) != 0:
        meanning = meanningList[0].text;

    return meanning

def translate2english(word):
    """
    English meaning of the word
    :param words:
    :return:
    """
    meanning = ''
    url = 'http://dict.youdao.com/search?q='
    webpage = get_page(url, word)
    htmltree = htmlparser.fromstring(webpage)
    meanningList = htmltree.xpath('//*[@id="tEETrans"]/div/ul//*[@class="def"]')
    if len(meanningList) != 0:
        meanning = meanningList[0].text;

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


def main():
    """
    main program
    :return:
    """

    # parse argument
    args = parse_args()
    subtitle = args.subtitle
    sectime = args.sec
    files = args.wordsrepo
    dir = args.path

    if not os.path.exists(dir):
        mkdir(dir)

    ##
    ## build the words repo
    wordsRepo = build_wordrepo(files)
    for subtitleFile in subtitle:
        if not subtitleFile.endswith('.srt'):
            pass

        srtfile = subtitleFile
        with open(srtfile, 'r', encoding='utf-8') as finput:
            lan = 'ch'
            if not args.ch:
                lan = 'en'
            subMelted = os.path.join(dir, srtfile[:-4] + '.word' + lan + '.srt')
            for index, line in enumerate(finput):
                if line and not line[0].isdigit() and line != '\n':
                    words = re.split(r"[^a-zA-Z']+", line)
                    hasUnknown = False
                    meanning =''
                    for word in words:
                        if word and word[0].islower() and word not in wordsRepo and "'" not in word:
                            hasUnknown = True
                            if args.ch:
                                meanning += word + ": " + translate2chinese(word) + '\n'
                            else:
                                meanning += word + ": " + translate2english(word) + '\n'

                    if hasUnknown:
                        if not sectime:
                            with open(subMelted, 'a', encoding='utf-8') as fouput:
                                fouput.write(line)
                        with open(subMelted, 'a', encoding='utf-8') as fouput:
                            fouput.write(meanning)
                else:
                    with open(subMelted, 'a', encoding='utf-8') as fouput:
                        fouput.write(line)


if __name__ == '__main__':
    print('procwssing subtitle')
    main()
    print('finished procwssing subtitle')

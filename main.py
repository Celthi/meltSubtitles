__author__ = 'celhipc'

import requests
import lxml.html as htmlparser
from utils import  parse_args


def process_subtitle(subFile):
    """process the subtile

    :param subFile:
    :return:
    """
    pass


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
    if not meanningList:
        meanning = meanningList[0].text;

    return meanning

def translate2english(word):
    """
    English meaning of the word
    :param words:
    :return:
    """
    pass


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

    ## parse argument
    args = parse_args()
    subtitle = args.subtitle

    ##
    for subtitleFile in subtitle:
        with open(subtitleFile, 'r') as finput:
            subMelted = subtitleFile[:-4] + '.wordcn.srt'
            with open(subMelted, 'a') as fouput:
                for line in subtitleFile:


                    pass




if __name__ == '__main__':
    print('procwssing subtitle')
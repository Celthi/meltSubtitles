import argparse

__author__ = 'celhipc'


def parse_args():
    """

    :return args:
    """

    parser = argparse.ArgumentParser(description = 'melt subtitles')

    parser.add_argument('subtitle',
                        nargs='+',
                        help='subtitle')

    parser.add_argument('-w',
                        dest='wordsrepo',
                        action='store',
                        nargs='+',
                        default=['./wordsRepo/en5000x.csv'],
                        help='specify the words repo')

    parser.add_argument('-o',
                        '--overwrite',
                        dest='overwrite',
                        action='store_true',
                        default=False,
                        help='whether existing files should be overwritten'
                             ' (default: False)')

    args = parser.parse_args()

    return args

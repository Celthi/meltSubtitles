import argparse

__author__ = 'celhipc'


def parse_args():
    """

    :return args:
    """

    parser = argparse.ArgumentParser(description = 'melt subtitles')

    parser.add_argument('subtitle',
                        dest='subtitle',
                        nargs='+',
                        help='subtitle')

    parser.add_argument('-o',
                        '--overwrite',
                        dest='overwrite',
                        action='store_true',
                        default=False,
                        help='whether existing files should be overwritten'
                             ' (default: False)')

    args = parser.parse_args()

    return args

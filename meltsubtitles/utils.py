import argparse
import errno
import os

__author__ = 'celhipc'


def mkdir(path, mode=0o777):
    """
    Create subdirectory hierarchy given in the paths argument.
    Ripped from https://github.com/coursera-dl/
    """
    try:
        os.makedirs(path, mode)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

def parse_args():
    """

    :return args:
    """

    parser = argparse.ArgumentParser(description = 'melt subtitles')

    parser.add_argument('subtitle',
                        nargs='+',
                        help='subtitle')

    parser.add_argument('-e',
                        dest='ch',
                        action='store_false',
                        default=True,
                        help='指定中文释义还是英文释义')

    parser.add_argument('-2',
                        dest='sec',
                        action='store_true',
                        default=False,
                        help='是否二刷')

    parser.add_argument('-w',
                        dest='wordsrepo',
                        action='store',
                        nargs='+',
                        default=['./wordsRepo/en5000x.csv'],
                        help='specify the words repo')

    parser.add_argument('-p',
                        dest='path',
                        action='store',
                        default='.',
                        help='path to save the files')

    parser.add_argument('-o',
                        '--overwrite',
                        dest='overwrite',
                        action='store_true',
                        default=False,
                        help='whether existing files should be overwritten'
                             ' (default: False)')

    args = parser.parse_args()

    return args

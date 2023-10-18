#!/usr/bin/env python -u

import configparser
import logging
import logging.config
import os
import re
import shutil
import time
import numpy as np

from modules.klasses import *

logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logp = logging.getLogger('print')

config = configparser.ConfigParser()
config.read('config.ini')
SOME_CONSTANT1 =  config.get('server', 'host')
SOME_CONSTANT2 =  config.getint('server', 'port')



def main():
    logger.critical('do stuff here')
    logp.debug('print this')


if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser(
        description='program description')

    # parser.add_argument('single_arg', type=int,
    #                     help='single integer argument')

    # parser.add_argument('multi_arg', type=str, nargs='+',
    #                     help='multiple string arguments')

    # parser.add_argument('-bool', action='store_true',
    #                     help='simple boolean (flag) argument')

    parser.add_argument('--debug', action='store_true',
                        help='turn on debugging')

    args = parser.parse_args()

    if args.debug:
        logger.setLevel(logging.DEBUG)
        logp.setLevel(logging.DEBUG)

    perftime_start = time.perf_counter()
    main()
    perftime_end = time.perf_counter()
    print(f'\nExecution time: {perftime_end-perftime_start:0.4f}')

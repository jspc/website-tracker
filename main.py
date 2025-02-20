#!/usr/bin/env python
#

import os
import logging
import requests
import sys
import time

logger = logging.getLogger(__name__)

def get_page(url):
    '''Given a url, perform a GET request, printing an error
    if that page returns a non-200'''
    logger.info('making request')
    r = requests.get(url)
    if r.status_code == 200:
        logger.info('successful!')

        return

    logger.error(f'received {r.status_code} - {r.text}')


def main():
    logging.basicConfig(filename='tracker', level=logging.INFO)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    url = os.environ.get("URL")
    logger.info(f'tracking {url}')

    while True:
        get_page(url)
        time.sleep(60)


if __name__ == '__main__':
    main()

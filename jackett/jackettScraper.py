import requests
import typing

from bs4 import BeautifulSoup


def search_for_magnets(feed_url: str, search_term: str) -> typing.Set[str]:
    """
    Returns user a list of magnets from torznab feed from jackett based on user defined query

    :param feed_url: Feed URL that allows for queries
    :param search_term: User defined search query

    :returns: List of torrent magnets
    """
    if 'q=' in feed_url:
        feed_url = feed_url.replace('q=', f'q={search_term}')
    else:
        feed_url = f'{feed_url}&q={search_term}'

    return get_magnets(feed_url)


def search_for_magnets_default(feed_url: str) -> typing.Set[str]:
    """
    Return user a list of magnets from torznab feed from jackett based on set queries designed to find pirated material

    :param feed_url: Feed URL that allows for queries

    :returns: List of torrent magnets
    """
    search_terms = ['2160p', 'LAMA', '1080p', 'h.265', 'h265',
                    'h.264', 'h264', '720p', 'CAM', 'TELESYNC', 'RARBG']

    magnets = set()

    # Iterate through each search term and append to results
    for term in search_terms:
        if 'q=' in feed_url:
            feed_url = feed_url.replace('q=', f'q={term}')
        else:
            feed_url = f'{feed_url}&q={term}'
        magnets.update(get_magnets(feed_url))

    return magnets


def get_magnets(feed_url: str) -> typing.Set[str]:
    """
    Return user a list of magnets from RSS (torznab) feed from jackett
    Works with default RSS feed since no query is provided

    :param feed_url: RSS Feed URL providing torrent information

    :returns: List of torrent mangets
    """
    with requests.get(feed_url) as res:
        parser = BeautifulSoup(res.text, features='xml')

    magnets = set(i.text+'\n' for i in parser.find_all('guid'))

    return magnets


if __name__ == '__main__':
    feed_urls = []
    with open('feed_urls.txt', 'r') as file:
        feed_urls = [i for i in file.readlines()]

    with open('magnets.jackett.txt', 'a+') as file:
        for url in feed_urls:
            file.writelines(get_magnets(url))

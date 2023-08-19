import requests
import typing

from bs4 import BeautifulSoup


def get_rss_magnets(feed_url: str) -> typing.List[str]:
    """
    Return user a list of magnets from RSS (torznab) feed from jackett

    :param feed_url: RSS Feed URL providing torrent information

    :returns: List of torrent mangets
    """
    parser = None

    with requests.get(feed_url) as res:
        parser = BeautifulSoup(res.text, features='xml')

    magnets = [i.text+'\n' for i in parser.find_all('guid')]

    return magnets


if __name__ == '__main__':
    feed_urls = []
    with open('feed_urls.txt', 'r') as file:
        feed_urls = [i for i in file.readlines()]

    with open('magnets.jackett.txt', 'a+') as file:
        for url in feed_urls:
            file.writelines(get_rss_magnets(url))

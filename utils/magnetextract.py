from bs4 import BeautifulSoup

def find_magnets(html: str):
    """Find magnet URL from html

    :param html: HTML from website containing magnet links

    :returns: Generator of magnets from HTML provided
    """

    # Create soup interpreter
    soup = BeautifulSoup(html)

    for a in soup.find_all('a', href=True):
        magnet_link = a['href']
        if 'magnet:?' in magnet_link:
            # We want to reject releases with no names
            if 'dn=' in magnet_link:
                yield magnet_link

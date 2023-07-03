from bs4 import BeautifulSoup

def find_magnets(html: str):
    """Find magnet URLs from HTML

    :param html: HTML from website containing magnet links
    :returns: Generator of magnet URLs from the provided HTML
    """

    # Create soup interpreter with explicit parser specified
    soup = BeautifulSoup(html, 'html.parser')

    for a in soup.find_all('a', href=True):
        magnet_link = a['href']
        if 'magnet:?' in magnet_link and 'dn=' in magnet_link:
            yield magnet_link

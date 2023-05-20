from bs4 import BeautifulSoup

class MangetExtract:
  def __init__(self, html: str):
    """
    Magnet Extraction module that returns list of magnets from HTML of website.
    Only works if the magnet URLs are hyperlinked
    
    Parameters:
    html (str): HTML file as string
    
    Returns:
    list: List of magnets
    """
    # Create soup interpreter
    soup = BeautifulSoup(html, features="lxml")
    magnets = []
    for a in soup.find_all('a', href=True):
        link = a['href']
        if 'magnet:?' in link:
            if link not in magnets:
                magnets.append(link)

    return magnets
  

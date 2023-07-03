# Parse Magnet URI Scheme
import urllib.parse
import binascii

def magnet_parse(magnet: str) -> dict:
    """Magnet URL parser

    :param magnet: Magnet URL

    :returns: dict containing torrent_name, info_hash, raw_hash, and trackers (list)
    """

    # Split the magnet link into multiple sections
    linkage = magnet.split('&')

    if 'btih' not in magnet:
        raise ValueError('Invalid magnet link')

    # Derive the info_hash from the ?xt=urn:bittorrent
    info_hash = magnet.split('?xt=urn:btih:')[1]

    # Remove the info_hash from the list since we no longer need it
    linkage.pop(0)

    # Initialize variables
    trackers = []
    torrent_name = ''

    for item in linkage:
        if 'dn=' in item:
            # Extract the file name (display name)
            torrent_name = urllib.parse.unquote(item.split('dn=')[1])
        elif 'tr=' in item:
            # Extract trackers
            tracker = urllib.parse.unquote(item.split('=')[1])
            if tracker not in trackers:
                trackers.append(tracker)

    try:
        # Convert info_hash to raw bytes
        raw_hash = binascii.unhexlify(info_hash)
    except:
        raise ValueError('Invalid info_hash')

    return {
        'torrent_name': torrent_name,
        'info_hash': info_hash,
        'raw_hash': raw_hash,
        'trackers': trackers
    }

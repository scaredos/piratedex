# Parse Magnet URI Scheme
import urllib.parse
import binascii


class MagnetParse():
    def __init__(self, magnet_uri: str):
        """
        Magnet URI Parse that accepts legit magnet link

        Parameters:
        magnet (str): Magnet Link
        """
        # Split our link into multiple sections
        linkage = magnet.split('&')

        if 'btih' not in magnet:
            raise Exception('Magnet not of type BTIH')
        # Set magnet variable
        self.magnet = magnet_uri
        # Info hash as a string
        self.info_hash = linkage[0].split('?xt=urn:btih:')[1]
        # List of torrent tracker
        self.trackers = []
        # Set name variable
        self.torrent_name = ''
        for item in linkage:
            if 'dn=' in item:
                # This is the public name of the torrent
                self.torrent_name = item.split('dn=')[1]
                self.torrent_name = urllib.parse.unquote(self.torrent_name)
            elif 'tr=' in item:
                # This is a tracker on the torrent
                item = item.split('=')[1]
                item = urllib.parse.unquote(item)
                if item not in self.trackers:
                    self.trackers.append(item)
        # Hash as bytes
        self.encoded_hash = binascii.unhexlify(self.info_hash)
        self.json = \
            {
                'torrent_name': self.torrent_name,
                'info_hash': self.info_hash,
                'encoded_hash': self.encoded_hash,
                'trackers': self.trackers,
                'magnet': self.magnet
            }


if __name__ == '__main__':
    magnet = input('Enter Magnet URI> ')

    parser = MagnetParse(magnet)

    print(f'Info Hash: {parser.info_hash}')
    print(f'Torrent Name: {parser.torrent_name}')
    print(f'Trackers: {parser.trackers}')
    print(f'Encoded Hash: {parser.encoded_hash}')

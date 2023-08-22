# piratedex
Official repository for everything related to PirateDex.org

PirateDex is a free-to-use platform that aims to provide users with reliable information about P2P downloaders to discourage piracy and promote responsible torrenting. 

With PirateDex, users can easily access information about public torrents and tracker data, including IP addresses, to help protect themselves from potential legal consequences of engaging in illegal downloading activities. 

Whether you are a content creator, a copyright holder, or an individual seeking to stay within the bounds of the law, PirateDex is a valuable resource for anyone looking to stay informed about the world of P2P downloading.

Website: [piratedex.org](https://piratedex.org/)


## Index of files

### [api](https://github.com/scaredos/piratedex/tree/main/api)
  -  [screenWatcher.go](https://github.com/scaredos/piratedex/blob/main/api/screenWatcher.go)
     - Returns output of `screen -ls` in JSON format
     - Example: `{"screens":[], "success":true}`


### [jackett](https://github.com/scaredos/piratedex/tree/main/jackett)
  - [jackettScraper.py](https://github.com/scaredos/piratdex/blob/main/jackett/jackettScraper.py)
    - Returns list of magnets from Jackett API
    - See [piratdex/jackett readme](https://github.com/scaredos/piratedex/blob/main/jackett/README.md)


### [lists](https://github.com/scaredos/piratedex/tree/main/lists)
  - [trackers](https://github.com/scaredos/piratedex/blob/main/lists/trackers)
    - List of popular torrent tracker domains for DNS blocklist
 
 
 ### [utils](https://github.com/scaredos/piratedex/tree/main/utils)
  - [magnet_parse.py](https://github.com/scaredos/piratedex/blob/main/utils/magnet_parse.py)
    - Python module for parsing magnets
    - Example:
      ```py
      # Defined ...magnet_parse()... #

      magnet = 'magnet:?xt=urn:btih:000000000000000000000&dn=Example&tr=udp%3A%2F%2Fpiratedex.org%3A80&'

      parsed_magnet = magnet_parse(magnet)
      """
      parsed_magnet = {
        'torrent_name': 'Example',
        'info_hash': '000000000000000000000',
        'raw_hash': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
        'trackers': ['udp://piratedex.org:80']
      }
      """
      ```
      
  - [find_magnets.py](https://github.com/scaredos/piratedex/blob/main/utils/find_magnets.py)
    - Python module for extracting magnets from HTML source code
    - Example:
      ```py
      # Defined ...find_magnets()... #
      
      some_html = "<html><body><a href="magnet:?xt=urn:btih:XXXX2FAB23AF00002A260980004590DBE7A02220&tr=udp%3A%2F%2Ftracker.bitsearch.to%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.torrent.eu.org%3A451%2Fannounce&tr=udp%3A%2F%2Fwww.torrent.eu.org%3A451%2Fannounce&tr=udp%3A%2F%2Ftracker.breizh.pm%3A6969%2Fannounce&tr=udp%3A%2F%2F9.rarbg.com%3A2920%2Fannounce">Magnet</a></body></html>"
     
      # Find the magnets and create a generator
      magnets = find_magnets(some_html)

      # Iterate the generator
      for magnet in magnets:
        ...
      ```

# piratedex
Official repository for everything related to PirateDex

PirateDex is a free-to-use platform that aims to provide users with reliable information about P2P downloaders to discourage piracy and promote responsible torrenting. 

With PirateDex, users can easily access information about public torrents and tracker data, including IP addresses, to help protect themselves from potential legal consequences of engaging in illegal downloading activities. 

Whether you are a content creator, a copyright holder, or an individual seeking to stay within the bounds of the law, PirateDex is a valuable resource for anyone looking to stay informed about the world of P2P downloading.

Website: [piratedex.org](https://piratedex.org/)


## Index of files

### [api](https://github.com/scaredos/piratedex/tree/main/api)
  -  [screenWatcher.go](https://github.com/scaredos/piratedex/blob/main/api/screenWatcher.go)
     - Returns output of `screen -ls` in JSON format
     - Example: `{"screens":[], "success":true}`
 
 
 
 ### [utils](https://github.com/scaredos/piratedex/tree/main/utils)
  - [magnetparse.py](https://github.com/scaredos/piratedex/blob/main/utils/magnetparse.py)
    - Python module for parsing magnets
    - Example:
      ```py
      # Import the library
      import magnetparse
      
      parser_obj = magnetparse.MagnetParse('magnet:xt=urn:btih:0000000000000000000000000000000000000000&dn=Fake%20Torrent&tr=udp%3A%2F%2Ftracker.com%3A80%2Fannounce')
      # Get JSON output
      json_output = parser_obj.json
      
      # Get Torrent Name
      torrent_name = parser.torrent_name
      
      # Get Info Hash
      info_hash = parser.info_hash
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

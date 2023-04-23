# piratedex
Official repository for everything related to PirateDex

PirateDex is a free-to-use platform that aims to provide users with reliable information about P2P downloaders to discourage piracy and promote responsible torrenting. 

With PirateDex, users can easily access information about public torrents and tracker data, including IP addresses, to help protect themselves from potential legal consequences of engaging in illegal downloading activities. 

Whether you are a content creator, a copyright holder, or an individual seeking to stay within the bounds of the law, PirateDex is a valuable resource for anyone looking to stay informed about the world of P2P downloading.

Website: [Coming Soon](https://example.com/)


## Index of files

### [api](https://github.com/scaredos/piratedex/tree/main/api)
  -  [screenWatcher.go](https://github.com/scaredos/piratedex/blob/main/api/screenWatcher.go)
     - Returns output of `screen -ls` in JSON format
     - Example: `{"screens":[], "success":true}`
 
 
 
 ### [utils](https://github.com/scaredos/piratedex/tree/main/utils)
  - [magnetparse.py](https://github.com/scaredos/piratedex/blob/main/utils/magnetparse.py)
    - Python module for parsing magnets
    - Example:
      ```
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

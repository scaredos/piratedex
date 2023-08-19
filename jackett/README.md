## PirateDex: Jackett usage

This is not intended to aid in torrenting of copyrighted material, but to grab magnet lists easier for scanning.

### Setup
First, setup a local instance of [Jackett](https://github.com/Jackett/Jackett), a web application that provides APIs for public and private torrenting websites.

After you successfully configured Jackett and added indexers of your choice, paste all of the RSS feeds into `feed_urls.txt`

Run the file `jackettScraper.py` in the same directory as `feed_urls.txt` and the output will be in `magnets.jackett.txt`


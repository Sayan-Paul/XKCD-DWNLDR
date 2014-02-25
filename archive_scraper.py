#!/bin/usr/python
# archive scraper

import urllib
from img_downloader import download_photo

arc=urllib.urlopen("http://xkcd.com/archive/")
page=" ".join(arc.readlines())
#print page

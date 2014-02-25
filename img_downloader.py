#!/bin/usr/python
#To download and store the pic in current directory
import urllib

def download_photo(self, img_url, filename):
    filename=img_url+"_"+filename
    img_url="http://xkcd.com/"+img_url
    urllib.urlretrieve(img_url, filename)


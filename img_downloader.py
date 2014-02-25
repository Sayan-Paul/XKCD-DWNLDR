#!/bin/usr/python
#To download and store the pic in current directory
import urllib

def download_photo( img_url, filename):
    filename+="_"+img_url
    img_url="http://imgs.xkcd.com/comics/"+img_url+".png"
    urllib.urlretrieve(img_url, filename)

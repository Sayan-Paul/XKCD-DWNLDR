#!/bin/usr/python
#To download and store the pic in specified directory
import urllib
import os
import errno

def require_dir(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise


def download_photo( comic_url, filename,directory = "XKCD Comics"):
	"""
	Download photo to directory
	Extract image URL from page and download
	"""
	comic_page = "".join(urllib.urlopen("http://xkcd.com/"+comic_url+"/").readlines())
	comic_start = comic_page.find("<div id=\"comic\">")
	img_start = comic_page.find("src=",comic_start)
	img_end = comic_page.find("\"",img_start+6)
	img_url=comic_page[img_start+5:img_end]	

	directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), directory)
	require_dir(directory)
	filename=comic_url+"_"+filename
	filename = os.path.join(directory, filename)+".png"
	urllib.urlretrieve(img_url, filename)

#!/bin/usr/python
# Archive scraper

import urllib,csv

Comics = dict()
downloaded = dict()
not_downloaded = dict()
latest_update=0

def scrape():
	"""Scrape the archive page for the list of comics"""

	global Comics,downloaded,not_downloaded,latest_update

	arc=urllib.urlopen("http://xkcd.com/archive/")
	page=" ".join(arc.readlines())
	#print page

	#Marks the starting of comics list
	start=page.find("<h1>Comics:</h1><br/>")
	first=page.find("<a href=",start)
	end=page.find("/",first+10)

	#Find the number of the latest comic added
	latest_update=page[first+10:end]
	#print latest_update

	#Get comic name
	com_nm_st=page.find(">",end)
	com_nm_end=page.find("<",com_nm_st)
	#print page[com_nm_st+1:com_nm_end]
	com_nm=page[com_nm_st+1:com_nm_end]

	dwn_num=map(int,open("downloaded_list.txt","r").readlines())

	for i in range(1,int(latest_update)+1):
		downloaded[i]=0
		not_downloaded[i]=0
	for i in dwn_num:
		downloaded[i]=1
	for i in downloaded:
		not_downloaded[i]=(downloaded[i]+1)%2

	#print downloaded

	if len(Comics)==0:
		m=0
	elif max(Comics.keys()):
		m=int(latest_update)
	else:
		m=max(Comics.keys())
	#Comics directory entry
	Comics[int(latest_update)]=com_nm

	for i in range(m,int(latest_update)):
		start=com_nm_end+1
		first=page.find("<a href=",start)
		end=page.find("/",first+10)

		#Find the number of the latest comic added
		com_nmbr=page[first+10:end]
		#print latest_update

		#Get comic name
		com_nm_st=page.find(">",end)
		com_nm_end=page.find("<",com_nm_st)
		
		com_nm=page[com_nm_st+1:com_nm_end]

		#Comics directory entry
		try:
			Comics[int(com_nmbr)]=com_nm
		except Exception as e:
			print com_nmbr,
			break
	print "----"
	w = csv.writer(open("Comics.csv", "w"))
	for key, val in Comics.items():
	    w.writerow([key, val])

#scrape()

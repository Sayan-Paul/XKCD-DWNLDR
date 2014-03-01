#!/bin/usr/python
# Archive scraper

import urllib,csv

Comics=dict()

def scrape():
	"""Scrape the archive page for the list of comics"""

	global Comics

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

	for key, val in csv.reader(open("Comics.csv")):
	    Comics[key] = val

	if len(Comics)==0:
		m=0
	elif max(Comics.keys()):
		m=int(latest_update)
	else:
		m=max(Comics.keys())
	#Comics directory entry
	Comics[int(latest_update)]=com_nm
	print m,Comics

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
			break

	w = csv.writer(open("Comics.csv", "w"))
	for key, val in Comics.items():
	    w.writerow([key, val])

# scrape()

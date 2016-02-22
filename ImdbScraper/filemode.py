import os,re
import requests
from bs4 import BeautifulSoup as bs
from Helper import Helper
from imdb import imdb

CURDIR=""


def search(folder):
	folders_discovered=[]
	files_discovered=[]
	for content in os.listdir(os.path.abspath(folder)):
		if os.path.isdir(os.path.abspath(content)):
			folders_discovered.append(content)
		else:
			if content.endswith('.mp4') or content.endswith('.avi') or content.endswith('.mkv'):
				files_discovered.append(content)
	return folders_discovered,files_discovered

def update(files):
	"""updates the files list with there downloadable name"""
	files_to_search=[]
	extras=[]
	#print files
	for f in files:
		m=re.match('(\D*\d?\d?\d?\D*[\d]{4}\)?\]?)',f)
		if m:
			files_to_search.append(m.group(0))
		else:
			extras.append(f)
	new_list=[]
	for f in files_to_search:
		new_list.append(f.replace('.',' '))	
	download_files(new_list)
	

def download_files(files):
	print "Starting Downloads"
	for filename in files:
		try:
			print filename
			url=Helper.prepare_search(filename,'tt')
			print url
			r=Helper.get_request(url)
			content=r.content
			soup=Helper.make_soup(content)
			title,link=imdb.get_title(soup)	
			print title," " ,link
			if title and link is not None:
				print (" saving {0}......").format(filename)
				Helper.save_page(title,link,CURDIR)
		except:
			pass	 

def main(dir_path):
        global CURDIR
	CURDIR=dir_path
        folders=set()
	files=set()
	fol,fil=[],[]
	print CURDIR
	os.chdir(CURDIR)
	for content in os.listdir(os.curdir):
		if os.path.isdir(os.path.abspath(content)):
			fol.append(content)
		else:
			if content.endswith('.mp4') or content.endswith('.avi') or content.endswith('.mkv'):
				fil.append(content)
	
	folders.update(fol)
	files.update(fil)

	for content in folders:
		fol,fil=search(content)
		folders.update(fol)
		files.update(fil)
	remove=[]
	for f in files:
		if "sample" in f.lower():
			remove.append(f)
	files.difference_update(remove) 
	update(files)
	print len(files)



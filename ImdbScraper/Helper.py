import requests
import os
from bs4 import BeautifulSoup as bs
SEARCH_QUERY='http://www.imdb.com/find?&q={0}&s={1}&ttype=ft'
DEFAULT_SEARCH="all"

class Helper:

	@staticmethod
	def get_request(url):
		'''return the request for given URL'''
		try:
			r=requests.get(url)
			return r
		except:
			print ("Error occured While reqesting the page")
	
	@staticmethod
	def make_soup(htmlcontent):
		'''Makes Soup for given html page'''
		try:
		 	soup=bs(htmlcontent,'html.parser')
		 	return soup
		except Exception, e:
		 	print ("Error",e)

	@staticmethod
	def get_movie_name_user():
		'''prompts the user to enter a movie_name'''
		try:
			s=raw_input("Enter the movie name : ")
			s='+'.join(s.split())
			return s
		except Exception,e:
			print ("Error while taking input")

	@staticmethod
	def get_search_categories():
		'''Takes the option for where to search the title'''
		options=[('All','all'),('Movie','tt'),('TV Episodes','ep'),('Names','nm')]
                count=0
                for k in options:
                                count+=1
                                print ("{0}.{1}").format(count,k[0])
                user_input=int(raw_input("Select an option that suits you the best : "))
                return options[user_input-1][1] #do vaildation


	@staticmethod
	def prepare_search(movie_name,option):
		'''formats the search string'''
		movie_name='+'.join(movie_name.strip().split())
		search=SEARCH_QUERY.format(movie_name,option)
		return search

	@staticmethod
	def save_page(title,url,curdir):
		'''saves the page'''
		try:
			path=os.path.join(curdir,"imdb")
			if not os.path.exists(path):	#checks if directory already exists
				os.makedirs(path)
			file_name=path+"/"+title.strip()+'.html'
			if not os.path.exists(file_name):
				r=requests.get(url)
				with open(file_name,'w') as f:			#save the webpage	
					f.write(r.content)
				print ("Succesfully Saved {0}").format(title)
			else:
				print ("Already exists")	
		except Exception: 
			print ("Error occured while saving title {0}").format(title)
	
        @staticmethod
	def select_title(titles):
		lis=[]
		count=0
		for key in titles:
			count+=1
			lis.append(key)
			print ("{0}.{1}").format(count,key[0:30]+"...")
		user_input=int(raw_input("Select the title which matches the most : "))
		if (0<user_input<=count):
			u=lis[user_input-1]
		else:
			print ("Not a valid value.choosing 1 as default")
			u=lis[0]
		return titles[u]
		"""except:
			print ("Error occured <select_title>")
		"""


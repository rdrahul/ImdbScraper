import os
import requests
from bs4 import BeautifulSoup as bs

class imdb:
	@staticmethod
	def soup_titles(soup):
		""" returns the search titles """
		try:
                        
			print ("Souping title")
			dict={}
			results=soup.find_all('div',attrs={'class':'findNoResults'})
			if len(results)>0:
				print( " No titles Found for {0}").format(soup.title)
				return
			titles=soup.find_all('tr',attrs={'class':'findResult'})
			if len(titles)>10:titles=titles[0:10]
			for i in titles:
				tag_a=i.find('a')
				dict[i.text]="http://imdb.com"+tag_a["href"]
			return dict
		except:
			print ("Some Error occured while souping {0}").format(soup.title)
	
	@staticmethod
	def get_title(soup):
		""" return on title of matches """
		try:
			results=soup.find_all('div',attrs={'class':'findNoResults'})
			if len(results)>0:
				print( " No titles Found for {0}").format(soup.title)
				return
			title=soup.find('tr',attrs={'class':'findResult'})
			tag_a=title.find('a')
			if tag_a:
				return title.text,"http://imdb.com"+tag_a["href"]
			else:
				return
		except:
			print ("Some Error occured while souping {0}").format(soup.title)		


	"""regular expression for matching name : (\D*\d?\d?\d?\D*[\d]{4}\)?\]?)"""
	@staticmethod
	def soup_movie_page(url):
		r=requests.get(url)
		soup=bs(r.content,"html.parser")
		info={}
		info=imdb.get_details(soup,info)
                info["name"]=imdb.get_name(soup)
		info["rating"]=imdb.get_rating(soup)
		info["credits"]=imdb.get_credits(soup)
		info["storyline"]=imdb.get_storyline(soup)
		info["genre"]=imdb.get_genre(soup)
		return info

	@staticmethod
	def get_rating(soup):
		try:
			rating=soup.find('div',attrs={'class':'ratingValue'})
			rating=rating.text.replace('\n','')
			return rating
		except:
			print ("Error while parsing rating")
	@staticmethod
	def get_name(soup):
		try:
			name=soup.find('h1',attrs={'itemprop':'name'})
			return name.text
		except Exception, e:
			print ("Error while parsing Name")
	@staticmethod
	def get_details(soup,info):
		try:
                        info["content_rating"]=soup.find('meta',attrs={'itemprop':'contentRating'}).text.replace('\n','')
                        info["running_time"]=soup.find('time',attrs={'itemprop':'duration'}).text.strip()		
                        return info
        	except Exception, e:
                        #print Exception
                        print ("Error while parsing Details")
	@staticmethod
	def get_credits(soup):
		try:
			credits=soup.find_all('div',attrs={'class':'credit_summary_item'})
			cred_str=""
			for cred in credits:
				cred_str+=cred.text.strip().replace('\n','').split('|')[0].replace(' ','').replace(':',': ').replace(',',', ')+'\n'
			return cred_str
		except Exception, e:
			print ("Error occured While Parsing Credits")

	@staticmethod
	def get_storyline(soup):
		try:
			story=soup.find('div',attrs={'itemprop':"description"})
			return story.text.strip().replace("  ","")
		except Exception, e:
			print ("Error occured While Parsing StoryLine")


	@staticmethod
	def get_genre(soup):
		try:
			genre=soup.find('div',attrs={'itemprop':"genre"})
			return genre.text.replace('\n','').split(':')[1].strip()
		except Exception, e:
			print ("Error occured While Parsing genre")

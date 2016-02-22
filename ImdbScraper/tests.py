import unittest
from imdb import imdb
import requests 
from bs4 import BeautifulSoup as bs
class TestIMDBmethods(unittest.TestCase):
	def test_soup_titles(self):
		d={}
		dummy_url="http://www.imdb.com/find?q=revenant&s=tt&ttype=ft&ref_=fn_ft"
		r=requests.get(dummy_url)
		d=imdb.soup_titles(bs(r.content,"lxml"))
		for i in d.keys():
			assert "Revenant" in i
			
	
if __name__=='__main__':
	unittest.main()
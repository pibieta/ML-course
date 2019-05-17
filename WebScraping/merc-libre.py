# -*- coding: utf-8 -*-
# imports 
import requests
from bs4 import BeautifulSoup

# specify the url
#  quote_page = ‘http://www.bloomberg.com/quote/SPX:IND'
url = 'https://articulo.mercadolibre.cl/MLC-471390138-notebook-gamer-acer-ryzen-5-16gb-ram-2tb-disco-156-_JM?quantity=1#c_id=/home/navigation/element'

# query the website and return the html to the variable ‘page’
# page = urllib.urlopen(quote_page)
page = requests.get(url)
# page
# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page.content, 'html.parser')
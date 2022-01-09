from bs4 import BeautifulSoup
from crawler import crawl
from finder import find_articles 
import os

crawl()
articles = find_articles()
print(articles)
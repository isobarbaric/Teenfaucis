# import custom functions from files (code was split up to improve readability)
from crawler import crawl
from finder import find_articles 

# executes the crawl() function from the crawler.py file to locate all trustworthy websites to find articles 
crawl()
# initializing list where all articles are stored 
articles = find_articles()
# printing all COVID-19 related articles out to the user
print(articles)
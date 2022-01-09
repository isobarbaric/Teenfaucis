from bs4 import BeautifulSoup
from crawler import crawl
import os 
crawl()
base_path = "news_channels/"
structure = os.listdir('news_channels/')
identifier = ['post', 'article', 'entry', 'news', 'heading', 'header', 'post']
covid_keywords = ['COVID', 'COVID-19', 'covid', 'pandemic', 'virus', 'Omicron', 'omicron', 'Delta', 'delta', 'variant', 'outbreak', 'wave', 'symptoms', 'testing', 'rapid test', 'pcr', 'PCR']
overall = []
for folder in structure:
    current_path = base_path + folder
    print(current_path)
    if (len(os.listdir(current_path)) == 0):
        continue
    with open(current_path + '/html_page.txt', 'r') as current_soup:
        soup = BeautifulSoup(current_soup.read(), 'lxml') 
        # element with class attribute -> grab href from anchor tag inside 
        possible = soup.find_all(attrs={'class'})
        print(possible)
        #for all_potential in possible:
        potential_articles = []
        overlap = False
        covid_related = False
        for article_title in potential_articles:
            for potential in identifier:
                if potential in article_title:
                    overlap = True
            for covid_word in covid_keywords:
                if covid_word in article_title:
                    covid_related = True
            if overlap and covid_word:
                print(article_title[0], article_title[1])
                #overall.append([article_title[0], article_title[1]]) 
print(overall)
from bs4 import BeautifulSoup
from collections import OrderedDict
import os

def find_articles():
    base_path = "news_channels/" # used as prefix for file path when creating files in the news_channels folder 
    structure = os.listdir('news_channels/') # returns a list containing all of the websites that were visited by crawler() to allow iteration
    identifier = ['post', 'article', 'entry', 'news', 'heading', 'header'] # words that appear often in the 
    # below list contains keywords that the program searches for in the heading section of all possible articles to determine whether they are about COVID-19 or not 
    covid_keywords = ['COVID', 'COVID-19', 'covid', 'pandemic', 'virus', 'Omicron', 'omicron', 'Delta', 'delta', 'variant', 'outbreak', 'wave', 'symptoms', 'testing', 'rapid test', 'pcr', 'PCR']
    # below list contains html elements where specifications are provided that can be used to determine whether certain text represents a news article's header or not 
    where_to_look = ['div', 'section', 'span']
    # below list will contain the final result, namely a list of news article names and links to those news articles
    overall = []
    for folder in structure:
        current_path = base_path + folder # specifies file path to the current file under consideration 
        with open(current_path, 'r') as current_soup: # opening the file and initializing a soup object
            soup = BeautifulSoup(current_soup.read(), 'lxml') 
            # element with class attribute -> grab href from anchor tag inside 
            potential_articles = [] # list will contain articles that are suitable to be checked further regarding their topic
            # below for loop goes through the article's html and parses through to locate all potential articles
            for i in range(3): 
                p1 = soup.find_all(where_to_look[i])
                p2 = []
                for potential in p1:
                    if (potential.has_attr('class')):
                        p2.append(potential)
                for tag in p2:
                    for anchor in tag.find_all('a'):
                        if (not anchor.has_attr('href')):
                            continue
                        potential_articles.append([tag, anchor])
            overlap = False # used to determine whether a particular html tag is referencing the news headling or not 
            covid_related = False # used to determine whether a particular html tag is related to COVID or not 
            for article_title in potential_articles: # checking whether a particular article is a COVID article or not 
                mod_title = article_title[1].text.replace('\\n', '').replace('\t', '').replace('\\r', '').replace('\\', '')
                mod_title = ' '.join(mod_title.split())
                # mod_title is the title of the article (is cleaned up a bit from its rough and unfiltered form when it is obtained)
                for potential in identifier: # this for loop determines whether this particular article title is actually refering the news headline or not 
                    if potential in article_title[0]['class']:
                        overlap = True
                for covid_word in covid_keywords: # this for loop checks to see if a particular article contains a reference to COVID or not 
                    if covid_word in mod_title:
                        covid_related = True
                if overlap and covid_related: # if an article passes both tests, then it is a valid article and it is passed to the final data structure 
                    overall.append([mod_title, article_title[1]['href']]) 
                    covid_related = False
                    overlap = False
    resultant = [] # final data structure that will contain the all COVID articles 
    # below for loop ensures that article duplication does not occur and only 
    for elem in overall: 
        if elem not in resultant:
            resultant.append(elem)
    return resultant 
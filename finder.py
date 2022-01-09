from bs4 import BeautifulSoup
import os

def find_articles():
    base_path = "news_channels/"
    structure = os.listdir('news_channels/')
    identifier = ['post', 'article', 'entry', 'news', 'heading', 'header']
    covid_keywords = ['COVID', 'COVID-19', 'covid', 'pandemic', 'virus', 'Omicron', 'omicron', 'Delta', 'delta', 'variant', 'outbreak', 'wave', 'symptoms', 'testing', 'rapid test', 'pcr', 'PCR']
    where_to_look = ['div', 'section', 'span']
    overall = []
    for folder in structure:
        current_path = base_path + folder
        # if (len(os.listdir(current_path)) == 0):
        #     continue
        with open(current_path, 'r') as current_soup:
            soup = BeautifulSoup(current_soup.read(), 'lxml') 
            # element with class attribute -> grab href from anchor tag inside 
            potential_articles = []
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
            overlap = False
            covid_related = False
            for article_title in potential_articles:
                mod_title = article_title[1].text.replace('\\n', '').replace('\t', '')
                mod_title = ' '.join(mod_title.split())
                for potential in identifier:
                    if potential in article_title[0]['class']:
                        overlap = True
                for covid_word in covid_keywords:
                    if covid_word in mod_title:
                        covid_related = True
                if overlap and covid_related:
                    overall.append([mod_title, article_title[1]['href']]) 
    return overall 
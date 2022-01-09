from bs4 import BeautifulSoup
from crawler import crawl
import os 
crawl()
base_path = "news_channels/"
structure = os.listdir('news_channels/')
identifier = ['post', 'article', 'entry', 'news', 'heading', 'header']
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
        # checking starts
        potential_articles = []
        # div's 
        p1 = soup.find_all('div')
        p2 = []
        for potential in p1:
            if (potential.has_attr('class')):
                p2.append(potential)
        for tag in p2:
            for anchor in tag.find_all('a'):
                if (not anchor.has_attr('href')):
                    continue
                # potential_articles.append([anchor.string, anchor['href']])
                potential_articles.append([tag, anchor])
        # section's
        p1 = soup.find_all('section')
        p2 = []
        for potential in p1:
            if (potential.has_attr('class')):
                p2.append(potential)
        for tag in p2:
            for anchor in tag.find_all('a'):
                if (not anchor.has_attr('href')):
                    continue
                # potential_articles.append([anchor.string, anchor['href']])
                potential_articles.append([tag, anchor])
        # span's
        p1 = soup.find_all('span')
        p2 = []
        for potential in p1:
            if (potential.has_attr('class')):
                p2.append(potential)
        for tag in p2:
            for anchor in tag.find_all('a'):
                if not anchor.has_attr('href'):
                    continue
                potential_articles.append([tag, anchor])
        # end of checking 
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
print(overall)
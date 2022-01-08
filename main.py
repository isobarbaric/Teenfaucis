from bs4 import BeautifulSoup
import requests
import os 
html_page = requests.get('https://mediabiasfactcheck.com/pro-science/')
with open('scientific_pages.txt', 'w') as storage:
    storage.write(str(html_page.content))
soup = BeautifulSoup(html_page.content, 'lxml')
suffixes = ['.com', '.org', '.edu', '.gov', '.int', '.co', '.net', '.au', '.us', '.uk', '.ne', 'news']
news_sites = soup.find_all('span', {'style': 'font-size: 12pt;'})
webpages = []
for news_channel in news_sites:
    link = news_channel.text[news_channel.text.rfind('(')+1:-1]
    if link[-4:] in suffixes:
        if (link[:8] == 'https://'):
            webpages.append(link[8:])
        else:
            webpages.append(link)
with open('link_database.txt', 'w') as storage:
    storage.write('\n'.join(webpages))
identifier = ['post', 'article', 'entry', 'news']
# want to collect all of the titles (p class) and links for headers (href)
os.mkdir('news_channels')
for website in webpages:
    with open('news_channels/' + website + '.txt', 'w') as rn:
        current_html = ''
        try:
            current_html = str(requests.get('https://' + website).content)
        except Exception:
            pass
        rn.write(current_html)
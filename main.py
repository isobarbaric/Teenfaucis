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
# want to collect all of the titles (p class) and links for headers (href)
os.mkdir('news_channels')
for website in webpages:
    os.mkdir('news_channels/' + website)
    try:
        current_html = str(requests.get('https://' + website).content)
        with open('news_channels/' + website + '/html_page.txt', 'w') as rn:
            rn.write(current_html)
        with open('news_channels/' + website + '/beautifulSoup.txt', 'w') as rn:
            soup = BeautifulSoup(current_html, 'lxml')
            rn.write(soup.text)
    except Exception:
        pass
identifier = ['post', 'article', 'entry', 'news']

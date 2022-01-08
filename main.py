from bs4 import BeautifulSoup
import requests
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
        webpages.append(link)
print('\n'.join(webpages))

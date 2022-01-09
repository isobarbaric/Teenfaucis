from bs4 import BeautifulSoup
import requests
import os 

def crawl():
    html_page = requests.get('https://mediabiasfactcheck.com/pro-science/')
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
    os.mkdir('news_channels')
    for website in webpages:
        try:
            current_html = str(requests.get('https://' + website).content)
            with open('news_channels/' + website + 'html_page.txt', 'w') as rn:
                rn.write(current_html)
        except Exception:
            pass
    print("Located all Webpages...")
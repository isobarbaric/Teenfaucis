from bs4 import BeautifulSoup
import requests
import os 

# crawl() will locate all possible trustworthy webpages and save the html for the home pages of all of these to a new directory named news_channels, where finder() in finder.py will be able to access them afterwards 
def crawl():
    html_page = requests.get('https://mediabiasfactcheck.com/pro-science/') # obtaining webpage with list of articles that are trustworthy and scientifically sound
    soup = BeautifulSoup(html_page.content, 'lxml') # creating a soup object to allow for analysis
    suffixes = ['.com', '.org', '.edu', '.gov', '.int', '.co', '.net', '.au', '.us', '.uk', '.ne', 'news'] # list of valid suffixes for all potential websites to explore using the aforementioned link
    news_sites = soup.find_all('span', {'style': 'font-size: 12pt;'}) # locating all websites mentioned on the actual webpage
    webpages = [] # data strucutre that will contain all webpages' addresses
    for news_channel in news_sites: # this for loop processes the data that is obtained from the website 
        link = news_channel.text[news_channel.text.rfind('(')+1:-1]
        if link[-4:] in suffixes:
            if (link[:8] == 'https://'):
                webpages.append(link[8:])
            else:
                webpages.append(link)
    with open('link_database.txt', 'w') as storage: # this creates a file called link_database where the URLs for all of these valid websites are saved for reference
        storage.write('\n'.join(webpages))
    os.mkdir('news_channels') # creates a new folder called news_channels to place all the html files into for explored webpages 
    for website in webpages: # goes through each website individually 
        # use of try and except when scraping each website to make sure that the program does not crash in case the website blocks the GET request
        try:
            current_html = str(requests.get('https://' + website).content) # obtains the webpage's html
            with open('news_channels/' + website + 'html_page.txt', 'w') as rn: # writes this html content to a file for future reference by find_articles() in finder.py
                rn.write(current_html)
        except Exception:
            pass
    print("Located all Webpages...") # indicates that the scraping is successful
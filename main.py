from ArticleFinder import ArticleFinder
import json
import time

article_compiler = ArticleFinder()

# get rid of brace formatting
# wean off news_channels directory
# clean up rest of code including comments here
# take rest of code to other project as ipynb and exit this repo

def write_to_storage(url: str, articles: list[str]):
    filename = url[url.find('.com') + 5:].replace('/', '_')[:-1] + '.json' 
    with open(filename, 'w') as storage:
        storage.write(json.dumps(articles, indent = 4))

science_url = 'https://mediabiasfactcheck.com/pro-science/'
conspiracy_url = 'https://mediabiasfactcheck.com/conspiracy/'

start = time.time()
# a = article_compiler.find_articles(science_url)
# write_to_storage(science_url, a)
b = article_compiler.find_articles(conspiracy_url)
write_to_storage(conspiracy_url, b)
print(time.time() - start)
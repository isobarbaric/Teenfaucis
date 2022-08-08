from ArticleFinder import ArticleFinder

# a = ArticleFinder('https://mediabiasfactcheck.com/pro-science/')

# get rid of brace formatting
# wean off news_channels directory
# clean up rest of code including comments here
# take rest of code to other project as ipynb and exit this repo

# with open('json/science.json', 'w') as f:
#     json.dumps(a.articles, indent=4)

import time

start = time.time()
b = ArticleFinder('https://mediabiasfactcheck.com/conspiracy/')
print(time.time() - start)

# with open('json/conspiracy.json', 'w') as f:
#     json.dumps(b.articles, indent=4)

# print(a.articles)
# print(b.articles)

# a = [1, 2, 3]
# print(a)
# with open('test.json', 'w', encoding='utf-8') as f:
#     f.write(json.dumps(a, indent=4))

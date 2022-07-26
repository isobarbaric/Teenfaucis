from ArticleFinder import ArticleFinder
import json

a = ArticleFinder('https://mediabiasfactcheck.com/pro-science/')

# with open('json/science.json', 'w') as f:
#     json.dumps(a.articles, indent=4)

b = ArticleFinder('https://mediabiasfactcheck.com/conspiracy/')

# with open('json/conspiracy.json', 'w') as f:
#     json.dumps(b.articles, indent=4)

# print(a.articles)
# print(b.articles)

# a = [1, 2, 3]
# print(a)
# with open('test.json', 'w', encoding='utf-8') as f:
#     f.write(json.dumps(a, indent=4))

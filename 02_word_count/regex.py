import re

WORD_RE = re.compile(r'[\w]+')

words = WORD_RE.findall('Big Data, hadoop adn map reduce. (hello world)')
print(words)
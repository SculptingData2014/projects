import re

text = open('data/ZenOfPython.txt').read()
text = text.lower()
words = re.split('\W+', text)

counts = {}
for word in words:
    n = counts.get(word, 0)
    counts[word] = n + 1

print counts

# for (word, value) in counts.items():
# 	print word, value

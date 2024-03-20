dictionary = input().split()
text = input().split()
abbreviations = {}
for word in text:
    for abbr in dictionary:
        if word.startswith(abbr):
            if word not in abbreviations or len(abbr) < len(abbreviations[word]):
                abbreviations[word] = abbr


result = [abbreviations.get(word, word) for word in text]
print(' '.join(result))

'''dictionary = set(input().split())
text = input().split()
abbreviations = {word: min((abbr for abbr in dictionary if word.startswith(abbr)), default=word) for word in text}
result = [abbreviations[word] for word in text]
print(' '.join(result))'''

'''import re

dictionary = input().split()
text = input()
pattern = re.compile(r'\b(?:' + '|'.join(dictionary) + r')\w*')
result = pattern.sub(lambda x: min(x.group(), key=len), text)
print(result)'''
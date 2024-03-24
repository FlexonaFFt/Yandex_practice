'''dictionary = input().split()
text = input().split()
abbreviations = {}
for word in text:
    for abbr in dictionary:
        if word.startswith(abbr):
            if word not in abbreviations or len(abbr) < len(abbreviations[word]):
                abbreviations[word] = abbr


result = [abbreviations.get(word, word) for word in text]
print(' '.join(result))'''

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

def replace_words():
    words_to_replace = input().strip().split(' ')
    initial_text = input().strip()
    words_in_text = initial_text.split(' ')
    words_to_replace_excluded = []

    for word_to_replace in words_to_replace:
        another_word_to_replace = next((w for w in words_to_replace if w != word_to_replace and word_to_replace.startswith(w) and len(w) < len(word_to_replace)), None)
        if another_word_to_replace:
            words_to_replace_excluded.append(word_to_replace)
    words_to_replace = [word for word in words_to_replace if word not in words_to_replace_excluded]

    words_to_replace_map = {}
    for word in words_to_replace:
        if word[0] not in words_to_replace_map:
            words_to_replace_map[word[0]] = []
        words_to_replace_map[word[0]].append(word)

    for index, word_in_text in enumerate(words_in_text):
        words_to_replace_options = words_to_replace_map.get(word_in_text[0], [])
        for word_to_replace in words_to_replace_options:
            if word_in_text.startswith(word_to_replace):
                words_in_text[index] = word_to_replace

    final_text = ' '.join(words_in_text)
    print(final_text)

replace_words()
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
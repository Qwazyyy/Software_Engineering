from collections import Counter
import re


def count_words_and_find_most_frequent(file_path):
    with open(file_path, 'r') as file:
        text = file.read().lower()
        words = re.findall(r'\b\w+\b', text)
        word_count = len(words)
        most_common_word, frequency = Counter(words).most_common(1)[0]

        return word_count, most_common_word, frequency


file_path = 'habr.txt'
word_count, most_common_word, frequency = count_words_and_find_most_frequent(file_path)
print(f'Всего слов: {word_count}')
print(f'Самое часто встречающееся слово: "{most_common_word}" попадается {frequency} раз')

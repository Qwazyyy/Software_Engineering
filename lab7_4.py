def load_banned_words(file_path):
    with open(file_path, 'r') as file:
        return file.read().split()

def replace_banned_words(sentence, banned_words):
    replaced_sentence = sentence
    for banned_word in banned_words:
        replaced_sentence = replaced_sentence.replace(banned_word.lower(), '*' * len(banned_word))
        replaced_sentence = replaced_sentence.replace(banned_word.capitalize(), '*' * len(banned_word))
        replaced_sentence = replaced_sentence.replace(banned_word.upper(), '*' * len(banned_word))
    return replaced_sentence

def main():
    banned_words = load_banned_words('banned_words.txt')
    sentence = "Hello, world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!!"
    replaced_sentence = replace_banned_words(sentence, banned_words)
    print(replaced_sentence)

if __name__ == "__main__":
    main()

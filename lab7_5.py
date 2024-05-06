def count_words(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        words = content.split()
        return len(words)


def main():
    file_path = input("Введите путь к текстовому файлу: ")
    word_count = count_words(file_path)
    if word_count != -1:
        print(f"Количество слов в файле '{file_path}': {word_count}")


if __name__ == "__main__":
    main()

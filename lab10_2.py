# Создание пустого файла
with open("empty.txt", "w") as empty_file:
    pass

# Создание файла с информацией
with open("text.txt", "w") as file_with_info:
    file_with_info.write("Какой то текст")


# Проверка содержимого файлов
def check_file_content(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            if not content:
                raise Exception("Файл пустой")
            else:
                print(content)
    except Exception as e:
        print(e)


# Проверка пустого файла
check_file_content("empty.txt")

# Проверка файла с информацией
check_file_content("text.txt")

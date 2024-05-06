def analyze_text(filename):
    letter_count = 0
    word_count = 0
    line_count = 0

    with open(filename, 'r') as file:
        for line in file:
            line_count += 1
            word_count += len(line.split())
            letter_count += sum(1 for char in line if char.isalpha())

    result = f"Input file contains:\n{letter_count} letters\n{word_count} words\n{line_count} lines"
    print(result)


if __name__ == "__main__":
    analyze_text('input.txt')
def most_frequent_digits(input_string):
    digit_count = {}

    for char in input_string:
        digit = int(char)
        if digit in digit_count:
            digit_count[digit] += 1
        else:
            digit_count[digit] = 1

    top_three_digits = sorted(digit_count.items(), key=lambda item: (-item[1], item[0]))[:3]

    result = {key: value for key, value in sorted(top_three_digits)}

    return result


input_string = input("Введите число: ")
output = most_frequent_digits(input_string)
print(output)
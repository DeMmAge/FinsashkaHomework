simple_numbers = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5, 'шесть': 6,
                  'семь': 7, 'восемь': 8, 'девять': 9, 'десять': 10, 'одиннадцать': 11,
                  'двенадцать': 12, 'тринадцать': 13, 'четырнадцать': 14, 'пятнадцать': 15, 'шестнадцать': 16,
                  'семнадцать': 17, 'восемнадцать': 18, 'девятнадцать': 19}

composite = {'двадцать': 20, 'тридцать': 30, 'сорок': 40, 'пятдесят': 50,
             'шестьдесят': 60, 'семьдесят': 70, 'восемьдесят': 80, 'девяносто': 90}

operations = {'плюс': '+', 'минус': '-', 'умножить': '*', 'разделить': '/'}


def parse_number(text):
    for j in range(len(text)):
        word = text[j]
        if word in simple_numbers:
            return int(simple_numbers[word])
        elif text[j] in composite:
            return int(composite[word]) + int(simple_numbers[text[j + 1]])


raw_text = input()
words = raw_text.split(' ')

operation = str()
first_number = str()
second_number = str()

for i in range(len(words)):
    if words[i] in operations:
        operation = words[i]
        first_number = words[: i]
        print(first_number)
        second_number = words[i + 1:]
        print(second_number)
        break

parsed_first = parse_number(first_number)
parsed_second = parse_number(second_number)

sign = operations[operation]
if sign == '+':
    print(parsed_first + parsed_second)
elif sign == '-':
    print(parsed_first - parsed_second)
elif sign == '*':
    print(parsed_first * parsed_second)
elif sign == '/':
    print(parsed_first / parsed_second)

print(str.format('{0} {1} {2}', first_number, operation, second_number))

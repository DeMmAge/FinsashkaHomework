import random
import sys

field = [[0 for i in range(4)] for j in range(4)]
win = False
free_x = -1
free_y = -1
instruction = 'Select coordinates between 0 to 3'
field_output_template = '''
    | X0 | X1 | X2 | X3 
+-----------------------+
Y0  | {:3}| {:3}| {:3}| {:3}
+-----------------------+
Y1  | {:3}| {:3}| {:3}| {:3}
+-----------------------+
Y2  | {:3}| {:3}| {:3}| {:3}
+-----------------------+
Y3  | {:3}| {:3}| {:3}| {:3}
'''


def fill_field():
    global free_x
    global free_y
    numbers = list()
    for i in range(1, 16):
        numbers.append(i)

    for x in range(4):
        for y in range(4):
            # If only one left in numbers
            if len(numbers) - 1 == 0:
                field[x][y] = numbers[0]
                break
            index = random.randint(0, len(numbers) - 1)
            number = numbers[index]
            numbers.remove(number)
            field[x][y] = number

    # Set random empty cell
    rand_x = random.randint(0, 3)
    rand_y = random.randint(0, 3)
    tmp = field[rand_x][rand_y]
    field[rand_x][rand_y] = 0
    free_x = rand_x
    free_y = rand_y
    field[3][3] = tmp


def print_field():
    # clear()
    out = list()
    # rewrite
    for i in range(4):
        for j in range(4):
            if field[i][j] != 0:
                out.append(str(field[i][j]))
            else:
                out.append(' ')

    print(str.format(field_output_template, *out))


def check_winning_positions():
    previous = 0
    for x in range(4):
        for y in range(4):
            current = field[x][y]
            if current == previous + 1:
                previous = current
            else:
                return False
            if x == 3 and y == 2:
                return True
    return True


def validate_coordinates(x, y):
    return (3 >= x >= 0) and (3 >= y >= 0)


def near_free_cell(x, y):
    return (x + 1 == free_x and y == free_y) \
           or (x == free_x and y == free_y + 1) \
           or (x - 1 == free_x and y == free_y) \
           or (x == free_x and y - 1 == free_y)


# Main loop
fill_field()
moves = 0
while not win:
    try:
        print_field()
        print('Select row\nX:')
        getY = int(input())
        if getY == -1:
            sys.exit(0)
        print('Y:')
        getX = int(input())
        if not validate_coordinates(getX, getY):
            print(instruction)
            continue

        if getX == free_x and getY == free_y:
            print('You cant select empty cell')
            continue

        print('Selected ' + str(field[getX][getY]) + '\nMove to\nX:')

        setY = int(input())
        print('Y:')
        setX = int(input())
        if not validate_coordinates(setX, setY):
            print(instruction)
            continue

        if near_free_cell(getX, getY):
            field[setX][setY] = field[getX][getY]
            field[getX][getY] = 0
            free_x = getX
            free_y = getY
            moves += 1
        else:
            print('Сells should be near')
            continue

    except ValueError:
        print(instruction)
        continue

win = check_winning_positions()
if win:
    print(str.format('You win in {0} moves!', moves))
    sys.exit(0)

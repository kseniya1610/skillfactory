def greet():
    print('Приветствуем в игре "Крестики-Нолики"')
    print(' формат ввода: x y ')
    print(' x - номер строки  ')
    print(' y - номер столбца ')
field = [[''] * 3 for i in range(3)]
def show():
    print(f' 0 1 2')
    for i in range(3):
        row = ' '.join(field[i])
        print(f'{i} {row}')
def ask():
    while True:
        field = input('Ваш ход: ').split()
        if len(field) != 2:
            print('Введите две координаты')

        x, y = field

        if not (x.isdigit()) or not (y.isdigit()):
            print(' Введите числа! ')
            continue

        x, y = map(int, input('Ваш ход:').split())
        if 0 <= x <= 2 and 0 <= y <= 2 :
            if field[x][y] == ' ':
                return x, y
            else:
                print('Клетка занята')
        else:
            print('координаты за пределами поля')
            continue

        if field[x][y] != " ":
            print(' Клетка занята! ')
            continue

        return x, y
def check_victory():
    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[i][j])
        if symbols == ['X', 'X', 'X']:
            return True
    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[j][i])
        if symbols == ['X', 'X', 'X']:
            return True
    symbols = []
    for i in range(3):
        symbols.append(field[i][i])
        if symbols == ['X', 'X', 'X']:
            return True
    symbols = []
    for i in range(3):
        symbols.append(field[i][2-i])
        if symbols == ['X', 'X', 'X']:
            return True

    return False


greet()
field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print(' Ходит крестик!')
    else:
        print(' Ходит нолик!')

    x, y = ask()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_victory():
        break

    if count == 9:
        print(" Ничья!")
        break
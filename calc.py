"""
    Необходимо написать простой калькулятор,
    который оперирует с двумя числами и оператором.

    В зависимости от введенного оператора,
    между числами проводится определенная операция.

    Результат выводится на экран.

    * обработать все возможные ошибки программы с помощью try-except
"""
while True:
    a = None
    b = None
    action = None
    res = None

    try:
        a = float(input('a: '))
        action = input('action: ')
        b = float(input('b: '))
    except ValueError:
        print('Not valid value')

    if action and action in '/*+-':
        if action == '/':
            if b != 0:
                res = a / b
            else:
                print('Division by zero is not possible!')

        elif action == '*':
            res = a * b

        elif action == '-':
            res = a - b

        elif action == '+':
            res = a + b

    else:
        print('Non-existent operator!')

    print('result:', res, '\n__________________')

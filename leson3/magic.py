"""
   Магическое число.
   Необходимо угадать загаданное число за наименьшее количество попыток.

   Алгоритм:

   2. Пользователь вводит число.
   3. Если введенное число больше или меньше сгенерированного, то
       выводится соответствующее сообщение и возвращаемся к пункту 2.
   4. Иначе введенное число равняется сгенерированному -
       пользователь угадал число. Выводится само число и количество попыток.
       А так же вопрос "Continue? (Y/n) ".
   6. Если пользователь выбирает продолжить -
       обнуляем счетчик попыток и переходим к пункту 1.
   7. Иначе выводим сообщение 'Bye!'.

   * Для генерации случайного числа используем random.randint(-inf, +inf),
       где -inf - +inf - диапазон возможных чисел

   ** по желанию, можете хранить рекордное число попыток
   и сообщать пользователю, если он поставил новый рекорд
"""

import random

min_count = 0
while True:
    count  = 0
    rand = random.randint(0, 1000)
    while True:
        count += 1
        try:
            num = int(input('введите число от 0 до 1000 : '))
        except ValueError:
            continue
        if num < rand:
            print('Ваше значение меньше')
        elif num > rand:
            print('Ваше значение больше')
        else:
            print('Верно!', rand)
            print('Количество попыток:', count)

            break

    if min_count == 0:
        min_count = count
    if min_count > count:
        min_count = count
        print('You set a new record')
    y_n = input('Continue(Y/n)?')
    if y_n == 'n':
        print('Bye')
        break

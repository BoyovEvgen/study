"""
    Генератор паролей.
    Пользователь выбирает 1 из 3 вариантов:
    1. Сгенерировать простой пароль (только буквы в нижнем регистре, 8 символов)
    2. Сгенерировать средний пароль (любые буквы и цифры, 8 символов)
    3. Сгенерировать сложный пароль (минимум 1 большая буква, 1 маленькая, 1 цифра и 1 спец-символ, длина от 8 до 16 
    символов)
        (для 3 пункта можно генерировать пароли до тех пор, пока не выполнится условие)

    Для решения использовать:
    - константы строк из модуля string (ascii_letters, digits и т.д.)
    - функцию choice из модуля random (для выборки случайного элемента из последовательности)
    - функцию randint из модуля random (для генерации случайной длины сложного пароля от 8 до 16 символов)


    Дополнительно:
    1. Позволить пользователю выбирать длину пароля, но предупреждать, что
        пароль ненадежный, если длина меньше 8 символов
    2. Добавить еще вариант генерации пароля - 4. Пользовательский пароль:
        - пользователь вводил пул символов, из которых будет генерироваться пароль
        - вводит длину желаемого пароля
        - программа генерирует пароль из нужной длины из введенных символов
        - * игнорируются пробелы
"""

import string
import random


def generate_password_low():
    return ''.join(random.sample(string.ascii_lowercase, 8))


def generate_password_letter_and_dig():
    return ''.join(random.sample(string.digits + string.ascii_letters, 8))


def generate_password_strong():
    char_set = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.sample(char_set, random.randint(8, 16)))

    if check_password(password):
        return password
    else:
        return generate_password_strong()


def check_password(password):
    flag_dig = flag_upp = flag_low = flag_punctuation = False

    for char in password:
        if char in string.digits:
            flag_dig = True
        if char in string.ascii_uppercase:
            flag_upp = True
        if char in string.ascii_lowercase:
            flag_low = True
        if char in string.punctuation:
            flag_punctuation = True
    if flag_dig and flag_upp and flag_low and flag_punctuation:
        return True
    return False


def generate_password_user():
    try:
        char_set = input('Введите символы из которых генерировать пароль: ').replace(' ', '')
        len_password = int(input('Введите длину пароля'))
        if len_password < 8:
            print('Пароль короче 8 символов! - Ненадежный!')

        password = ''.join(random.sample(char_set, len_password))
        return password
    except ValueError:
        print('Не валидное значение длины.')
        return generate_password_user()


def choice_typ_password():
    return input(
    '1. Сгенерировать простой пароль (только буквы в нижнем регистре, 8 символов)\n'
    '2. Сгенерировать средний пароль (любые буквы и цифры, 8 символов)\n'
    '3. Сгенерировать сложный пароль (минимум 1 большая буква, 1 маленькая, 1 цифра и 1 спец-символ, длина от 8 до 16 '
    'символов)\n'
    '4. Пользовательский пароль.\n'
    'Выберите 1 из 4 вариантов: )'
    )


def main():

    match choice_typ_password():
        case '1':
            print(f'Strong pwd: {generate_password_low()}')
        case '2':
            print(f'Strong pwd: {generate_password_letter_and_dig()}')
        case '3':
            print(f'Strong pwd: {generate_password_strong()}')
        case '4':
            print(f'Strong pwd: {generate_password_user()}')
        case _:
            print('Не существующий вариант')


if __name__ == "__main__":
    main()

"""
    Необходимо реализовать форму регистрации пользователей.
    Поля формы: номер телефона, email, пароль и подтверждение пароля.

    пункты с ** - дополнительно, но не обязательно (не влияет на оценку)

    1. Пользователь вводит номер телефона.
        Программа проверяет валидность телефона:
        - приводит номер к формату 380501234567
        - если номер не получается привести к нужному формату
            то запрашивает ввод номера еще раз
            и так до тех пор, пока не будет введен валидный номер

    2. Пользователь вводит email.
        Программа проверяет валидность email:
        - должен иметь длину 6 символов и больше
            (функция len())
        - содержать один символ '@'
            (строчный метод count())
        - ** содержать логин и полный домен (логин@полный.домен)
        Пользователь может вводить email до тех пор, пока он не будет валидным.

    3. Пользователь ввод пароль.
        Программа проверяет надежность пароля:
        - минимум 8 символов
            (функция len())
        - пароль не должен содержать пробельные символы
            (строчный метод isspace())
        - наличие минимум 1 буквы в верхнем регистре, 1 в нижнем и 1 цифры
            (строчные методы isupper(), islower(), isdigit())
        - ** наличие минимум 1 спец символа

    4. После успешного ввода пароля пользователь вводит подтверждение пароля.
        Если подтверждение пароля не сходится с введенным паролем,
        то возвращаемся к пункту 3.

    Программа выводит сообщение:

    Поздравляем с успешной регистрацией!
    Ваш номер телефона: 380501234567
    Ваш email: example@mail.com
    Ваш пароль: ********** (кол-во  == кол-ву символов пароля)

"""


def set_phone():
    """
    Функция запрашивает у пользователя номер телефона до тех пор пока
    пользователь не введет валидный номер.
    Проверяет его, приводит к единому формату (380123456789) и возвращает его.
    :return: str
    """

    phone= input('Введите номер телефона: ')
    if (phone_num := phone_format(phone))[0]:
        return phone_num[1]
    else:
        return set_phone()


def phone_format(phone_str):
    phone_num = ''
    for char in phone_str:
        if char.isdigit():
            phone_num += char
    if len(phone_num) >= 9:
        return True, '380' + phone_num[-9::]
    else:
        print('НЕ ВЕРНЫЙ ФОРМАТ')
        return False, f'{phone_str} НЕ ВЕРНЫЙ ФОРМАТ ТЕЛЕФОНА'


def set_email():
    """
    Пользователь вводит email.
    Программа проверяет валидность email:
    - должен иметь длину 6 символов и больше
        (функция len())
    - содержать один символ '@'
        (строчный метод count())
    - ** содержать логин и полный домен (логин@полный.домен)
    Пользователь может вводить email до тех пор, пока он не будет валидным.
    :return: str
    """
    email_ = input("Введите Ваш email: ")
    if check_email(email_):
        return email_
    return set_email()


def check_email(email_):
    """
    пояснение второй проверки: последние 4 символа это минимум "@_._",
    из чего следует, логин должен быть минимум 2 символа, тогда общая длина выйдет min 6 символов.
    проверяем длину среза от 0 до индекса "@", должнпа быть не менее 2
    третья проверка: берем срез начиная с "@" - доконца, считаем в нем колл-во ".". не должно быть нулем.
    после '@' должно быть минимум 3 символа
    из устных разъямнений задачи...

    :param email_:
    :return: bool
    """

    if email_.count('@') != 1 \
            or len(email_[:email_.index('@')]) < 2 \
            or email_[email_.index('@'):].count('.') == 0\
            or len(email_[email_.index('@'):]) < 4:
        print('Введен не валидный email')
        return False
    return True


def set_password():
    """
    3. Пользователь ввод пароль.
    Программа проверяет надежность пароля:
    - минимум 8 символов
        (функция len())
    - пароль не должен содержать пробельные символы
        (строчный метод isspace())
    - наличие минимум 1 буквы в верхнем регистре, 1 в нижнем и 1 цифры
        (строчные методы isupper(), islower(), isdigit())
    - ** наличие минимум 1 спец символа

    4. После успешного ввода пароля пользователь вводит подтверждение пароля.
    Если подтверждение пароля не сходится с введенным паролем,
    то возвращаемся к пункту 3.
    :return: str
    """

    password = input("Пароль не должен содержать пробелы.\n"
                     "Должны быть минимум по одному символу в верхнем и нижнем регистре.\n"
                     "Должны быть минимум одна цифра.\n"
                     "Введите пароль: ")
    if check_password(password)[0]:
        return password
    else:
        return set_password()


def check_password(pwd):
    flag_apper = flag_lower = flag_digit = flag_space = 0

    for char in pwd:
        if char.isupper():
            flag_apper = 1
        if char.islower():
            flag_lower = 1
        if char.isdigit():
            flag_digit = 1
        if char.isspace():
            flag_space = 1

    if len(pwd) < 8:
        print('КОРОТКИЙ ПАРОЛЬ')
        return False, 'КОРОТКИЙ ПАРОЛЬ'  #возвращает список. второй єлемент будет использоваться в Lesson6(импортирую модуль)
    elif not flag_apper or not flag_lower or not flag_digit:
        print('НЕНАДЕЖНЫЙ ПАРОЛЬ')
        return False, ' НЕНАДЕЖНЫЙ ПАРОЛЬ'
    elif flag_space:
        print('НЕ ДОЛЖЕН СОДЕРЖАТЬ ПРОБЕЛОВ')
        return False, ' НЕ ДОЛЖЕН СОДЕРЖАТЬ ПРОБЕЛОВ'
    else:
        password_reply = input('Повторите пароль: ')
        if password_reply == pwd:
            return True, ' ПАРОЛЬ ПРИНЯТ'
        else:
            print('ПАРОЛИ НЕ СОВПОДАЮТ')
            return False, ' ПАРОЛИ НЕ СОВПОДАЮТ'


def main():
    phone = set_phone()
    email_ = set_email()
    password = set_password()
    print("Поздравляем с успешной регистрацией!\n"
          f"Ваш номер телефона: {phone}\n"
          f"Ваш email: {email_}\n"
          f"Ваш пароль: {'*' * len(password)}")


if __name__ == '__main__':
    main()

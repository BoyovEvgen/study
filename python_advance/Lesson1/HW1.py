import datetime
import re


def print_execution_time(f):
    """
    Декоратор который выводит время работы функции
    """
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        res = f(*args, **kwargs)
        execution_time = datetime.datetime.now() - start_time
        print(execution_time)
        return res
    return wrapper


@print_execution_time
def fibanachi(n):
    """
    Функция считает число Фибаначи n-ого елемента.
    """
    first_num = 1
    second_num = 1
    for _ in range(n):
        first_num, second_num = second_num, first_num + second_num
    return second_num


# fibanachi = print_execution_time(fibanachi)


def summ_max_num(*args):
    """
    Функция принимает кортеж елементов типа Int и возвращает сумму двух наибольших элементов.
    """
    print(type(args))
    lst_num = sorted(args, reverse=True)
    return lst_num[0] + lst_num[1]


def sum_input_digit():
    flag = True
    print('Вводите цифры для их сумирования.\nДля выхода введите "*"')
    res = 0
    while flag:
        input_str = input()
        if '*' in input_str:
            flag = False
        list_didit = re.findall(r'\d+', input_str)
        res += sum(map(int, list_didit))
        print(res)


def main():
    # print(fibanachi(5))
    print(summ_max_num(5, 10, 20, 3, 2))
    # sum_input_digit()


if __name__ == '__main__':
    main()
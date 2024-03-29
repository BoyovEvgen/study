"""
    Написать функцию, которая будет проверять счастливый билетик или нет.

    Билет счастливый, если сумма одной половины цифр равняется сумме второй.
"""

# Ниже описаны некоторые варианты решения задачи.


def is_lucky(ticket_num):
    num = []
    for char in str(ticket_num):
        num.append(int(char))
    if len(num) % 2 != 0:
        return False
    center = len(num) // 2
    return sum(num[:center]) == sum(num[center:])
#    lt = len(ticket_num)
#    a = b = 0
#    for i in range(lt):
#        print(i)
#        if i < lt // 2:
#            a += ticket_num[i]
#        else:
#            b += ticket_num[i]
#    return a == b


assert is_lucky(1230) is True
assert is_lucky(239017) is False
assert is_lucky(134008) is True
assert is_lucky(15) is False
assert is_lucky(2020) is True
assert is_lucky(199999) is False
assert is_lucky(77) is True
assert is_lucky(479974) is True
assert is_lucky(4700731) is False


print("All tests passed successfully!")

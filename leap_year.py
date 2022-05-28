"""
    Вводится год.
    Программа выводит количество дней в году, учитывая високосный год.

    * високосный год кратный 4, но не кратный 100 или кратный 400
"""

while True:
    try:
        year = int(input('Enter year: '))
        if (year % 4 == 0 and year % 100 > 0) or (year % 100 == 0 and year % 400 == 0):  # то високосный
            print('366 days in year')
        else:
            print('365 days in year')
    except:
        print("Not valid year")



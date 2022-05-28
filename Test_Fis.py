### N1
##a = input('Enter value 1:')
##b = input('Enter value 2:')
##c = input('Enter value 3:')
##print('{}\n{}\n{}'.format(c, b, a))
###==============================================================================


###N2
##def Prog_for_Fis(val):
##    lst = [int(x) for x in val.split()]
##    print((lst[0]+lst[1])/(lst[2]+lst[3]))
##
##
##Prog_for_Fis(input("Введите 4 числа через пробел: "))     
###===============================================================================



###N3
##name = input('Enter name: ')
##age = input('Enter age: ')
##city = input('Enter city: ')
##print('{} from {}\nHe is {}'.format(name, city, age))
###================================================================================



###N4
class Rectangle:
    def __init__ (self, a, b):
        if a > 0:
            self.__a = a
        else: self.__a = 1
        if b > 0:
            self.__b = b
        else: self.__b = 1
    @property
    def perimeter(self):
            return (self.__a + self.__b)*2
    @property
    def square(self):
            return self.__a * self.__b

    @property
    def a(self):
        return self.__a
    @property
    def b(self):
        return self.__b

    @a.setter
    def a (self, value):
        if value > 0 and type(value)==int:
            self.__a = value
    @b.setter
    def b (self, value):
        if value > 0 and type(value)==int:
            self.__b = value

rect = Rectangle(10, 5)
print('Значения первого обЪекта:')
print('Периметр - ', rect.perimeter)
print('Площадь', rect.square)
print('============================\n\n')

rect1 = Rectangle(1, 1)
print("ОБЪЕКТ № 2\n============================")
while True:
    rect1.a = int(input("Введите строну прямоугольника: "))
    rect1.b = int(input("Введите вторую сторону прямоугольнтка: "))
    print('Периметр = ', rect1.perimeter)
    print('Площадь = ', rect1.square)
    print('**************************************\n')
#=====================================================================================



###N5
##class  Triangle:
##    @staticmethod
##    def square(katet1, katet2):
##        return katet1 * katet2 /2
##    @staticmethod
##    def perimeter(katet1, katet2):
##        gepatenusa = (katet1**2+katet2**2)**0.5
##        return gepatenusa + katet1 + katet2
##
##while True:
##    a = int(input("Введите первый катет треугольника, для выода введите '0': "))
##    b = int(input("Введите второй катет треугольника, для выода введите '0': "))
##    if a == 0 or b == 0:
##        break
##    else:
##        print('Площадь треугольника: ', Triangle.square(5, 10))
##        print('Периметр треугольника', Triangle.perimeter(10,35))
##        print('**************************************\n')
##    







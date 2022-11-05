from collections import deque

def sum(arr):
    if len(arr) > 0:
        return arr.pop() + sum(arr)
    else:
        return 0


def len_list(arr):
    try:
        arr.pop()
        return 1 + len_list(arr)
    except IndexError:
        return 0


def max_digit(arr:list):
    max_num = arr[0]
    for i in arr:
        if i > max_num:
            max_num = i
    return max_num


# print(max_digit([1, 2, 3, 10, 4, 5, 6, -5]))
##########################################


class Person:

    def __init__(self, name, profession):
        self.name = name
        self.profession = profession
        self.friand_lst = []

    def __repr__(self):
        return f'{self.name} - {self.profession}'


Evgen = Person('Evgen', 'developer')
Max = Person('Max', 'sailor')
Alex = Person('Alex', 'engineer')
Tom = Person('Tom', 'driver')
Sofia = Person('Sofia', 'killer')
Fis = Person('Fis', 'teacher')
Evgen.friand_lst.extend([Max, Alex])
Max.friand_lst.extend([Alex, Evgen, Tom])
Alex.friand_lst.extend([Evgen, Fis, Max])
Sofia.friand_lst.extend([Fis])
Fis.friand_lst.extend([Sofia, Alex])


def search_profession(person, worker):
    search_queue = deque()
    search_queue.append(person)
    search_queue.extend(person.friand_lst)
    searched = []
    print(search_queue)

    while search_queue:
        friend: Person = search_queue.popleft()
        if friend not in searched:
            searched.append(friend)
            if friend.profession == worker:
                print(f'{worker} is {friend.name}')
                return friend
            else:
                search_queue.extend(friend.friand_lst)
                print(search_queue)


print(search_profession(Evgen, 'killer'))
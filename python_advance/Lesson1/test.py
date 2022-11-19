def all_combinations(a):
    if len(a) <= 1:
        yield a
    else:
        head = ''
        tail = list(a)
        while len(tail) > 0:
            head += tail.pop(0)
            for s in all_combinations(tail):
                yield [head] + s


# a = all_combinations(tuple(map(str, range(1, 10))))

for a in all_combinations(tuple(map(str, range(1, 10)))):
    print(a)

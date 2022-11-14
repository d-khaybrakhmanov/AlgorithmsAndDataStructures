def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])


print(count([2, 4, 6]))

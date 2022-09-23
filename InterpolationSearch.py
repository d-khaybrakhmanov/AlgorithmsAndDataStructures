def interpolation_search(lst, search_item):
    low = 0
    high = len(lst) - 1
    search_result = False

    while (low <= high and search_item >= lst[low]) and search_item <= lst[
        high] and not search_result:
        middle = low + int(((high - low)/(lst[high] - lst[low])) * (
            search_item - lst[low]))
        guess = lst[middle]
        if guess == search_item:
            search_result = True
        if guess < search_item:
            low = middle + 1
        else:
            high = middle - 1
    return search_result

lst = [3, 5, 11, 12, 15, 23, 25, 34, 67, 86]
value = 67
result = interpolation_search(lst, value)

if result:
    print('Элемент найден!')
else:
    print('Элемент не найден!')
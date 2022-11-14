def quicksort(array):
    if len(array) < 2:
        return array
    else:
        # рекурсивный случай
        pivot = array[0]
        # Подмассив всех элементов, меньше опорного
        less = [i for i in array[1:] if i < pivot]
        # Подмассив всех элементов, больше опорного
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([1, 5, 2, 8, 23, 65, 33]))

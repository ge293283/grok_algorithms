# Chapter 4. Quick Sort

def sum_arr(arr):
    total = 0
    for x in arr:
        total += x
    return total


print(sum_arr([1, 2, 3]))


def sum_arr_recursion(arr, index=0):
    if len(arr) == index:  # базовый случай
        return 0
    else:
        element = arr[index]
        sum_elements = element + sum_arr_recursion(arr, index + 1)  # рекурсия
        return sum_elements


print(sum_arr_recursion([1, 2, 3]))


def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])


print(count([1, 2, 3, 4, 5]))


def max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    else:
        sub_max = max(list[1:])
        return list[0] if list[0] > sub_max else sub_max


print(max([14, 32, 3, 99, 5, 551, 0]))


# Быстрая сортировка
def quicksort(array):
    if len(array) < 2:  # базовый случай
        return array
    else:
        pivot = array[0]  # рекурсивынй случай
        less = [i for i in array[1:] if i <= pivot]  # подмассив всех элементов меньше опорного
        greater = [i for i in array[1:] if i > pivot]  # подмассив всех элементов больше опорного
        return quicksort(less) + [pivot] + quicksort(greater)


# def quicksort(array):
#     if len(array) < 2:  # базовый случай
#         return array
#     else:
#         pivot = array[-1]  # рекурсивынй случай
#         less = [i for i in array[:-1] if i <= pivot]  # подмассив всех элементов меньше опорного
#         greater = [i for i in array[:-1] if i > pivot]  # подмассив всех элементов больше опорного
#         return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10, 3, 54, 3, 111, 34, 84, 19, 5]))

# Сортировка слиянием и быстрая сортировка
def print_items(list):
    for item in list:
        print(item)

from time import sleep
def print_items2(list):
    for ittem in list:
        sleep(1)
        print(item)

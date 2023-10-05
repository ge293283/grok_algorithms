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

# Chapter 2. Selection sort

def find_samllest(arr):
    """
    Функция для поиска наименьшего элемента массива

    :param arr: массив
    :return: индекс наименьшего элемента
    """
    smallest = arr[0]    # для хранения наименьшего значения
    smallest_index = 0    # для хранения инлекса наименьшего значения

    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    """
    Функция сортировки выбором

    :param arr: массив
    :return: отсортированный массив
    """
    sort_arr = []

    for i in range(len(arr)):
        smallest = find_samllest(arr)   # находит наименьшей элемент в массиве
        sort_arr.append(arr.pop(smallest))    # добавляет в новый массив
    return sort_arr

print(selection_sort([6, 77, 1, 0, 332, 9, 8, 6, 55]))
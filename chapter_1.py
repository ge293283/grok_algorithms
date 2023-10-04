# Chapter 1: Introduction to Algorithms

# Бинарынй посик. log2(n) шагов. O(log n)
def binary_search(list, item):
    list.sort()  # работает только с отсортрованным списком
    low = 0  # граница списка
    high = len(list) - 1  # граница списка

    while low <= high:  # пока эта часть не сокр. до 1 элемента
        mid = (low + high) // 2  # проверяем средний элемент
        guess = list[mid]

        if guess == item:  # значение найдено
            return mid
        elif guess > item:  # много
            high = mid - 1
        else:  # мало
            low = mid + 1
    return None


list_test = [1, 7, 2, 3, 65, 33, 100, 5, 0]

print(binary_search(list_test, 3))
print(binary_search(list_test, 999))

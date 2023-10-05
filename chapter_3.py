# Chapter 3. Recursion

# # Бесконечный цикл!
# def count_down(i):
#     """
#     Функция выполняется бесконечно!
#     :param i:
#     :return:
#     """
#     print(i)
#     count_down(i - 1)
#

# count_down(5)

"""
Каждая рекурсивная функция состоит из двух частей:
базового случая и рекурсивного случая.
"""


def count_down(i):
    """
    Функция выполняется бесконечно!
    :param i:
    :return:
    """
    print(i)
    if i <= 0:  # базовый случай; i < 0:, print: -1 0 1 2 ...
        return
    else:  # рекурсивный случай
        count_down(i - 1)


count_down(5)


def greet(name):
    print(f"hello, {name}!")
    greet2(name)
    print("getting ready to say bye...")
    bye()


def greet2(name):
    print(f"how are you, {name}?")


def bye():
    print("ok bye")


greet("Maggie")

"""
Когда вы вызываете функцию из другой функции, вызывающая функция
приостанавливается в частичоо завершеноом состоянии.
"""


def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)


print(fact(3))

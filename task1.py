"""Задача 26:  Посчитать факториал (произведение 1 до N) и треугольное число (сумма чисел от 1 до N) 
для числа N ЧЕРЕЗ РЕКУРСИЮ и без циклов"""


"""n = int(input("Введите число N: "))
def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)
print(factorial(n))    """


n = int(input("Введите число N: "))
def triangle(n):
    if n == 1:
        return n
    else:
        return n + triangle(n - 1)
print(triangle(n))
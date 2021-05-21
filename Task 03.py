# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

'''Эта функция ищет сумму двух наибольших чисел из трёх'''
def my_func(a,b,c):
    return a + b + c - min([a,b,c])

First = int(input('Enter first number >>> '))
Second = int(input('Enter second number >>> '))
Third  = int(input('Enter third number >>> '))

print(my_func(First, Second, Third))
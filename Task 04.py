# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

# ** Подсказка:** попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def Neg_Pow(x, y):
   return x ** y

Number = int(input('Enter positive number >>> '))
Exponent = int(input('Enter negative exponent >>> '))

print(Neg_Pow(Number, Exponent))

def Old_Neg_Pow(x, y):
    Result = 1.0 # Принудительно указываем тип
    for function in range(-y):
        Result = Result / x
    return Result

Number = int(input('Enter positive number >>> '))
Exponent = int(input('Enter negative exponent >>> '))

print(Old_Neg_Pow(Number, Exponent))

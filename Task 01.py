# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def Div_Func():
    Divisible = int(input("Введите делимое >>> "))
    Divisor = int(input("Введите делитель >>> "))
    try:
        return round(Divisible / Divisor)
    except ZeroDivisionError:
        return print("На ноль делить нельзя!")
print(Div_Func())


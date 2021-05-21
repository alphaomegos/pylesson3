# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def Summer():
    Sum_Res = 0
    Exit = False
    while Exit == False:
        Number = input('Enter numbers separated by space or press Q to quit >>> ').split()
        Res = 0
        for El in range(len(Number)):
            if Number[El] == 'Q':
                Exit = True
                break
            else:
                Res = Res + int(Number[El])
        Sum_Res = Sum_Res + Res
        print(f'Current sum is {Sum_Res}')
    print(f'Final sum is {Sum_Res}')

Summer()
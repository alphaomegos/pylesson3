# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def User_Info(Name, Surname, Birth_Year, City, Email, Phone):
    return ', '.join([Name , Surname, Birth_Year, City, Email, Phone])

print('User info: ', User_Info(Name = 'Sergey', Surname = 'Ivanov', Birth_Year = '1990', City = 'Moscow', Email = 'id90@mail.ru', Phone = '89261234576'))


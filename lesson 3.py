# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать
# у пользователя, предусмотреть обработку ситуации деления на ноль.

# def my_arg():
#     try:
#         arg1 = float(input('Введите число 1: '))
#         arg2 = float(input('Введите число 2: '))
#     except ValueError:
#         return
#     if arg2 == 0:
#         print('Деление на ноль невозможно')
#     else:
#         del_arg = arg1 / arg2
#         return del_arg
#
# print(my_arg())

# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

# def inform_data():
#     name = input('Введите Ваше имя: ')
#     f_name = input('Введите Вашу фамилию: ')
#     year_birth = input('Введите Ваш год рождения: ')
#     city = input('Введите Ваш город проживания: ')
#     email = input('Введите Ваш e-mail: ')
#     phone = input('Введите Ваш номер телефона: ')
#     return name, f_name, year_birth, city, email, phone
#
# name, f_name, year_birth, city, email, phone = inform_data()
#
# print(f"Имя: {name}; Фамилия: {f_name}; Год рождения: {year_birth}; Город проживания: {city}; e-mail: {email}; "
#       f"Номер телефона: {phone}")

# or



# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух
# аргументов.

# def my_func():
#     try:
#         arg1 = float(input('Введите число 1: '))
#         arg2 = float(input('Введите число 2: '))
#         arg3 = float(input('Введите число 3: '))
#     except ValueError:
#         return
#         min_arg = min(arg1, arg2, arg3)
#         sum_arg = sum(arg1, arg2, arg3)
#         sum_max = sum_arg - min_arg
#         return sum_max
# sum_max = my_func
# print(my_func())

# 4. Программа принимает действительное положительное число x и целое отрицательное число y. Выполните возведение
# числа x в степень y. Задание реализуйте в виде функции my_func(x, y). При решении задания нужно обойтись без встроенной
# функции возведения числа в степень.

# def my_func():
#     try:
#         x = float(input('Введите положительное число 1: '))
#         y = float(input('Введите целое отрицательное число 2: '))
#     except ValueError:
#         return
#     arg =1 / x**y
#     return arg
# print(my_func())




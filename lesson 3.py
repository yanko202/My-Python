# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать
# у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_arg():
    try:
        arg1 = float(input('Введите число 1: '))
        arg2 = float(input('Введите число 2: '))
    except ValueError:
        return
    if arg2 == 0:
        print('Деление на ноль невозможно')
    else:
        del_arg = arg1 / arg2
        return del_arg

print(my_arg())

# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

def inform_data():
    name = input('Введите Ваше имя: ')
    f_name = input('Введите Вашу фамилию: ')
    year_birth = input('Введите Ваш год рождения: ')
    city = input('Введите Ваш город проживания: ')
    email = input('Введите Ваш e-mail: ')
    phone = input('Введите Ваш номер телефона: ')
    return name, f_name, year_birth, city, email, phone

name, f_name, year_birth, city, email, phone = inform_data()

print(f"Имя: {name}; Фамилия: {f_name}; Год рождения: {year_birth}; Город проживания: {city}; e-mail: {email}; "
      f"Номер телефона: {phone}")

# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух
# аргументов.

def my_func():
    try:
        arg1 = float(input('Введите число 1: '))
        arg2 = float(input('Введите число 2: '))
        arg3 = float(input('Введите число 3: '))
    except ValueError:
        return
    min_arg = min(arg1, arg2, arg3)
    sum_arg = sum(arg1, arg2, arg3)
    sum_max = sum_arg - min_arg
        return sum_max
sum_max = my_func
print(my_func())

# or

def my_func():
    arg1 = float(input('Введите число 1: '))
    arg2 = float(input('Введите число 2: '))
    arg3 = float(input('Введите число 3: '))

    spisok = [arg1, arg2, arg3]
    sum_max = sum(spisok) - min(spisok)
    return sum_max
sum_max = my_func
print(my_func())

# 4. Программа принимает действительное положительное число x и целое отрицательное число y. Выполните возведение
# числа x в степень y. Задание реализуйте в виде функции my_func(x, y). При решении задания нужно обойтись без встроенной
# функции возведения числа в степень.

def my_func():
    try:
        x = float(input('Введите положительное число 1: '))
        y = float(input('Введите целое отрицательное число 2: '))
    except ValueError:
        return
    arg =1 / x**y
    return arg
print(my_func())

# 5. Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии Enter должна выводиться
# сумма чисел. Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter. Сумма вновь введённых
# чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается. Если специальный символ введён после
# нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def my_spisok():
    try:
        arg = int(input('Введите набор положительных числен разделенных пробелом: '))
        arg = arg.split()
    except ValueError:
        return
    for el in arg:
        if el == "N":
            retun sum_spiska
            print('Ошибка ввода')
        else:
        sum_spiska = sum(arg)
        return sum_spiska
sum_spiska = my_spisok
print(my_spisok())

# 6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же, но с прописной
# первой буквой. Например, print(int_func(‘text’)) -> Text.

def int_func():
    input_text = input('Веведите текст: ')
    text = input_text.capitalize()
    return text

print(int_func())

# 7. Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом. Каждое слово
# состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки, но каждое слово должно начинаться
# с заглавной буквы. Используйте написанную ранее функцию int_func().

def int_func():
    input_text = input('Веведите текст: ')
    text = input_text.title()
    return text

print(int_func())

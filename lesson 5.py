# 1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

f = open('my_text.txt', 'w')
f.writelines(input('Введите данные, по завершение нажмите ввод: '))
f.close()

# or

my_text = input('Введите строку: ')
with open('my_text.txt', 'w') as file:
    while my_text:
        file.write(my_text+'\n')
        my_text = input('Введите строку: ')

# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в
# каждой строке.

with open('my_text.txt', 'r') as file:
    file_lines = file.readline()
    sum_lines = len(file_lines)
    print(f'Количество строк в файле: {sum_lines}')
    for line_number, line in enumerate(file_lines, 1):
        sum_words = len(line.split())
        print(f'Количество строк в строке {line_number}: {sum_words}')

# 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.

all_sum = 0

with open('Files3' ,'r') as file:
    lines = file.readline()
    for line in lines:
        surname, wages = line.split()
        all_sum += int(wages)
        if int(wages) < 20000:
            print(f'Сотрудник имеет оклад менее 20 тыс. руб. {surname}')
average_wages = all_sum / len(lines)
print(f'Средняя зарплата сотрудников: {average_wages}')

# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные
# должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

my_dictionary = {'One':'Один',
'Two':'Два',
'Three':'Три',
'Four':'Четыре',
'Five':'Пять',
'Six':'Шесть',
'Seven':'Семь',
'Eight':'Восемь',
'Nine':'Девять'}

with open('file4', 'w') as file_write:
    for line in file_write.readlines():
        text_number, number = line.split()
        text_number = line.pop()
        file_write.write(f'{my_dictionary[text_number]}')

# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

with open('file 5', 'w') as file_write:
file_write.write(input('Введите данные через пробле, по завершение нажмите ввод: '))
f.close()

with open('file 5', 'r') as file:
    my_list = file.read.split()
    number_list = [int(number) for number in my_list if number.isdigit()]
    print(number_list)
    print(sum(number_list))



# 6. Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и наличие
# лекционных, практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий. Необязательно,
# чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.

result_dict = {}
with open('file 6', 'r') as file:
    for line in file:
        lesson_type, *lesson = line.split()
        lesson_count = int(lesson.rstrip('(лек)(прак)(лаб)'))
        result_dict.update(sum(lesson_count))
print(result_dict)

# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные о
# фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
# убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

result_list = []
dict_plus_profit = []
dict_minus_profit = []
with open('file 7', 'r') as file:
    average_profit_list = []
    for line in file.readlines()
        name, type, revenue, cost = line.split():
        profit = int(revenue - costs)
        if profit > 0:
            average_profit_list.append(profit)
            dict_plus_profit.update(name)
        else:
            dict_minus_profit.update(name)
    result_list.append(dict_plus_profit)
    result_list.append(dict_minus_profit)

    average_profit = sum(average_profit_list)/len(average_profit_list)
    result_list.append(average_profit)

f = open('file7_profit', 'w')
f.writelines(average_profit)
f.close()
    

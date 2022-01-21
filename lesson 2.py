#1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого
#элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать
#явно, в программе.

el_list_1 = 1
el_list_2 = 3
el_list_3 = 'text'
el_list_4 = True
el_list_5 = False
el_list_6 = None

my_list =  [el_list_1, el_list_2, el_list_3, el_list_4, el_list_5, el_list_6]
print(f'# 1 {type(el_list_1)} \n# 2 {type(el_list_2)} \n# 3 {type(el_list_3)} '
     f'\n# 4 {type(el_list_4)} \n# 5 {type(el_list_5)} \n# 6 {type(el_list_6)}')

# or

for element in my_list:
    print(type(element))


# 2. Для списка реализовать обмен значений соседних элементов. Значениями обмениваются элементы
# с индексами 0 и 1, 2 и 3 и т. д. При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

input_elements = input("Введите элементы списка через пробел, по завершению нажмите ввод: ")
input_elements = input_elements.split()
print(input_elements)

i = 0
while i < len(input_elements)-1:
    if i % 2 == 0:
        input_elements[i], input_elements[i+1] = input_elements[i+1], input_elements[i]
    i += 1
print(input_elements)

or

input_elements = input("Введите 4 элемента списка через пробел, по завершению нажмите ввод: ")
input_elements = input_elements.split()
print(input_elements)

input_elements[:-1:2], input_elements[1::2] = input_elements[1::2], input_elements[:-1:2]
print(input_elements)


# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и dict.

number_of_month = int(input("Введите месяц целым числом от 1 до 12: "))
if number_of_month == 12 or number_of_month == 1 or number_of_month == 2:
    print("Время года ЗИМА")
elif number_of_month == 3 or number_of_month == 4 or number_of_month == 5:
    print("Время года ВЕСНА")
elif number_of_month == 6 or number_of_month == 7 or number_of_month == 8:
    print("Время года ЛЕТО")
elif number_of_month == 9 or number_of_month == 10 or number_of_month == 11:
    print("Время года ОСЕНЬ")

or

number_of_month = int(input("Введите месяц целым числом от 1 до 12: "))
if number_of_month <= 0 or number_of_month > 12:
    print("Ведено не верное число")
else:
    winter = [12, 1, 2]
    spring = [3, 4, 5]
    summer = [6, 7, 8]
    autumm = [9, 10, 11]

    if number_of_month in winter:
        print("Время года ЗИМА")
    elif number_of_month in spring:
        print("Время года ВЕСНА")
    elif number_of_month in summer:
        print("Время года ЛЕТО")
    elif number_of_month in autumm:
        print("Время года ОСЕНЬ")

# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки нужно пронумеровать. Если слово длинное, выводить только первые 10 букв в слове.

input_string = input("Вводите строку из нескольких слов, разделённых пробелами: ")
input_words = input_string.split()
i = 1
for words in input_words:
    print(i, words[:10])
    i += 1

# 5.Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

rating_list = [7, 5, 3, 3, 2]
rating_list_copy = rating_list.copy()

input_new_rating = int(input("Вводите новый элемент рейтинга: "))

if  input_new_rating <= rating_list[-1]:
    rating_list.append(input_new_rating)
    print(f'Введенное число {input_new_rating} занимает конец списка {rating_list }')
else:
    i = 0
    while i < len(rating_list):
            if input_new_rating > rating_list[i]:
                rating_list.insert(i, input_new_rating)
                print(f'Введенное число занимает позицию {i+1} в {rating_list}')
                break

            i += 1
print(rating_list)
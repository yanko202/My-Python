#1. Поработайте с переменными, создайте несколько, выведите на экран. Запросите у пользователя
# некоторые числа и строки и сохраните в переменные, затем выведите на экран.

name = input("Введите ваше имя: ")
surname = input("Введите вашу фамилию: ")
age = int(input("Введите ваш возраст: "))
professional = input("Введите вашу профессию: ")
print(f'Привет, {name} {surname}! Твой возраст {age}. Твоя профессия {professional}')

#2. Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
#спользуйте форматирование строк.

time_seconds = int(input("Введите время в секундах: "))
time_hour = time_seconds // 3600
time_minut = (time_seconds - (time_hour * 3600)) // 60
time_seconds_1 = (time_seconds - (time_hour * 3600) - (time_minut * 60))
print(f'Время в формате чч:мм:сс\n {time_hour}:{time_minut}:{time_seconds_1}')

#3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число
#3. Считаем 3 + 33 + 333 = 369.

input_number = input("Введите целое число: ")
print(int (input_number) + int(input_number * int(2)) + int(input_number * int(3)))

#4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
#Для решения используйте цикл while и арифметические операции.

#вариант 1

input_number = input("Введите целое число: ")
input_numbers = list(input_number)
print(max(input_numbers))

#вариант 2

input_number = int(input("Введите целое число: "))
max_number = 0
while input_number != 0:
   last_element = input_number % 10
   input_number = input_number // 10
   if last_element > max_number:
      max_number = last_element
print(max_number)

#5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом
#работает фирма. Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
#Выведите соответствующее сообщение.

sales_revenue = input("Введите значение выручки вашего предпрития: ")
cost_value = input("Введите значение издержек вашего предпрития: ")
if sales_revenue > cost_value:
    print("Прибыль")
else:
    print("Убыток")

#6. Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке.
#Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.

sales_revenue = int(input("Введите значение выручки вашего предпрития, тыс.: "))
cost_value = int(input("Введите значение издержек вашего предпрития, тыс.: "))
number_employees = int(input("Введите численность сотрудников вашего предпрития: "))
profit = (sales_revenue - cost_value)
profit_employees = str(((sales_revenue - cost_value) / number_employees) / (sales_revenue - cost_value))
if sales_revenue > cost_value:
    print(f' Прибыль общая, тыс. {profit} или {profit/sales_revenue*100}%.\n '
          f'Прибыль на 1 сотрудника, тыс. {profit_employees} или {profit/sales_revenue*100/number_employees}%.')
else:
    print(f' Убыток: {name}')

#7. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
#Каждый день спортсмен увеличивал результат на 10% относительно предыдущего. Требуется определить номер дня,
#на который результат спортсмена составит не менее b километров. Программа должна принимать значения параметров a и b и
#выводить одно натуральное число — номер дня.

first_day = int(input("Введите сколько км пробежал в первый день бегун: "))
last_day = int(input("Введите сколько км должени пробежать бегун: "))
days = 1
while first_day < last_day:
    first_day *=1.1
    days +=1
    print(f'{days}-й день - {round(first_day,2)} км')




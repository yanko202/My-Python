# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) —
# на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.

from itertools import cycle

class TrafficLight:
    color = ('красный', 'желтый', 'зеленый')
    switching_time = (7, 2, 4)
    message =('Стоп, горит красный', 'Подождите, горит желтый', 'Идите, горит зеленый')

    def __init__(self, color):
        self.__color = color

    def running(self):
        my_cycle = cycle(self.switching_time)
        for traffic_color in my_cycle:
            if self.__color == traffic_color:
                print(self.message[self.color])

# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной
# в 1 см*число см толщины полотна;
# проверить работу метода.

class Road:

    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def calculation(self, weight, thickness):
        my_calculation = self._lenght * self._width * weight * thickness
        return my_calculation

my_road = Road(20,20)
print(my_road.calculation(5, 1))

# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, \
#                                                                                     {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом
# премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить
# значения атрибутов, вызвать методы экземпляров.

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):

    @property
    def full_name(self):
         return f'{self.name} {self.surname}'

    @property
    def employee_income(self):
         return self._income['wage'] + self._income['bonus']

my_position = Position('Petr', 'Petrov', 450, 150)
print(f'{my_position.get.full_name} {my_position.get.employee_income}')

# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы:
# go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.

class Cars:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.color} машина марки {self.name} поехала со скоростью {self.speed}')
    def stop(self):
        print(f'{self.color} машина марки {self.name} остановилась')
    def turn(self, direction):
        print(f'{self.color} машина марки {self.name} повернкула на {direction}')
    def show_speed(self)
        print(f'Текущая скорость {self.speed}')

class TownCar(Cars):

    def show_speed(self):
        if self.speed > 60:
            print(f'Вы превышаете допустимую скорость, 60 км/ч')
            else
            print(f'Вы едите с разрещенной скорось. Ваша скорость '{cars.show.speed})

class SportCar(Cars):
    def __init__(self, speed, color, name):
        Cars.__init__(speed, color, name, si_police=False)

class WorkCar(Cars):
    def show_speed(self):
        if self.speed < 40 or self.speed > 60:
            print(f'Проверьти вашу скокость, Вы нарушаете')
        else
            print(f'Ваша скорость {cars.show.speed}')

class SportCar(Cars):
    def __init__(self, speed, color, name):
        Cars.__init__(speed, color, name, si_police=True)

my_police_cer = PoliceCar(10, 'белый', 'Geely')
my_police_car.go()
my_police_car.turn('налево')
my_police_car.stop()
my_police_car.show_speed()

5. Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationary:
    def __init__(self, title):
        sel.title = title

    def draw(self):
        print('Start draw')

class Pen(Stationary)
    def draw(self):
        print(f'We are drawind by {self.title}')

class Pencil(Stationary):
    def draw(self):
        print(f'We are drawind by {self.title}')

class Handle(Stationary):
    def draw(self):
        print(f'We are drawind by {self.title}')

pen =  Pen('pen')
pencil - Pencil('pencil')
pen.draw()
handle.draw()
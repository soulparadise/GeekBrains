class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print('Машина двигается')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина поворачивает {direction}')

    def show_speed(self):
        print(f'Скорость машины: {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Превышена допустимая скорость')
        else:
            super().show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Превышена допустимая скорость')
        else:
            super().show_speed()


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


auto_1 = WorkCar(10, 'green', 'CAT')
auto_1.go()
auto_1.turn('Налево')
auto_1.show_speed()
auto_1.stop()
print(auto_1.is_police)

auto_2 = WorkCar(50, 'black', 'Uaz')
auto_2.show_speed()

auto_3 = PoliceCar(100, 'pink', 'honda')
auto_3.stop()
print(auto_3.is_police)





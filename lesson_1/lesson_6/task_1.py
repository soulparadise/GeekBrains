from time import sleep
from itertools import cycle


class TrafficLight:
    def __init__(self):
        self.__color = ['Красный', 'Оранжевый', 'Зеленый']

    def running(self, traffic_counter):
        count = 0
        iterator = cycle(self.__color)
        for el in iterator:
            if count == traffic_counter:
                break
            print(el)
            sleep(7)
            print(next(iterator))
            sleep(2)
            print(next(iterator))
            count += 1
            sleep(5)


traffic_light = TrafficLight()
traffic_light.running(3)

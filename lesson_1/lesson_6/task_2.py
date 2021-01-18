class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate(self):
        print(
            f'Масса асфальта необходимая для покрытия всей дороги равна: '
            f'{self._length * self._width * 25 * 1 // 1000} тонн')


road = Road(20, 5000)
road.calculate()
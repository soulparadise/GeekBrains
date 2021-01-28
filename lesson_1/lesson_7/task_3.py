class Cell:
    def __init__(self, part):
        self.part = part

    def __add__(self, other):
        return f'Сумма ячеек двух клеток равна: {self.part + other.part}'

    def __sub__(self, other):
        if other.part > self.part:
            return 'Вычитание невозможно. Колличество ячеек второй клетки превышает колличество ячеек первой клетки'
        else:
            return f'Результат вычитания равен: {self.part - other.part}'

    def __mul__(self, other):
        return f'Результат произведения двух клеток равен: {self.part * other.part}'

    def __truediv__(self, other):
        return f'Результат деления клеток равен: {round(self.part // other.part)}'

    def make_order(self, line):
        print(range(self.part // line))
        return '\n'.join(['*' * line for el in range(self.part // line)]) + '\n' + '*' * (self.part % line)


first_cell = Cell(10)
second_cell = Cell(10)
print(second_cell.make_order(3))

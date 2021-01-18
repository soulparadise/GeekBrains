class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):

    def draw(self):
        print(f'Запуск отрисовки инструментом {self.title}')


class Pencil(Stationery):

    def draw(self):
        print(f'Начинаем отрисовывать инструментом {self.title}')


class Handle(Stationery):

    def draw(self):
        print(f'Орисовываем инструментом {self.title}')


pen = Pen('Ручка')
pen.draw()
pencil = Pencil('Карандаш')
pencil.draw()
handle = Handle('Маркер')
handle.draw()

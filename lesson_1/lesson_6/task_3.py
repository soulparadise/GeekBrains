class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Positions(Worker):

    def get_full_name(self):
        print(self.name, self.surname, self.position)

    def get_total_income(self):
        print(self._income['wage'] + self._income['bonus'])


income_worker_1 = dict(wage=5000, bonus=3000)
income_worker_2 = dict(wage=11000, bonus=14000)

worker_1 = Positions('Maksim', 'Vaziulia', 'GitMaestro', income_worker_1)
worker_1.get_full_name()
worker_1.get_total_income()
worker_2 = Positions('Nikolai', 'Kopernik', 'Astronomer', income_worker_2)
worker_2.get_full_name()
worker_2.get_total_income()

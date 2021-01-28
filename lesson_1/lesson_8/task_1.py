import random


class LotoCard:

    def __init__(self, name):
        self.name = name
        self.card = self.generate_card()

    def __str__(self):
        return self.name + ':\n' + ('-' * 34) + '\n' + '\n'.join('\t'.join(map(str, el)) for el in self.card) + '\n'

    def generate_card(self):
        my_list = random.sample(range(1, 91), 15)
        list_a = random.sample(my_list, 5)
        my_list = [el for el in my_list if el not in list_a]
        list_b = random.sample(my_list, 5)
        list_c = [el for el in my_list if el not in list_b]
        for _ in range(4):
            list_a.append(' '), list_b.append(' '), list_c.append(' ')

        for element in [list_a, list_b, list_c]:
            random.shuffle(element)

        for element in [list_a, list_b, list_c]:
            self.list_sort(element)

        new_list = []
        new_list.append(list_a), new_list.append(list_b), new_list.append(list_c)
        return new_list

    def list_sort(self, input_list):
        indexes = []
        numbers = []
        for idx, el in enumerate(input_list):
            if isinstance(el, int):
                indexes.append(idx)
                numbers.append(el)
        numbers = sorted(numbers)
        for idx, el in enumerate(numbers):
            input_list[indexes[idx]] = el


class LotoGame:
    def __init__(self, player_card, computer_card):
        self.player_card = player_card
        self.computer_card = computer_card

    def roll_generate(self):
        for el in random.sample(range(1, 91), 90):
            yield el

    def start(self):
        player_score = 0
        computer_score = 0
        roll = self.roll_generate()
        while True:
            if player_score == 15:
                print('Победил Игрок')
                break
            if computer_score == 15:
                print('Победил компьютер')
                break
            print(self.player_card)
            print(self.computer_card)
            roll_step = next(roll)
            print(f'Игрок {player_score} : {computer_score} Компьютер')
            print(f'Новый бочонок: {roll_step}')
            player_answer = input('Хотите зачеркнуть?')

            check_computer_answer = self.check_roll(self.computer_card.card, roll_step, True)
            if check_computer_answer:
                computer_score += 1

            if player_answer == 'y':
                check_player_answer = self.check_roll(self.player_card.card, roll_step)
                player_score += 1
                if not check_player_answer:
                    print('Вы ошиблись. Игра окончена.')
                    break
            if player_answer == 'n':
                exit_check = False
                for row in self.player_card.card:
                    if roll_step in row:
                        print('Вы ошиблись. Игра окончена.')
                        exit_check = True
                        break
                if exit_check:
                    break

    def check_roll(self, card, roll, is_computer=False):
        element_exists = False
        for row in card:
            if roll in row:
                idx = row.index(roll)
                row[idx] = '-'
                element_exists = True

            if element_exists:
                break

        if not (element_exists or is_computer):
            return False
        elif element_exists and is_computer:
            return True
        elif not element_exists and is_computer:
            return False
        else:
            return True


human_player = LotoCard('Игрок')
computer_player = LotoCard('Компьютер')
game = LotoGame(human_player, computer_player)
game.start()

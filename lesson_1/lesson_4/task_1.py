import argparse

parser = argparse.ArgumentParser()

parser.add_argument('hours_of_work', type=int, help='How many hours did the employee work')
parser.add_argument('money_per_hour', type=int, help='Money per hour')
parser.add_argument('premium', type=int, help='Amount of premium')


def payment(a, b, c):
    return a * b + c


args = parser.parse_args()

print(payment(args.hours_of_work, args.money_per_hour, args.premium))

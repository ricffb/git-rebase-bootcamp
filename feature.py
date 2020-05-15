import sys
import random

MSG = [
    "Hello",
    "Whats up",
    "Greetings,"
]

Finalize = [
    "Have a good day!",
    "Enjoy life!",
    "Here are your lemons!"
]


def message_builder(name: str) -> str:
    greet = MSG[random.randint(0, len(MSG)-1)] + ", "
    fin = Finalize[random.randint(0, len(Finalize)-1)]

    return greet + name + "!\n" + fin


def better_printer(name):
    print(message_builder(name))


if __name__ == '__main__':
    better_printer(sys.argv[1])

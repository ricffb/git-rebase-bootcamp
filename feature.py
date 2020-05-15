import os, sys
import tensorflow as tf
import numpy as np
import random

MSG = [
    "Hello",
    "Whats up",
    "Greetings,"
]


def better_printer(name):
    print(MSG[random.randint(0, len(MSG)-1)] + ",", name + "!")


if __name__ == '__main__':
    better_printer(sys.argv[1])

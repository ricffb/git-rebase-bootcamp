import sys


def print_hello(msg):

    print("Hello,", msg, "!")


if __name__ == "__main__":
    print_hello(sys.argv[1])
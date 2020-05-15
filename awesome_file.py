import sys


def print_hello(msg):

    print("Hello,", msg, "!")


def print_hello_to_everyone(msgs):

    for name in msgs:
        print("Hello,", name, "!")


if __name__ == "__main__":
    print_hello_to_everyone(sys.argv[1:])
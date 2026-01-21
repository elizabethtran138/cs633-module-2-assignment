import random
import time

FUN_FORTUNES = [
    "You're close to finishing your Jira task!",
    "Good things are coming your way!",
    "This is going to be a super fun weekend!",
    "A song will hit differently today",
    "You're about to get super lucky this weekend"
]


def print_fortune(fortune):
    for char in fortune:
        print(char, end="", flush=True)
        time.sleep(0.05)
    print()


def main():
    print_fortune("Hiya there!")
    time.sleep(0.5)

    print_fortune(random.choice(FUN_FORTUNES))


if __name__ == "__main__":
    main()
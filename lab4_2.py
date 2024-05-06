import random


def throw_dice():
    result = random.randint(1, 6)
    print(f"Кубик показывает: {result}")
    if result == 5 or result == 6:
        print("Вы победили!")
    elif result == 3 or result == 4:
        throw_dice()
    elif result == 1 or result == 2:
        print("Вы проиграли!")


if __name__ == "__main__":
    throw_dice()

import random

def guess(n):
    i = 0
    while True:
        i += 1
        print("What's your guess between 1 and 99?")
        k = input(">> ")
        if k.isdigit():
            g = int(k)
            if g == n:
                break
            elif g > n:
                print("Too high!")
            else:
                print("Too low!")
        else:
            print("That's not a number.")
    print("Congratulations, you've got it!")
    print("You won in {} attempts!".format(i))


if __name__ == "__main__":
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 to find out the secret number.")
    print("Type 'exit' to end the game.")
    print("Good luck!\n")
    n = random.randint(1, 99)
    guess(n)
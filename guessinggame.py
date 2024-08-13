import random
def main():
    while True:
        lvl_input= (input("Level:"))
        if lvl_input.isdigit():
            lvl_input= int(lvl_input)
            print(lvl_input)
            if lvl_input > 0:
                break
    while True:
        guess_input= (input("Guess:"))
        if guess_input.isdigit():
            guess_input = int(guess_input)
            if guess_input > 0:
                break
    n = random.randrange(0, lvl_input +1)
    if n == guess_input:
        print("Just right!")
    elif n < guess_input:
        print("Too large!")
    else:
        print("Too small!")

main()
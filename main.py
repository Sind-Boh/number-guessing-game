import random

def game():

    number = random.randint(1,100)
    print("Hello! This is Number Guessing Game!")
    print("Rules: You have to guess a random number from 1 to 100")

    diff_mes = "1.Easy (10 chances); 2.Normal (5 chances); 3.Hard (3 chances)"
    diff = int(input(f"{diff_mes}\nChoose difficulty: "))

    while True:
        if diff > 3:
            print("Try again!")
            diff = int(input(f"{diff_mes}\nChoose difficulty: "))
        else:
            if diff == 1:
                print("You have 10 chances!")
                break
            elif diff == 2:
                print("You have 5 chances!")
                break
            elif diff == 3:
                print("You have 3 chances!")
                break
            
    guess_num = 0
    guess_num_max = 0
    if diff == 1:
        guess_num_max = 10
    elif diff == 2:
        guess_num_max = 5
    else:
        guess_num_max = 3

#    print(number)
#    print(guess_num_max)

    while True:
        if guess_num < guess_num_max:
            guess = int(input("Enter your guess: "))
            if guess > 100:
                print("Remember the rules! Enter number between 1 & 100!")
            else:
                if guess_num == (guess_num_max - 2):
                    if guess > number:
                        print(f"Number is smaller than {guess}!")
                    elif guess < number:
                        print(f"Number is bigger than {guess}!")
                    ch_hint = input("Do you want a hint? [y/n]: ")
                    if ch_hint.lower() == "y":
                        print("Here is your hint:\nYour number is lower than",
                              number + random.randint(1,5), 
                              "and bigger than", number - random.randint(1,5))
                        guess_num += 1
                    elif ch_hint.lower() == "n":
                        guess_num += 1
                        continue
                else: 
                    if guess == number:
                        print("Congrats!")
                        break
                    elif guess > number:
                        guess_num += 1
                        print(f"Number is smaller than {guess}!")
                    elif guess < number:
                        guess_num += 1
                        print(f"Number is bigger than {guess}!")
        else:
            print(f"You lost! Answer: {number}")
            break

game()
while True:
    cont = input("Do you wanna play again? [y/n]: ")
    if cont.lower() == "y":
        game()
    elif cont.lower() == "n":
        break
    else:
        print("Try again!")

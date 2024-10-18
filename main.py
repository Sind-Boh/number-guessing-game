import random
import time

def welcome():
    print("\nHello! This is Number Guessing Game!")
    print("Rules: You have to guess a random number from 1 to 100\n")

def diff():
    diff_mes = "1.Easy (10 chances); 2.Normal (5 chances); 3.Hard (3 chances)"
    diff = int(input(f"{diff_mes}\nChoose difficulty: "))
    while True:
        if diff > 3:
            print("Try again! Enter 1, 2 or 3")
            diff = int(input(f"{diff_mes}\nChoose difficulty: "))
        else:
            if diff == 1:
                print("You have 10 chances!\n")
                break
            elif diff == 2:
                print("You have 5 chances!\n")
                break
            elif diff == 3:
                print("You have 3 chances!\n")
                break
    guess_num_max = 0
    if diff == 1:
        guess_num_max = 10
    elif diff == 2:
        guess_num_max = 5
    else:
        guess_num_max = 3
    return guess_num_max

def game(guess_num_max, number):
    start = time.time()
    guess_num = 0
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
                        end = time.time()
                        time_rec = end - start
                        time_rec = round(time_rec, 3)
                        print("\nCongrats! You have won in", guess_num + 1, "turns!\n"
                              "You have spend", time_rec, "s.")
                        return time_rec
                        break
                    elif guess > number:
                        guess_num += 1
                        print(f"Number is smaller than {guess}!")
                    elif guess < number:
                        guess_num += 1
                        print(f"Number is bigger than {guess}!")
        else:
            print(f"\nYou lost! Answer: {number}")
            break

def records(guess_num_max, time_rec):
    recs.setdefault("Easy", 0)
    recs.setdefault("Normal", 0)
    recs.setdefault("Hard", 0)
    if guess_num_max == 10 and (time_rec < recs["Easy"] or recs["Easy"] == 0): 
        recs.update({"Easy" : time_rec})
    if guess_num_max == 5 and (time_rec < recs["Normal"] or recs["Normal"] == 0): 
        recs.update({"Normal" : time_rec})
    if guess_num_max == 3 and (time_rec < recs["Hard"] or recs["Hard"] == 0): 
        recs.update({"Hard" : time_rec})
    print("Your records:", recs)

def main():
    number = random.randint(1,100)
    guess_num_max = diff()
    time_rec = game(guess_num_max, number)
    if time_rec != None:
        records(guess_num_max, time_rec)

def contin():
    while True:
        cont = input("\nDo you wanna play again? [y/n]: ")
        if cont.lower() == "y":
            print('\n')
            main()
        elif cont.lower() == "n":
            break
        else:
            print("Try again!")
recs = {}
welcome()
main()
contin()

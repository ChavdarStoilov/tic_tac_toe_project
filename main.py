import random

places = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}

def board():
    print("------------------------\n       |       |")
    print(f"   {places.get(1)}   |   {places.get(2)}   |   {places.get(3)}   \n       |       |       ")
    print("------------------------\n       |       |")
    print(f"   {places.get(4)}   |   {places.get(5)}   |   {places.get(6)}   \n       |       |       ")
    print("------------------------\n       |       |")
    print(f"   {places.get(7)}   |   {places.get(8)}   |   {places.get(9)}   \n       |       |       ")
    print("------------------------")

def winner():

    if places[1] == "x" and places[2] == "x" and places[3] == "x":
        return "Computer win"
    elif places[1] == "o" and places[2] == "o" and places[3] == "o":
        return "You win"

    if places[4] == "x" and places[5] == "x" and places[6] == "x":
        return "Computer win"
    elif places[4] == "o" and places[5] == "o" and places[6] == "o":
        return "You win"

    if places[7] == "x" and places[8] == "x" and places[9] == "x":
        return "Computer win"
    elif places[7] == "o" and places[8] == "o" and places[9] == "o":
        return "You win"

    if places[1] == "x" and places[4] == "x" and places[7] == "x":
        return "Computer win"
    elif places[1] == "o" and places[4] == "o" and places[7] == "o":
        return "You win"

    if places[2] == "x" and places[5] == "x" and places[8] == "x":
        return "Computer win"
    elif places[2] == "o" and places[5] == "o" and places[8] == "o":
        return "You win"

    if places[3] == "x" and places[6] == "x" and places[9] == "x":
        return "Computer win"
    elif places[3] == "o" and places[6] == "o" and places[9] == "o":
        return "You win"

    if places[1] == "x" and places[5] == "x" and places[9] == "x":
        return "Computer win"
    elif places[1] == "o" and places[5] == "o" and places[9] == "o":
        return "You win"

    if places[7] == "x" and places[5] == "x" and places[3] == "x":
        return "Computer win"
    elif places[7] == "o" and places[5] == "o" and places[3] == "o":
        return "You win"



def choose(computer_choice):

    if places[computer_choice] == " ":
        places[computer_choice] = "x"
    else:
        computer_choosing()



def computer_choosing():


    computer = random.randrange(1, 9)

    choose(computer)

def new_computer_choose():

    if places[9] == "o" and places[5] == "o" or places[4] == "o" and places[7] == "o" or places[3] == "o" and places[2] == "o":
        if places[1] == " ":
            places[1] = "x"
        else:
            computer_choosing()

    elif places[1] == "о" and places[3] == "o" or places[8] == "o" and places[5] == "o":
        if places[2] == " ":
            places[2] = "x"
        else:
            computer_choosing()

    elif places[7] == "o" and places[5] == "o" or places[1] == "o" and places[2] == "o" or places[9] == "o" and places[6] == "o":
        if places[3] == " ":
            places[3] = "x"
        else:
            computer_choosing()

    elif places[6] == "o" and places[5] == "o" or places[1] == "o" and places[7] == "o":
        if places[4] == " ":
            places[4] = "x"
        else:
            computer_choosing()

    elif places[9] == "o" and places[1] == "o" or places[7] == "o" and places[3] == "o" or places[4] == "о" and places[6] == "o" or places[2] == "о" and places[8] == "o":
        if places[5] == " ":
            places[5] = "x"
        else:
            computer_choosing()

    elif places[4] == "o" and places[5] == "o" or places[3] == "0" and places[9] == "o":
        if places[6] == " ":
            places[6] = "x"
        else:
            computer_choosing()

    elif places[3] == "o" and places[5] == "o" or places[8] == "0" and places[9] == "o" or places[1] == "o" and places[4] == "o":
        if places[7] == " ":
            places[7] = "x"
        else:
            computer_choosing()

    elif places[9] == "o" and places[7] == "o" or places[2] == "o" and places[5] == "o":
        if places[8] == " ":
            places[8] = "x"
        else:
            computer_choosing()

    elif places[1] == "o" and places[5] == "o" or places[7] == "o" and places[8] == "o" or places[3] == "o" and places[6] == "o":
        if places[9] == " ":
            places[9] = "x"
        else:
            computer_choosing()

    else:
        computer_choosing()

    board()

def your_choosing(choose):
    your_choose = int(choose)
    if places[int(your_choose)] == " ":
        places[int(your_choose)] = "o"


    if winner() == "Computer win" or winner() == "You win":
        board()
        print(winner())
        exit()

    elif places[1] == " " or places[2] == " " or places[3] == " " or places[4] == " " or places[5] == " " or \
            places[6] == " " or places[7] == "" or places[8] == " " or places[9] == " ":

        print("Computer choosing....")
        new_computer_choose()

    else:
        print("There no winner")
        exit()


board()
start = input("Choose number from 1 to 9: ")

while start != "stop":
    if start == "":
        start = input("Cannot enter empty input, please enter number from 1 to 9:")

    your_choosing(start)

    if winner() == "Computer win" or winner() == "You win":
        print(winner())
        break

    start = input("Choose number from 1 to 9: ")
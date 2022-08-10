import random


def board(place):
    print("------------------------\n       |       |")
    print(f"   {place.get(1)}   |   {place.get(2)}   |   {place.get(3)}   \n       |       |       ")
    print("------------------------\n       |       |")
    print(f"   {place.get(4)}   |   {place.get(5)}   |   {place.get(6)}   \n       |       |       ")
    print("------------------------\n       |       |")
    print(f"   {place.get(7)}   |   {place.get(8)}   |   {place.get(9)}   \n       |       |       ")
    print("------------------------")

def winner(place):

    if place[1] == "x" and place[2] == "x" and place[3] == "x":
        return "Computer win"
    elif place[1] == "o" and place[2] == "o" and place[3] == "o":
        return "You win"

    if place[4] == "x" and place[5] == "x" and place[6] == "x":
        return "Computer win"
    elif place[4] == "o" and place[5] == "o" and place[6] == "o":
        return "You win"

    if place[7] == "x" and place[8] == "x" and place[9] == "x":
        return "Computer win"
    elif place[7] == "o" and place[8] == "o" and place[9] == "o":
        return "You win"

    if place[1] == "x" and place[4] == "x" and place[7] == "x":
        return "Computer win"
    elif place[1] == "o" and place[4] == "o" and place[7] == "o":
        return "You win"

    if place[2] == "x" and place[5] == "x" and place[8] == "x":
        return "Computer win"
    elif place[2] == "o" and place[5] == "o" and place[8] == "o":
        return "You win"

    if place[3] == "x" and place[6] == "x" and place[9] == "x":
        return "Computer win"
    elif place[3] == "o" and place[6] == "o" and place[9] == "o":
        return "You win"

    if place[1] == "x" and place[5] == "x" and place[9] == "x":
        return "Computer win"
    elif place[1] == "o" and place[5] == "o" and place[9] == "o":
        return "You win"

    if place[7] == "x" and place[5] == "x" and place[3] == "x":
        return "Computer win"
    elif place[7] == "o" and place[5] == "o" and place[3] == "o":
        return "You win"



def choose(computer_choice, place):

    if place[computer_choice] == " ":
        place[computer_choice] = "x"
    else:
        computer_choosing(place)



def computer_choosing(place):


    computer = random.randrange(1, 9)

    choose(computer, place)

def new_computer_choose(place):

    if place[9] == "o" and place[5] == "o" or place[4] and place[7] == "o" or place[3] == "o" and place[2] == "o":
        if place[1] == " ":
            place[1] = "x"
        else:
            computer_choosing(place)

    elif place[1] == "о" and place[3] == "o" or place[8] == "o" and place[5] == "o":
        if place[2] == " ":
            place[2] = "x"
        else:
            computer_choosing(place)

    elif place[7] == "o" and place[5] == "o" or place[1] == "o" and place[2] == "o" or place[9] == "o" and place[6] == "o":
        if place[3] == " ":
            place[3] = "x"
        else:
            computer_choosing(place)

    elif place[6] == "o" and place[5] == "o" or place[1] == "o" and place[7] == "o":
        if place[4] == " ":
            place[4] = "x"
        else:
            computer_choosing(place)

    elif place[9] == "o" and place[1] == "o" or place[7] == "o" and place[3] == "o" or place[4] == "о" and place[6] == "o" or place[2] == "о" and place[8] == "o":
        if place[5] == " ":
            place[5] = "x"
        else:
            computer_choosing(place)

    elif place[4] == "o" and place[5] == "o" or place[3] == "0" and place[9] == "o":
        if place[6] == " ":
            place[6] = "x"
        else:
            computer_choosing(place)

    elif place[3] == "o" and place[5] == "o" or place[8] == "0" and place[9] == "o" or place[1] == "o" and place[4] == "o":
        if place[7] == " ":
            place[7] = "x"
        else:
            computer_choosing(place)

    elif place[9] == "o" and place[7] == "o" or place[2] == "o" and place[5] == "o":
        if place[8] == " ":
            place[8] = "x"
        else:
            computer_choosing(place)

    elif place[1] == "o" and place[5] == "o" or place[7] == "o" and place[8] == "o" or place[3] == "o" and place[6] == "o":
        if place[9] == " ":
            place[9] = "x"
        else:
            computer_choosing(place)

    else:
        computer_choosing(place)

    board(place)

def your_choosing(choose, place):
    your_choose = int(choose)
    if place[int(your_choose)] == " ":
        place[int(your_choose)] = "o"


    if winner(place) == "Computer win" or winner(place) == "You win":
        board(place)
        print(winner(place))
        exit()

    elif place[1] == " " or place[2] == " " or place[3] == " " or place[4] == " " or place[5] == " " or \
            place[6] == " " or place[7] == "" or place[8] == " " or place[9] == " ":

        print("Computer choosing....")
        new_computer_choose(place)

    else:
        print("There no winner")
        exit()

places = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}
board(places)
start = input("Choose number from 1 to 9: ")

while start != "stop":
    if start == "":
        start = input("Cannot enter empty input, please enter number from 1 to 9:")

    your_choosing(start, places)

    if winner(places) == "Computer win" or winner(places) == "You win":
        print(winner(places))
        break

    start = input("Choose number from 1 to 9: ")
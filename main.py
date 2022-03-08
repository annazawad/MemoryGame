import random
import pandas as pd
import numpy as np
import datetime
from datetime import date

file_words = "words.txt"
winner = pd.read_csv("winners.csv")
winnerHard = pd.read_csv("winnersH.csv")

class game_list:
    def __init__(self,file,num_cards):
        self.file = file
        self.num_cards = num_cards

    def create_tab(self):
        tab = []
        for line in open(self.file, 'r'):
            tab.append(line)
        k = len(tab)
        i = 0
        while i < k:
            tab[i] = tab[i].replace("\n", "")
            i += 1
        tab2 = []
        for word in range(0, self.num_cards):
            tab2.append(random.choice(tab))
            tab.remove(tab2[word])
        tab2 = 2 * tab2
        return tab2

#board = game_list(file_words,3)
#a = board.create_tab()
#random.shuffle(a)
#print(a)

def x_board(num_cards):
    x_b = pd.DataFrame(np.array([["X" for i in range(0, num_cards)], ["X" for i in range(0, num_cards)]]), index=["A", "B"],
                       columns=[i for i in range(1, num_cards +1)])
    return x_b

def word_board(num_cards):
    w_b = game_list(file_words,num_cards)
    w_b3 = w_b.create_tab()
    random.shuffle(w_b3)
    w_b2 = pd.DataFrame(np.array([[w_b3[i] for i in range(0, num_cards)], [w_b3[i] for i in range(num_cards, 2*num_cards)]]), index=["A", "B"],
                      columns=[i for i in range(1, num_cards+1)])
    return w_b2

#print(word_board(6))
#supporting_table = x_board()

def game(x_board,word_board,num_quess,num_cards):
    if num_cards == 4:
        level = 'EASY'
    else:
        level = "DIFFICULT"

    win = False
    k = 0

    while num_quess > 0:
        if num_cards == 0:
            win = True
            num_quess = 0
            break
        else:
            k += 1
            print("Level: ",level,"\n Chances: ", num_quess)
            print(x_board)
            row_1 = str(input("Enter the row: \n"))
            col_1 = int(input("Enter the col: \n"))
            x_board.at[row_1, col_1] = word_board.at[row_1, col_1]
            print(x_board)
            row_2 = str(input("Enter the row: \n"))
            col_2 = int(input("Enter the col: \n"))
            x_board.at[row_2, col_2] = word_board.at[row_2, col_2]
            print(x_board)
            if x_board.at[row_1, col_1] != x_board.at[row_2, col_2]:
                x_board.at[row_1, col_1] = 'X'
                x_board.at[row_2, col_2] = 'X'
                num_quess -= 1
            else:
                num_cards -= 1
                num_quess -= 1

    return win,k

#num_cards = 3
#num_quess = 6
#vx_board = x_board(num_cards)
#vword_board = word_board(num_cards)
#game(vx_board,vword_board,num_quess,num_cards)

choice = 0
while choice != 3:
    start = datetime.datetime.now()
    choice = int(input("Choose the level\n 1 - EASY\n 2 - DIFFICULT\n 3- quit the game\n"))
    if choice == 1:
        num_cards = 2
        num_guess = 6
    elif choice == 2:
        num_cards = 4
        num_guess = 16
    elif choice == 3:
        print("Thank you")
        break
    else:
        print("Choose from avaiable choices")
        continue
    vx_board = x_board(num_cards)
    vword_board = word_board(num_cards)
    W = game(vx_board,vword_board, num_guess, num_cards)
    if W[0]:
        print("YOU WON \n")
        duration = datetime.datetime.now() - start
        today = date.today()
        print(f"It took you {W[1]} chances and {duration.seconds} seconds to win.")
        name = input("What's your name?: ")
        df5 = pd.DataFrame([[name, W[1],duration.seconds,today]], columns=['name','chances','time','date'])
        if choice == 1:
            winner = pd.concat([winner,df5], ignore_index=True)
            winner = winner.nsmallest(10,"chances")
            winner.to_csv("winners.csv")
            print(winner[['name','chances','time','date']])
        else:
            winnerHard = pd.concat([winnerHard, df5], ignore_index=True)
            winnerHard = winnerHard.nsmallest(10, "chances")
            winnerHard.to_csv("winnersH.csv")
            print(winnerHard[['name', 'chances', 'time', 'date']])
        stay = input(print("Do you want to restart the game (y/n) ?: "))
        if stay == 'y':
            continue
        else:
            break
    else:
        print("GAME OVER \n")
        if choice ==1:
            winner = winner.nsmallest(10, "chances")
            print('See the list of best scores:\n \n', winner[['name','chances','time','date']])
        else:
            winnerHard = winnerHard.nsmallest(10, "chances")
            print('See the list of best scores:\n \n', winnerHard[['name', 'chances', 'time', 'date']])
        stay = input(print("Do you want to restart the game (y/n) ?: "))
        if stay == 'y':
            continue
        else:
            print("GOODBYE!")
            break

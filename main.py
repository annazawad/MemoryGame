import random
import pandas as pd
import numpy as np
import datetime
from datetime import date

file_words = "words.txt"

"""def game_list(file):
    tab = []
    for line in open(file,'r'):
        tab.append(line)
    k = len(tab)
    i = 0
    while i< k:
        tab[i] = tab[i].replace("\n","")
        i +=1
    return tab
print(game_list(file_words))"""

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

#board = game_list(file_words,4)
#board.create_tab()

def x_board(num_cards):
    x_b = pd.DataFrame(np.array([["X" for i in range(0, num_cards)], ["X" for i in range(0, num_cards)]]), index=["A", "B"],
                       columns=[i for i in range(1, num_cards +1)])
    return x_b

def word_board(num_cards):
    w_b = game_list(file_words,num_cards)
    random.shuffle(w_b.create_tab())
    w_b2 = pd.DataFrame(np.array([[w_b.create_tab()[i] for i in range(0, num_cards)], [w_b.create_tab()[i] for i in range(num_cards, 2*num_cards)]]), index=["A", "B"],
                      columns=[i for i in range(1, num_cards+1)])
    return w_b2

print(word_board(4))
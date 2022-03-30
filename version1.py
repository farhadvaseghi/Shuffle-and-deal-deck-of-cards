import random
from random import choice, randrange
random.seed(10)

type = ['Spade', 'Heart', 'Diamond', 'Club']
dic = {'Spade':list(range(1,14)),'Heart':list(range(1,14)),'Diamond':list(range(1,14)),'Club':list(range(1,14))}

player = [{'Spade': [], 'Heart': [], 'Diamond': [], 'Club': []}, {'Spade': [], 'Heart': [], 'Diamond': [], 'Club': []}, {'Spade': [], 'Heart': [], 'Diamond': [], 'Club': []}, {'Spade': [], 'Heart': [], 'Diamond': [], 'Club': []}]

for j in range(0, 13):
    for i in range(4):
        choose = random.choice(type)
        if len(dic[choose]) != 0 :
            player[i][choose].append(dic[choose].pop(random.randrange(len(dic[choose]))))


for i in range(4):
    print("[INFO] player No {} _ Deck of Cards: {}".format(i+1, player[i]))

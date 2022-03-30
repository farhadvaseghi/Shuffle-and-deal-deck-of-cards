# Python program to shuffle a deck of card

# importing modules
import itertools, random
random.seed(10)

# make a deck of cards
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))

# shuffle the cards
random.shuffle(deck)

# draw five cards
j=1
print("player No {}".format(j))
for i in range(52):
    print(deck[i][0], "of", deck[i][1],)
    if (i+1)%13==0 and j<4:
        print('------------------------------------------------')
        j+=1
        print("player No {}".format(j))

   



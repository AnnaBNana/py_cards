import random
from card import Card
'''
Style Note:
While functions in your code should be sepparated by two blank lines, class methods should be sepparated by one.
'''

class Deck(object):
    def __init__(self):
        # fun fact: empty objects, including empty strings, lists, tuples, etc. evaluate to false in python
        self.cards = []
        self.reset()

    def reset(self):
        values = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
        suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        # shown below is a single line of code that replaces the nested for loops commented out below.  this technique is known as list comprehension, a more advanced concept that will at first be confusing, and then awesome, try a simpler version for yourself:
        #test = [i for i in range(10)]
        #print test
        self.cards = [Card(v,s) for v in values for s in suits]
        # for s in suits:
        #     for v in values:
        #         card = Card(v, s)
        #         self.cards.append(card)

    # Most of you should recognize this as the Fisher-Yates shuffle.  Why is this shuffle superior (i.e. more efficient) than some other solutions?
    def shuffle(self):
        length = len(self.cards)
        l = length - 1
        for i in range(l,0,-1):
            r = random.randint(0,i)
            # note that python makes swapping list values very simple.  This is very exciting to anyone who's been making manual swaps, as we have been doing in morning algoritms.  Would something like this work in JavaScript?
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def deal(self):
        self.shuffle()
        card = self.cards.pop()
        return card

    # let's write a debugging function to help us visualize our cards.  objects can be annoying to debug in python because of the way they display in terminal.  let's create a helper function to fix that
    def show(self):
        for c in self.cards:
            #the vars() built-in displays the attributes of an object in dict form
            print "card in deck: ", vars(c)
        print "The deck contains ", len(self.cards), " cards."

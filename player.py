class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def hit(self, deck):
        #make sure you're removing from the deck every time a player adds a card to their hand
        card = deck.deal()
        self.hand.append(card)
        return self

    def discard(self, index):
        if index < len(self.hand):
            self.hand.remove(self.hand[index])
            print "removed", self.hand[index].value, "of", self.hand[index].suit, "from hand!"
        else:
            print "index out of range"
        return self

    #show hand for debugging
    def show_hand(self):
        print self.name,"'s hand: "
        for c in self.hand:
            print "card: ", vars(c)
        print self.name, " has ", len(self.hand), " cards"
        return self

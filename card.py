class Card(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    # a card doesn't have to do anything, but let's add a show method for debugging
    def show(self):
        return vars(self)

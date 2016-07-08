from deck import Deck
from card import Card
from player import Player
'''
Style Note:
according to convention, all imports should be done at the top of the file in the following order: standard library modules, third-party modules, your own modules.  These should be in alphabetical order.  Remember that circular imports will cause errors.
Imports should always be as explicit as possible, using the from file import class syntax.
'''
deck1 = Deck()
deck1.shuffle()
my_card = deck1.deal()
print "my deck: "
deck1.show()
print "dealt card: ", my_card.show()

player1 = Player("Bob")
player1.hit(deck1).hit(deck1).hit(deck1).hit(deck1).show_hand()
player1.discard(0).show_hand()

print "after deal: "
deck1.show()

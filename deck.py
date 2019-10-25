class Deck:
    
	    def __init__(self):
		self.deck = []
		for suit in suits:
		    for rank in ranks:
			card = Card(suit,rank)
			self.deck.append(card)
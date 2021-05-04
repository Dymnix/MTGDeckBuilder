####################################################
#               deckCard Class                     #
####################################################

#This class represents a card slot in the decklist
class deckCard:

    #constructor
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    #returns the name of the card as a string
    def getName(self):
        return self.name

    #returns the quantity of the card as an integer
    def getQuantity(self):
        return str(self.quantity)



####################################################
#               result Class                       #
####################################################

class result:

    #constructor
    def __init__(self, name, image):
        self.name = name
        self.image = image

    def getName(self):
        return self.name

    def getImage(self):
        return self.image
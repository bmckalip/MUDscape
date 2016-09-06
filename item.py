class Item(object):

    def __init__(self, name, quantity, stackable = False, noted = False):
        self.name = name
        self.quantity = quantity
        self.stackable = stackable
        self.noted = noted

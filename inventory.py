from item import Item

class Inventory(object):

    def __init__(self):
        self.max_capacity = 28
        self.occupied_slots = 0
        self.items = []

    def addItem(self, item):

        if self.occupied_slots < self.max_capacity and (item.stackable or item.noted):
            self.items.append(item)
            self.occupied_slots += 1

        elif self.occupied_slots + item.quantity <= self.max_capacity:
            while item.quantity >= 1: #We loop and add them as individual items as they are not stackable
                temp_item = Item(item.name, 1)
                self.items.append(temp_item)
                self.occupied_slots += 1
                item.quantity -= 1

    def showInventory(self):

        print( "")
        print( "*** INVENTORY {}/{} ***".format(self.occupied_slots, self.max_capacity))
        for item in self.items:
            if(item.stackable):
                print("- {}[{}]".format(item.name, item.quantity))
            else:
                print("- {}".format(item.name))
        print( "")

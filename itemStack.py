class ItemStack:
    def __init__(self, itemID, quantity=1):
        self.itemID = itemID
        self.quantity = quantity

    def combine(self, other):
        if type(other) is ItemStack:
            if self.itemID == other.itemID:
                self.quantity += other.quantity
        return self


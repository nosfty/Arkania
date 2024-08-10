class Slot:
    def __init__(self, contain_item:Item = None) -> None:
        self.contain_item = contain_item


class Inventory:

    def __init__(self) -> None:
        self.filled_slots = 0
        self.max_slots = 0

        self.inventory = []
        for _ in range(30):
            self.inventory.append(Slot)
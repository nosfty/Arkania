from _items import _resource_item, Item, ResourceItem, ToolItem, MeleeItem

class Slot:
    def __init__(self, contain_item = None) -> None:
        self.contain_item = contain_item


class Inventory:

    def __init__(self) -> None:
        self.filled_slots = 0
        self.max_slots = 30

        self.inventory = []

        for i in range(self.max_slots):
            self.inventory.append(Slot(Item(None, "Empty", None)))


    def Get_Filled(self) -> int:
        self.filled_slots = 0
        for i in range(len(self.inventory)):
            print(i)
            if self.inventory[i].contain_item.rarity is not None:
                self.filled_slots += 1

        return self.filled_slots


    def Get_INV_DEBUG(self) -> list:
        temp_ls = []
        for i in range(len(self.inventory)):
            temp_ls.append(self.inventory[i].contain_item.name)
        return temp_ls



    def Craft(self, Recipe:list) -> str:

        Filled = self.Get_Filled()
        ObjMem = []

        item_for = None

        if Filled < len(self.inventory):
            for i in range(len(Recipe)):
                for j in range(len(self.inventory) - (len(self.inventory) - self.Get_Filled())):
                    if self.inventory[j].contain_item.name == Recipe[i]:
                        ObjMem.append(self.inventory[j])
                        self.inventory[j] = Slot(Item(None, "Empty", None))
                        break

            if len(ObjMem) != len(Recipe):
                for t in range(len(ObjMem)):
                    for n in range(len(self.inventory)):
                        if self.inventory[n].contain_item.name == "Empty":
                            self.inventory[n] = ObjMem[t]
                            break
                return "You dont have enough resources"


            else:
                for i in range(len(_resource_item)):
                    if Recipe == _resource_item[i].recipe:
                        item_for = _resource_item[i]
                        break

                if item_for is not None:
                    self.inventory[self.Get_Filled()].contain_item = item_for

                    return f"{item_for.name} Succesfully created!"

                else:
                    for t in range(len(ObjMem)):
                        for n in range(len(self.inventory)):
                            if self.inventory[n].contain_item.name == "Empty":
                                self.inventory[n] = ObjMem[t]
                                break
                    return "Unknown Recipe"
        else:
            return "Your inventory is Full!"





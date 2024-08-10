class Item:
    def __init__(self, Recipe:list, Name:str, Rarity:str) -> None:
        self.recipe = Recipe
        self.name = Name
        self.rarity = Rarity



class ResourceItem(Item):
    def __init__(self, Recipe:list, Name:str, Rarity:str, type:str) -> None:
        Item.__init__(self, Recipe, Name, Rarity)
        self.type = type




class MeleeItem(Item):
    def __init__(self, Recipe: list, Name:str, Rarity: str, enchant:str, damage:int) -> None:
        Item.__init__(self, Recipe, Name, Rarity)
        self.enchant = enchant
        self.damage = damage


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





class Races:
    
    # : Like Humans, Dwarves, Elfs, Draconits, TikTok Gnomes and of course Quadrobers

    def __init__(self, RaceName:str, CanUseMagic:bool, Stamina:int, Hp:int, Strength:int, Wisdom:int, Charisma:int):
        self.RaceName = RaceName
        self.CanUseMagic = CanUseMagic
        self.Stamina = Stamina
        self.Hp = Hp
        self.Strength = Strength
        self.Wisdom = Wisdom
        self.Charima = Charisma



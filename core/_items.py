

class Item:
    def __init__(self, Recipe:list, Name:str, Rarity:str) -> None:
        self.recipe = Recipe
        self.name = Name
        self.rarity = Rarity



class ResourceItem(Item):
    def __init__(self, Recipe:list, Name:str, Rarity:str, type:str) -> None:
        Item.__init__(self, Recipe, Name, Rarity)
        self.type = type


class ToolItem(Item):
    def __init__(self, Recipe: list, Name:str, Rarity: str, enchant:str, durability:int, effective:int) -> None:
        Item.__init__(self, Recipe, Name, Rarity)
        self.enchant = enchant
        self.durability = durability
        self.Effective = effective


class MeleeItem(Item):
    def __init__(self, Recipe: list, Name:str, Rarity: str, enchant:str, damage:int) -> None:
        Item.__init__(self, Recipe, Name, Rarity)
        self.enchant = enchant
        self.damage = damage



# : Items List

_resource_item = [
    ResourceItem(None, "Stick", "Common", "Wood"),
    ResourceItem(None, "Iron Ore", "Common", "Ore"),
    ToolItem(["Stick", "Iron Ore"], "Iron Shovel",  "Common", None, 12,12)
    ]



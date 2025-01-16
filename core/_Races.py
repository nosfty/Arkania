# : Like Humans, Dwarves, Elfs, Draconits, TikTok Gnomes and of course Quadrobers


class Races:
    # : Like Humans, Dwarves, Elfs, Draconits, TikTok Gnomes and of course Quadrobers
    def __init__(self, RaceName:str, CanUseMagic:bool, Stamina:int, Hp:int, Strength:int, Mana:int, Wisdom:int, Charisma:int):
        self.RaceName = RaceName
        self.CanUseMagic = CanUseMagic
        self.Stamina = Stamina
        self.Hp = Hp
        self.Strength = Strength
        self.Mana = Mana
        self.Wisdom = Wisdom
        self.Charima = Charisma



_Races = [
    Races("Human", True, 5, 6, 4, 5, 5, 5),
    Races("Draconian", True, 6, 7, 6, 6, 4, 4),
    Races("Sylph", True, 4, 5, 3, 7, 4, 4),
    Races("Golem", False, 8, 10, 7, 0, 1, 0),
    Races("Nymph", True, 2, 2, 3, 8, 7, 5),
    Races("Elf", True, 2, 3, 2, 9, 8, 7),
    Races("Centaur", False, 6,6,6,0,6,6),
    Races("Dwarf", False, 8,9,7,0,2,2)
]










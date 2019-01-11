import materials as matr

class Armor():
    
    def __init__(self, armor_type, material, name=None):
        self.armor_type = armor_type
        self.weight = Armor._weight_table[armor_type] * material.weight
        self.protection = self.weight 
        if name == None:
            self.name = f"{material.name} {armor_type}"
        else:
            self.name = name

    @property
    def damage(self):
        pass

    _weight_table = {
        "Gloves" : 2,
        "Boots" : 2,
        "Helmet" : 5,
        "Armor" : 10, 
    }
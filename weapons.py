import materials as matr

class Weapon():
    
    def __init__(self, weap_type, material, name=None):
        self.weap_type = weap_type
        self.weight = Weapon._weight_table[weap_type] * material.weight
        self.damage = 1.2 * self.weight 
        if name == None:
            self.name = f"{material.name} {weap_type}"
        else:
            self.name = name

    @property
    def damage(self):
        pass

    _weight_table = {
        "Dagger" : 2,
        "Sword" : 5,
        "Axe" : 6,
        "Hammer" : 8,
        "Mace" : 8,
        "Two-Handed Sword" : 12   
    }
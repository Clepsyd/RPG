class Material():
    '''Material class, instances apply modifiers to weapons and armors'''

    def __init__(self, name, tier=0):
        self.name = name
        self.tier = Material.tier_list[tier]
        self.att_mod = self.tier[0]
        self.def_mod = self.tier[1]
        self.durability = self.tier[2]
        self.value = self.tier[3]
        self.weight = Material._weight_table[self.name]

    #Modifiers used to create the tier_list
    att_mod = 1
    def_mod = 2
    durability = 100
    value = 5

    #tier_list parameters
    number_of_tiers = 5
    perct_incr = 20
    # Default tier list with base modifier values
    tier_list = [(att_mod, def_mod, durability, value)]

    @classmethod
    def create_tiers(cls, number_of_tiers, perct_incr):
        '''Creates a list of 'number_of_tiers' quality tiers of materials in ascending order (attack modifer, defense modifier, durability, value)
        Each successive tier is modified linearly by increasing each attribute by 'perct_incr'% of its original value.'''
        tiers = []
        tier = cls.tier_list[0]
        for x in range(number_of_tiers):
            modifier = (1 + x/(100/perct_incr))
            new_tier = tuple([attribute * modifier for attribute in tier])
            tiers.append(new_tier)
        cls.tier_list = tiers

    _weight_table = {
        "Wood" : 1.2,
        "Stone" : 1.5,
        "Iron" : 1.6,
        "Steel" : 1.7,
        "Tempered Steel" : 1.7 
    } 

Material.create_tiers(Material.number_of_tiers, Material.perct_incr)
wood = Material("Wood")
stone = Material("Stone", 1)
iron = Material("Iron", 2)
steel = Material("Steel", 3)    
tempered_steel = Material("Tempered Steel", 4)

__author__ = 'kate'



class Hero():

    def __init__(self, name, gender, nclass, type, hitpoints, attack, defence, armour, mana, carry_weight):

        self.name=name
        self.gender=gender
        self.nclass=nclass
        self.type=type
        self.hitpoints=hitpoints
        self.attack=attack
        self.defence=defence
        self.armour=armour
        self.mana=mana
        self.carry_weight=carry_weight
        self.pack = []
        self.current_carry_weight = 0
        self.equipped= {'head': None,
                        'neck': None,
                        'chest': None,
                        'legs': None,
                        'right hand': None,
                        'left hand': None,
                        'hands': None,
                        'wrists': None,
                        'feet': None,
                        'tail': None}


    def pick_up(self, item):
        if self.current_carry_weight + item.weight <= self.carry_weight:
            self.pack.append(item)
            self.current_carry_weight += item.weight
        else:
            print('sorry its too heavy')

    def drop_item(self, item):
        self.current_carry_weight -=item.weight
        self.pack.remove(item)

    def equip(self, item):
        self.equipped[item.body_location]=item
        print('{0} has equipped a {1}'.format(self.name, item.name))
        self.pack.remove(item)
        self.current_carry_weight-=item.weight


    def __repr__(self):
        return '{0} the {1} {2}'.format(self.name, self.type, self.nclass)



Main_Character = Hero('Harry', 'Male', 'Chinchilla', 'Ninja', 10, 10, 10, 20, 0, 20)

print(Main_Character,'the', Main_Character.type, Main_Character.nclass)



class Item():

    def __init__(self, name, type, location, attack_value, defence, weight, value):

        self.name=name
        self.type=type
        self.attack_value=attack_value
        self.weight=weight
        self.value=value
        self.armour_rating=defence
        self.body_location=location

    def __repr__(self):

        return '{0}'.format(self.name)

food = Item('monkey nut', 'food', None, 0, 0, 1, 1)

weapon = Item('sword', 'weapon', 'right hand', 2, 0, 2, 30)

armour = Item ('breast plate', 'armour', 'chest', 0, 5, 8, 10)

Main_Character.pick_up(food)
print(Main_Character.pack, Main_Character.current_carry_weight)
Main_Character.pick_up(food)
print(Main_Character.pack, Main_Character.current_carry_weight)
Main_Character.pick_up(food)
print(Main_Character.pack, Main_Character.current_carry_weight)

Main_Character.drop_item(food)
print(Main_Character.pack, Main_Character.current_carry_weight)

Main_Character.pick_up(weapon)
print(Main_Character.pack, Main_Character.current_carry_weight)

Main_Character.pick_up(armour)
print(Main_Character.pack, Main_Character.current_carry_weight)

print(Main_Character.equipped['chest'])
Main_Character.equip(armour)
print(Main_Character.equipped['chest'])

print(Main_Character.equipped['right hand'])
Main_Character.equip(weapon)
print(Main_Character.equipped['right hand'])

print(Main_Character.pack, Main_Character.current_carry_weight)
__author__ = 'Daniel'


class Hero():

    def __init__(self, name, profession, gender):
        self.name = name
        self.profession = profession
        self.gender = gender
        self.health = 100
        self.strength = 10
        self.defence = 10
        self.armour = 0
        self.attack = 1
        self.damage = 2
        self.max_carry_weight = 5 * self.strength
        self.current_weight = 0
        self.pack_size = 2
        self.equipped_items = {'head': None,
                               'clock': None,
                               'chest':None,
                               'belt': None,
                               'neck': None,
                               'legs': None,
                               'hands': None,
                               'wrists': None,
                               'feet': None,
                               'right_hand': None,
                               'left_hand': None,
                               'left_ring': None,
                               'right_ring': None,
                               'pack': None}

        self.pack = []

    def pick_up_item(self, item):
        if len(self.pack) >= self.pack_size:
            print('{0} can not add {1} to his pack not enough space'.format(self.name, item))
            return
        if (item.weight + self.current_weight) > self.max_carry_weight:
            print('{0} can not carry {1}, its too heavy'.format(self.name, item))
            return
        self.pack.append(item)
        self.current_weight = self.current_weight.__add__(item.weight)



    def __str__(self):
        if self.gender == 'male':
            gen = ['his', 'he']
        else:
            gen = ['her', 'she']
        return '{0} has {1} health\n'.format(self.name, self.health) + '{0} defence is {1} and attack is {2}\n'.format(gen[0], self.defence, self.attack) + '{0} is carrying {1} items in {3} pack that weighs {2}kg\n'.format(gen[1], len(self.pack), self.current_weight, gen[0])

class Item():

    def __init__(self, name, weight):

        self.name = name
        self.weight = weight

if __name__ == "__main__":

    hero = Hero('kate', 'ninja', 'female')

    print(hero)

    sword = Item('broad sword', 5)
    hero.pick_up_item(sword)

    print(hero)
    #hero.pick_up_item(sword)



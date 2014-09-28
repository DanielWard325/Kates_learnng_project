__author__ = 'Daniel'

from examples import Hero, Item


hero = Hero('kate', 'nurse', 'female')
breast_plate = Item('breast_plate', 30, 'chest')
shirt = Item('cloth_shirt', 2, 'chest')
print(hero)

hero.pick_up_item(breast_plate)

print(hero)
print(hero.pack)

hero.equip_item(breast_plate)

print(hero)

hero.pick_up_item(shirt)

print(hero)
print(hero.pack)

hero.equip_item(shirt)

print(hero)
print(hero.pack)
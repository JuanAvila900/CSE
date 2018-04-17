class Item(object):
    def __init__(self, name):
        self.name = name

    def name(self):
        print("You got a %s" % self.name)


class Weapon(Item):
    def __init__(self, name, Weight, skill, description):
        super(Weapon, self).__init__(name)
        self.Weight = Weight
        self.skill = skill
        self.description = description

    def Weight(self):
        print("It weighs in at 50.5")

    def ability(self):
        print("Ability 'Rage' activated")

    def description(self):
        print("You Got a %s!  Now you can start fighting off monsters!!" % self.name)


class Sword(Weapon):
    def __init__(self, name, skill, weight, description):
        super(Sword, self).__init__('Sword', description, skill, weight)
        

class Bow(Weapon):
    def __init__(self, name, skill, Weight, description):
        super(Bow, self).__init__('Bow', skill, Weight, description)


class SilverSword(Weapon):
    def __init__(self, name, skill, Weight, description):
        super(SilverSword, self).__init__('Silver Sword', description, skill, Weight)
        
    
class HpSword(Weapon):
    def __init__(self, name, skill, Weight, description):
        super(HpSword, self).__init__(' Hp Sword', description, skill, Weight)
        
        
class Xbow(Weapon):
    def __init__(self, name, skill, weight, description):
        super(Xbow, self).__init__('Xbow', description, skill, weight)


class Bombs(Weapon):
    def __init__(self, name, skill, weight, description):
        super(Bombs, self).__init__('Bombs', description, skill, weight)


class CrystalSword(Weapon):
    def __init__(self, name, skill, weight, description):
        super(CrystalSword, self).__init__('CrystalSword', description, skill, weight)


class ManaSword(Weapon):
    def __init__(self, name, skill, weight, description):
        super(ManaSword, self).__init__('ManaSword', description, skill, weight)




class consumable(Item):
    def __init__(self, name, description, effect):
        super(consumable, self).__init__(name)
        self.description = description
        self.effect = effect


    def description(self):
        print("This is a %s. Use it wisely. Lel." % self.name)

    def effect(self):
        print("This %s that you got has an effect!" % self.name)


class Potion(consumable):
    def __init__(self, name, description, effect):
        super(Potion, self).__init__('Potion', description, effect)


class HealthPotion(Potion):
    def __init__(self, name, description, effect):
        super(HealthPotion, self).__init__('Health Potion',description, effect)


class ManaPotion(Potion):
    def __init__(self, name, weight, description, effect):
        super(ManaPotion, self).__init__('ManaPotion', description, effect)


class RevivePotion(Potion):
    def __init__(self, name, weight, description, effect):
        super(RevivePotion, self).__init__('Revive Potion', description, effect)


class PoisonPotion(Potion):
    def __init__(self, name, description, effect):
        super(PoisonPotion, self).__init__('Poison Potion', description, effect)


class Food(consumable):
    def __init__(self, name, description, effect):
        super(Food, self).__init__('Food', description, effect)


class soup(Food):
    def __init__(self, name, description, effect):
        super(soup, self).__init__('soup', description, effect)


class oldhamburger(Food):
    def __init__(self, name, description, effect):
        super(oldhamburger, self).__init__('Old hamburger', description, effect)


class Orangechicken(Food):
    def __init__(self, name, description, effect):
        super(Orangechicken, self).__init__('Orange Chicken', description, effect)


class Clothing(consumable):
    def __init__(self, name, description, effect):
        super(Clothing, self).__init__(name, description, effect)


class Nikeshoes(Clothing):
    def __init__(self, name, description, effect):
        super(Nikeshoes, self).__init__('Nikeshoes', description, effect)


class LevisPants(Clothing):
    def __init__(self, name, description, effect):
        super(LevisPants, self).__init__('Levis Pants', description, effect)


class HolisterShirt(Clothing):
    def __init__(self, name, description, effect):
        super(HolisterShirt, self).__init__('Holister shirt', description, effect)

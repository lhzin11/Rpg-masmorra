class Item:
    def __init__(self, name):
        self.name = name

    def use(self, player):
        pass

class HealthPotion(Item):
    def __init__(self):
        super().__init__("Poção de Saúde")

    def use(self, player):
        player.health += 20
        print("Você usou uma Poção de Saúde. Saúde aumentada em 20.")

class PowerBoost(Item):
    def __init__(self):
        super().__init__("Aumento de Poder")

    def use(self, player):
        player.attack_power += 5
        print("Você usou um Aumento de Poder. Poder de ataque aumentado em 5.")

class Armor(Item):
    def __init__(self):
        super().__init__("Armadura")

    def use(self, player):
        player.health += 10
        print("Você usou uma Armadura. Saúde aumentada em 10.")

class Weapon(Item):
    def __init__(self):
        super().__init__("Arma")

    def use(self, player):
        player.attack_power += 10
        print("Você usou uma Arma. Poder de ataque aumentado em 10.")

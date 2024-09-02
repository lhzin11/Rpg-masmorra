class Enemy:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self):
        return self.attack_power

    def take_damage(self, damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0

class Goblins(Enemy):
    def __init__(self):
        super().__init__("Goblins", 30, 5)

class Orc(Enemy):
    def __init__(self):
        super().__init__("Orc", 50, 10)

class Golem(Enemy):
    def __init__(self):
        super().__init__("Golem", 100, 15)

class Mage(Enemy):
    def __init__(self):
        super().__init__("Mago", 40, 12)

class Witch(Enemy):
    def __init__(self):
        super().__init__("Bruxa", 60, 8)

class Troll(Enemy):
    def __init__(self):
        super().__init__("Troll", 80, 10)

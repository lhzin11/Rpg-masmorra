from enemy import Orc, Mage, Goblins, Golem, Witch, Troll
from item import HealthPotion, PowerBoost, Armor, Weapon, Item
import random

class Dungeon:
    def __init__(self, player):
        self.player = player
        self.level = 1
        self.rooms = ["Sala Vazia", "Sala do Tesouro", "Sala do Monstro"]
        self.current_room = random.choice(self.rooms)
    
    def display_room(self):
        print(f"Você está na {self.current_room}")
    
    def explore(self):
        self.current_room = random.choice(self.rooms)
        print(f"Você explora e encontra: {self.current_room}")
        if self.current_room == "Sala do Tesouro":
            item = self.generate_item()
            self.player.add_item(item)
            print(f"Você encontrou um {item.name}!")
        elif self.current_room == "Sala Vazia":
            if random.random() < 0.5:  # 50% chance to find an item
                item = self.generate_item()
                self.player.add_item(item)
                print(f"Você encontrou um {item.name}!")

    def fight(self):
        if self.current_room == "Sala do Monstro":
            enemy = self.generate_enemy()
            while enemy.is_alive() and self.player.is_alive():
                action = input("Você quer (atacar/correr/usar item): ").lower()
                if action == "atacar":
                    enemy.take_damage(self.player.attack())
                    print(f"Você atacou o {enemy.name}!")
                    if enemy.is_alive():
                        self.player.take_damage(enemy.attack())
                        print(f"O {enemy.name} te atacou!")
                    else:
                        print(f"Você derrotou o {enemy.name}!")
                        self.level_up()
                elif action == "correr":
                    print("Você fugiu da batalha!")
                    break
                elif action == "usar item":
                    self.player.use_item()
                else:
                    print("Ação inválida!")
                self.player.display_status()
        else:
            print("Não há nada para lutar aqui.")
    
    def generate_enemy(self):
        enemies = [Goblins(), Orc(), Golem(), Mage(), Witch(), Troll()]
        return random.choice(enemies)

    def generate_item(self):
        items = [HealthPotion(), PowerBoost(), Armor(), Weapon()]
        return random.choice(items)
    
    def level_up(self):
        self.level += 1
        print(f"Você avançou para o nível {self.level}!")

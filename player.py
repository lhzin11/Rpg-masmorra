class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20  # Valor inicial de dano ajustado para 20
        self.inventory = []

    def attack(self):
        return self.attack_power

    def take_damage(self, damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0

    def add_item(self, item):
        self.inventory.append(item)

    def display_status(self):
        print(f"{self.name} - HP: {self.health}, Attack Power: {self.attack_power}")

    def use_item(self):
        if not self.inventory:
            print("Você não tem itens no inventário.")
            return

        print("Itens disponíveis:")
        for i, item in enumerate(self.inventory):
            print(f"{i + 1}. {item.name}")

        choice = input("Escolha o número do item que deseja usar: ")
        try:
            choice_idx = int(choice) - 1
            if 0 <= choice_idx < len(self.inventory):
                item = self.inventory.pop(choice_idx)
                item.use(self)
            else:
                print("Escolha inválida.")
        except ValueError:
            print("Escolha inválida.")

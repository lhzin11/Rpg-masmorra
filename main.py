from player import Player
from dungeon import Dungeon

def main():
    print("Bem-vindo ao RPG Dungeon!")
    player_name = input("Digite o nome do seu personagem: ")
    player = Player(player_name)
    
    dungeon = Dungeon(player)
    
    while player.is_alive():
        dungeon.display_room()
        command = input("O que você quer fazer? (explorar/lutar/sair): ").lower()
        
        if command == "explorar":
            dungeon.explore()
        elif command == "lutar":
            dungeon.fight()
        elif command == "sair":
            print("Saindo do jogo...")
            break
        else:
            print("Comando inválido!")
        
        if command == "usar":
            player.use_item()

        if dungeon.level >= 2:
            dungeon.level_up()

    if not player.is_alive():
        print("Você morreu! Game over.")

if __name__ == "__main__":
    main()

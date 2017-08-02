from collections import OrderedDict
from player import Player
import world

def play():
    print("Escape from Cave Terror!")
    player = Player()
    
    while True:
        room = world.tile_at(player.x, player.y)
        print(room.intro_text())
        room.modify_player(player)
        
        action_input = get_player_command()
        if action_input in ['n','N','s','S','e','E','w','W']:
            player.move_cardinal(action_input)
        elif action_input in ['i','I']:
            player.print_inventory()
        elif action_input in ['a','A']:
            player.attack()
        elif action_input in ['h','H']:
            player.heal()
        else:
            print("Invalid Action!")

def get_player_command():
    return input('Action: ')

def get_available_actions(room, player):
    actions = OrderedDict()
    print("Choose an action: ")
    if player.inventory:
        action_adder(actions, 'i', player.print_inventory)
    if isinstance(room, world.EnemyTile) and room.enemy.is_alive():
        

play()

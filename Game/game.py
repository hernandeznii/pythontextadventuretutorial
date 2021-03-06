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
        choose_action(room, player)

def choose_action(room, player):
    action = None
    while not action:
        available_actions = get_available_actions(room, player)
        action_input = input("Action: ")
        action = available_actions.get(action_input)
        if action:
            action()
        else:
            print("Invalid Action!")

def get_available_actions(room, player):
    actions = OrderedDict()
    print('You are now at ({},{})'.format(player.x, player.y))
    print("Choose an action: ")
    if player.inventory:
        action_adder(actions, 'i', player.print_inventory, "Print Inventory")
    if isinstance(room, world.EnemyTile) and room.enemy.is_alive():
        action_adder(actions,'a', player.attack, "Attack")
    else:
        if world.tile_at(room.x, room.y - 1):
            action_adder(actions, 'n', player.move_north, "Go North")
        if world.tile_at(room.x, room.y + 1):
            action_adder(actions, 's', player.move_south, "Go South")
        if world.tile_at(room.x - 1, room.y):
            action_adder(actions, 'w', player.move_west, "Go West")
        if world.tile_at(room.x + 1, room.y):
            action_adder(actions, 'e', player.move_east, "Go East")
    if player.hp < player.max_hp:
        action_adder(actions, 'h', player.heal, "Heal")

    return actions

def action_adder(action_dict, hotkey, action, name):
    action_dict[hotkey.lower()] = action
    action_dict[hotkey.upper()] = action
    print("{}: {}".format(hotkey, name))

play()

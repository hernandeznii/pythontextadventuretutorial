import items
import world


class Player:
    def __init__(self):
        self.inventory = [items.Rock() , items.Dagger(),'Gold(5)',items.CrustyBread(),'Bready Crust', items.Lucky_Charm()]
        self.x = 1
        self.y = 2
        self.hp = 100
        self.max_hp = 100
    
    def print_inventory(self):
        print("Inventory:")
        for items in inventory:
            print('* ' + str(items))
        best_weapon = self.most_powerful_weapon()
        print("Your best weapoin is your {}".format(best_weapon))
        
    def heal(self):
        consumables = [item for item in self.inventory if isinstance(item,items.Consumable)]
        if not consumables:
            print("You don’t have any items to heal you!")
            return
        for i, item in enumerate(consumables,1):
            print("Choose your healing item: ")
            print("{}. {}".format(i,item))
            
            valid = False
            while not valid:
                choice = input("")
                try:
                    to_eat = consumables[int(choice) - 1]
                    self.hp = min(self.max_hp, self.hp + to_eat.healing_value)
                    self.inventory.remove(to_eat)
                    print("Current HP: {}".format(self.hp))
                    valid = True
                except (ValueError, IndexError):
                    print("You can’t use that, try again.")
        
    def most_powerful_weapon(self):
        max_damage = 0
        best_weapon = None
        for item in self.inventory:
            try:
                if item.damage > max_damage:
                    best_weapon = item
                    max_damage = item.damage
            except AttributeError:
                pass
        return best_weapon
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        
    def move_cardinal(self,direction):
        if direction in ['n','N']:
            self.move(dx=0, dy=-1)
        elif direction in ['s','S']:
            self.move(dx=0, dy=1)
        elif direction in ['e','E']:
            self.move(dx=1, dy=0)
        elif direction in ['w','W']:
            self.move(dx=-1, dy=0)
        else:
            self.move(dx=0, dy=0)
    
    def attack(self):
        best_weapon = self.most_powerful_weapon()
        room = world.tile_at(self.x,self.y)
        enemy = room.enemy
        print("You use {} against {}!".format(best_weapon.name, enemy.name))
        enemy.hp -= best_weapon.damage
        if not enemy.is_alive():
            print("You killed the {}!".format(enemy.name))
        else:
            print("You dealt {} damage to {}; its HP is now {}.".format(best_weapon.damage,enemy.name, enemy.hp))

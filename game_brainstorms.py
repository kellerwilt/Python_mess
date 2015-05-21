import locale
class player:
    def __init__(self, inventory,name,skills,level,health,quests):
        self.inventory = inventory
        self.name      = name
        self.skills    = skills
        self.level     = level
        self.health    = health
        self.quests    = quests
    def check_inventory(self,inventory):
        print 'm:misc'
        print 'w:weapons'
        print 'f:food/potions'
        print 'c:clothing/armour'
        print 'r:resources'
        category = raw_input().upper
        if category == 'm':
            for item in inventory.misc:
                print inventory.misc.index(item),
                print item
            print 'c close'
            print 'b back to categories'
            print 'n next page'
            print 'p previous page'
            item = raw_input()
            if item == 'c':
                return None
    def get_item(self,inventory,item):
        category = item.category
        if category == 'm':
            self.inventory.misc.append(item)
            print 
        if category == 'w':
            self.inventory.weapons.append(item)
        if category == 'f':
            self.inventory.food.append(item)
        if category == 'c':
            self.inventory.clothing.append(item)
        if category == 'r':
            self.inventory.resources.append(item)
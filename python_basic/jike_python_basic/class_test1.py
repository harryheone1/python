# requirement version 1:
# Player with name and hp, could print its name and hp

# requirement version 2:
# A new class Monster, not sure about functionality yet.
# A new attribute 'Occupation' of player, print his occupation with other
# attribute name need to be 封装, only one method could modify

# Imperative paradism
player1 = {'name': 'Tom', 'hp': 100}
player2 = {'name': 'Jerry', 'hp': 80}


def print_role(role):
    print('name is %s   , hp is %s' % (role['name'], role['hp']))


print_role(player1)
print_role(player2)


class Player():
    def __init__(self, name, hp, occu):
        self.__name = name
        self.hp = hp
        self.occupation = occu

    def print_role(self):
        print('name is %s   , hp is %s  , occupation is %s' %
              (self.__name, self.hp, self.occupation))

    def update_name(self, newname):
        if len(newname) > 0:
            self.__name = newname


class Monster():
    pass


player3 = Player('tom', 100, 'warrior')
player4 = Player('jerry', 80, 'magician')
player3.print_role()
print(player4)

monster1 = Monster()
print(monster1)
print(Monster)

# update hp is ok
player3.hp = 200
player3.print_role()

# update name by field should not work
player3.name = 'tom brother'
player3.print_role()

# update name by public method is ok
player3.update_name('tom brother')
player3.print_role()

# update name by public method with empty name should not work
player3.update_name('')
player3.print_role()

# requirement version 1:
# Player with name and hp, could print its name and hp

# requirement version 2:
# A new class Monster, not sure about functionality yet.
# A new attribute 'Occupation' of player, print his occupation with other
# attribute name need to be 封装, only one method could modify

# requirement version 3:
# A new class Monster, not sure about functionality yet.
# Two subclass of Monster, one is Animal, other is Boss
# One attribute is 'hp', Monster, Animal and Boss have different default value.
# One common method is run(), One overridden method is whoami()


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


class Monster:
    def __init__(self, hp=100):
        self.__hp = hp

    def run(self):
        print('I am running with hp %s' % self.__hp)

    def whoami(self):
        print("I am a Monster")


class Animal(Monster):
    def __init__(self, hp=20):
        super().__init__(hp)

    def whoami(self):
        print("I am a Animal")


class Boss(Monster):
    def __init__(self, hp=1000):
        super().__init__(hp)

    def whoami(self):
        print("I am a Boss")


monster1 = Monster()
monster1.run()
monster1.whoami()

monster2 = Animal()
monster2.run()
monster2.whoami()

monster3 = Animal(50)
monster3.run()
monster3.whoami()

monster4 = Boss()
monster4.run()
monster4.whoami()

# True, False, True, True
print(isinstance(monster4, Monster))
print(isinstance(monster1, Animal))
print(isinstance(monster1, object))
print(isinstance(monster3, object))

# player3 = Player('tom', 100, 'warrior')
# player4 = Player('jerry', 80, 'magician')
# player3.print_role()
# print(player4)
#
# monster1 = Monster()
# print(monster1)
# print(Monster)
#
# # update hp is ok
# player3.hp = 200
# player3.print_role()
#
# # update name by field should not work
# player3.name = 'tom brother'
# player3.print_role()
#
# # update name by public method is ok
# player3.update_name('tom brother')
# player3.print_role()
#
# # update name by public method with empty name should not work
# player3.update_name('')
# player3.print_role()

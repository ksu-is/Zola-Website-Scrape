import random

class Pet:

    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.direction = 0
        self.health = 10
        self.fight = random.randint(0, 8)
        self.is_alive = True

    def eat(self):
        if self.is_alive:
            print(self.name + " goes 'Nom Nom Nom...'")
        else:
            print("Dis boi ded.")

    def sleep(self):
        if self.is_alive:
            print("zzzzzzzzzzzzzz...")
        else:
            print(self.name + " is in eternal sleep.")
            
    def play(self):
        if self.is_alive:
            print("Yippee!")
        else:
            print("Flips in casket!!")

    def rotate_right(self):
        self.direction += 1

        if self.direction == 4:
            self.direction = 0

    def rotate_left(self):
        self.direction -= 1

        if self.direction == -1:
            self.direction = 3

    def move(self):
        if self.direction == 0:
            self.y += 1
        elif self.direction == 1:
            self.x += 1
        elif self.direction == 2:
            self.y -= 1
        elif self.direction == 3:
            self.x -= 1

    def attack(self, other):
        if self.is_alive and other.is_alive:
            print(self.name + " and  " + other.name + " duel!")
            damage = (other.fight + random.randint(0,10)) - \
            (self.fight + random.randint(0,10))
            if damage > 0:
                self.health -= damage
                print(other.name + " beats up " + self.name + " for like " + \
                      str(damage) + " damage.")
                print(self.name + " health: " + str(self.health))
                print(other.name + " health: " + str(other.health))
            elif damage < 0:
                damage = damage * -1
                other.health -= damage
                print(self.name + " beats up " + other.name + " for like " + \
                      str(damage) + " damage.")
                print(self.name + " health: " + str(self.health))
                print(other.name + " health: " + str(other.health))
            else:
                print("After a long fight " + self.name + " and " + other.name + \
                      " decide to call it a draw.")
                print(self.name + " health: " + str(self.health))
                print(self.other + " health: " + str(other.health))

            if self.health <= 0:
                self.is_alive = False
                print(self.name + " is dead due to the wrath of " + other.name + ".")
            elif other.health <= 0:
                other.is_alive = False
                print(other.name + " is dead due to the wrath of " + self.name + ".")
        else:
            if not self.is_alive and not other.is_alive:
                print("Fam they both dead 100% let them die please.")
            elif not self.is_alive:
                print(self.name + " gets mutilated cause he is very much in the dead department right now by " + other.name + ".")
            elif not other.is_alive:
                print(other.name + " gets mutilated cause he is very much in the dead department right now by " + self.name + ".")
    

    def __repr__(self):
        return "Name: " + self.name + \
               " [x=" + str(self.x) + \
               ", y=" + str(self.y) + \
               ", d=" + str(self.direction) + "]"
    
    
pet1 = Pet("Jaden")
pet2 = Pet("Coop Dogg")
pet3 = Pet("Bob Ross")
print(pet1.name + " has an attack of " + str(pet1.fight) + ".")
print(pet2.name + " has an attack of " + str(pet2.fight)+ ".")
print(pet3.name + " has an attack of " + str(pet3.fight) + ".")

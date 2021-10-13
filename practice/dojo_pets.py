class Pet:
    def __init__( self, name, type, tricks ):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100

    def sleep(self, energy):
        self.pet.sleep += energy
        return self

    def eat(self, energy, health):
        self.pet.eat += energy + health
        return self

    def play(self, health):
        self.pet.play += health
        return self

    def noise(self):
        self.pet.noise = ("")
        return self


    def display_activity(self):
        print(f"{self.name}'s current activity is{self.pet.display_pet_info()}.")
        return self


class Ninja:
    def __init__( self, first_name, last_name, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = Pet( self, "yomi", "cat", "distance_leap")

    def walk(self, play):
        self.pet.walk = play
        return self

    def feed(self, eat):
        self.pet.feed = eat
        return self

    def bathe(self, noise):
        self.pet.bathe = noise
        return self

    def display_pet_info(self):
        return self.pet


yomi = Pet("yomi","cat", "distance_leap" )
darren = Ninja("darren", "f","salmon_skin","tuna")

yomi.sleep(25).eat(5+10).play(5).noise("rawwwwr")


print(yomi.display_activity())




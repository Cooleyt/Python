#chooses a random number each time you run the code.
# from random import randint 

# print(randint(1, 100)) 


#dice roller - get one number for each time you run the code
from random import randint

def roll_dice(number = 1, sides = 20, bonus= 0):
    #number and sides - xdy - 2d6 
    #bonus is added to the result of rollin t hose x dice

    result = bonus

    for x in range(0, number):
        result += randint(1, sides)


    return result 

print(roll_dice(sides = 6))


#new character
#   for stat in stats:
        # character[stat] = roll_dice(3, 6) 

def generate_character():
    #str, dex, con, int, wis, cha
    #3-18 - 3d6

    character = {
        'str': roll_dice(3, 6),
        'dex': roll_dice(3, 6),
        'con': roll_dice(3, 6),
        'int': roll_dice(3, 6),
        'wis': roll_dice(3, 6),
        'cha': roll_dice(3, 6)

    }

    return character

print(generate_character())
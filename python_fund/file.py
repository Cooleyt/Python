num1 = 42  #variable declaration
num2 = 2.3  #variable declaration
boolean = True  #log statement #Boolean
string = 'Hello World'
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']  #type check ,#Strings, #List
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}  #type check ,#Strings, #Dictionary
fruit = ('blueberry', 'strawberry', 'banana')  #type check , #Strings, #Tuples
print(type(fruit))  #type check, #Tuples
print(pizza_toppings[1]) #Tuples
pizza_toppings.append('Mushrooms') #Strings,#Tuples
print(person['name']) #Tuples
person['name'] = 'George' #Strings, #List
person['eye_color'] = 'blue' #Strings, #List
print(fruit[2]) #Tuples

if num1 > 45:  #Numbers, #conditional
    print("It's greater") #Tuples
else: #conditional
    print("It's lower") #Tuples

if len(string) < 5: #conditional
    print("It's a short word!") #Strings, #Tuples
elif len(string) > 15: #conditional
    print("It's a long word!") #Strings, #Tuples
else:
    print("Just right!") #String, #Tuples ,#conditional

for x in range(5):  #length check, #for loop
    print(x)
for x in range(2,5): #length check,#for loop
    print(x)
for x in range(2,10,3): #length check,#for loop
    print(x)
x = 0
while(x < 5): #Numbers, #while loop
    print(x)
    x += 1

pizza_toppings.pop()
pizza_toppings.pop(1)

print(person)
person.pop('eye_color') #Strings, #Tuples
print(person)

for topping in pizza_toppings: #for loop
    if topping == 'Pepperoni': #Strings, conditional 
        continue
    print('After 1st if statement') #Strings, #Tuples
    if topping == 'Olives': #Strings, conditional 
        break

def print_hello_ten_times():
    for num in range(10):  #length check
        print('Hello') #Strings

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):  #length check
        print('Hello') #Strings, #Tuples

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello') #Strings, #Tuples

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section  #comment
""" 

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)
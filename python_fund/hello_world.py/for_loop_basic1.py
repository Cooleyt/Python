#1. Print all integers from 0 to 150.

for x in range(0, 151, 1):
    print(x)

#2 Multiples of Five - Print all the multiples of 5 from 5 to 1,000

for x in range(5, 1001, 5):
    print(x)

#3. Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".

for x in range(1, 101):
    print(x)
    if x % 5:
        print ("Coding")

    if x % 10:
        print ("Coding Dojo")

#4. Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

for x in range(0, 5000001):
    Oddtotal = 0

for number in range(0, 5000000+1, 2):
    print("{0}".format(number))
    Oddtotal = Oddtotal + number

print("The Sum of Odd Numbers from 0 to{0} ={1}".format(number, Oddtotal))

#5. Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

for x in range(2018, 0, -4):
    if x > 0:
        print(x)

#6. Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

lowNum = 2
highNum = 9
multi = 3

for x in range(lowNum, highNum+1):
    if x % multi == 0:
        print(x)


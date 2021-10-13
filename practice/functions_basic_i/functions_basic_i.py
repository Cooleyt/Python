#1
# def number_of_food_groups():
#     return 5
# print(number_of_food_groups())
#5

# #2
# def number_of_military_branches():
#     return 5
# print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# it doesnt know the first value

# #3
# def number_of_books_on_hold():
#     return 5
#     return 10
# print(number_of_books_on_hold())
# 5 -because it will only run the first return statement

# #4
# def number_of_fingers():
#     return 5
#     print(10)
# print(number_of_fingers())
# 5 - because print is in the wrong place and only will read the second on that is not indented

# #5
# def number_of_great_lakes():
#     print(5)
# x = number_of_great_lakes()
# print(x)
# prints 5 and also none because the second print or x is empty

# #6
# def add(b,c):
#     print(b+c)
# print(add(1,2) + add(2,3))
# this wont print anything because python doesnt add that way

# #7
# def concatenate(b,c):
#     return str(b)+str(c)
# print(concatenate(2,5))
# this is linking the 2 and 5 to make 25

# #8
# def number_of_oceans_or_fingers_or_continents():
#     b = 100
#     print(b)
#     if b < 10:
#         return 5
#     else:
#         return 10
#     return 7
# print(number_of_oceans_or_fingers_or_continents())
# this will print 100 and 10 because the first print says to print b which is 100 and them since 10 is not greater than b, it returns 10 and prints that in the ()

# #9
# def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
# print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# this will print 7 14 and 21 because the first line to print is true, but the second line is not so it prints 14 and then it add the two for the third print to make 21

# #10
# def addition(b,c):
#     return b+c
#     return 10
# print(addition(3,5))
# this will print 8 because it says to return b+c which is 3+5 and it asks to print it as an addition. 


# #11
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
# print(b)
# foobar()
# print(b)
# this will print 500 500 300 and 500 because it says to print the first b which is 500, then it skips the foobar until it is called after the second b is called and then the last b is called.
# i am not 100% sure why or how it is being skipped tho.


# #12
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
#     return b
# print(b)
# foobar()
# print(b)
# this is the same as above except it is telling it to return instead of print, but it ends with the same result


# #13
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
#     return b
# print(b)
# b=foobar()
# print(b)
# this is will print 500 500 300 300 because b changes after it prints the second time


# #14
# def foo():
#     print(1)
#     bar()
#     print(2)
# def bar():
#     print(3)
# foo()
# this will print 1 3 2 because that is what is set to print on each line and it does so because nothing changes since the indents are there

# #15
# def foo():
#     print(1)
#     x = bar()
#     print(x)
#     return 10
# def bar():
#     print(3)
#     return 5
# y = foo()
# print(y)
# this will print 1 3 5 10 because of how it is set up to return, y here doesnt get printed i dont believe
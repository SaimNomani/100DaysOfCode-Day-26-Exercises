# In this list comprehension exercise you will practice using list comprehension to filter out the even numbers from a series of numbers.
#
# First, use list comprehension to convert the list_of_strings to a list of integers.
#
# Then use list comprehension again to create a new list called result. This new list should only contain the even numbers from the list numbers.
#
# Again, try to use Python's List Comprehension instead of a Loop.
#
# Example Input
# 9, 0, 32, 8, 2, 8, 64, 29, 42, 99
# Example Output
# [0, 32, 8, 2, 8, 64, 42]
numbers=input("enter list of numbers separated by comma: ").split(',')
numbers_int=[int(num) for num in numbers]
numbers_even=[num for num in numbers_int if num%2==0]
print(numbers_even)

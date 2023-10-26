# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
#
# You are going to create a list called result which contains the numbers that are common in both files.
#
# e.g. if file1.txt contained:
#
# 1
# 2
# 3
# and file2.txt contained:
#
# 2
# 3
# 4
# result = [2, 3]
# IMPORTANT: The output should be a list of integers and not strings! Try to use List Comprehension instead of a Loop.
#
# Example Output
# [3, 6, 5, 33, 12, 7, 42, 13]
with open('file1.txt') as file1:
    file1_contentent=file1.readlines()
    file1_numbers=[int(num) for num in file1_contentent]
with open('file2.txt') as file2:
    file2_contentent=file2.readlines()
    file2_numbers=[int(num) for num in file2_contentent]
common_nums=[num for num in file1_numbers if num in file2_numbers]
common_nums=list(set(common_nums))
print(common_nums)



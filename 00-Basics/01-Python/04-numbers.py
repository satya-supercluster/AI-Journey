x = int(input("Enter a number: "))  # Print table
for _ in range(1, 11):
    print(f"{x} * {_} = {x * _}")

# Enter a number: 3
# 3 * 1 = 3
# 3 * 2 = 6
# 3 * 3 = 9
# 3 * 4 = 12
# 3 * 5 = 15
# 3 * 6 = 18
# 3 * 7 = 21
# 3 * 8 = 24
# 3 * 9 = 27
# 3 * 10 = 30

###########################################

num = int(input("Enter a number: "))  # check whether number is palindrome or not
num_str = str(num)
n = len(num_str)
p = True
for index in range(0, n//2):
    if num_str[index] != num_str[n-1-index]:
        p = False
        break
print("Given number is " + ("Palindrome" if p else "Not Palindrome."))

# Enter a number: 121
# Given number is Palindrome

############################################

from math import *
my_num = 5.4
print(ceil(my_num))
print(floor(my_num))
print(pow(2, 3))
print(sqrt(my_num))
print(round(sqrt(my_num), 2))

# 6
# 5
# 8.0
# 2.32379000772445
# 2.32

friends = ["suyash", 31, 56.3]
for _ in friends:
    print(f"type({str(_)}): {type(_)}")

# type(suyash): <class 'str'>
# type(31): <class 'int'>
# type(56.3): <class 'float'>

####################################################

fruits: list[str] = ["Apple", "Banana", "Litchi"]
for index in range(0, len(fruits)):
    print(fruits[index])

# Apple
# Banana
# Litchi

###########################

print(fruits[1:])
# ['Banana', 'Litchi']

###########################

friends[1] = "kkk"
print(friends)
# ['suyash', 'kkk', 56.3]

######################################################

friends.extend(fruits)
fruits.append("Mango")
print(friends)
# ['suyash', 'kkk', 56.3, 'Apple', 'Banana', 'Litchi']

print(fruits)
# ['Apple', 'Banana', 'Litchi', 'Mango']

fruits.insert(-1, "Grapes")
print(fruits)
# ['Apple', 'Banana', 'Litchi', 'Grapes', 'Mango']

friends.pop()
print(friends)
# ['suyash', 'kkk', 56.3, 'Apple', 'Banana']

#######################################################


# read
file = open("10-data.txt", "r")
print(file.readable())
# True
print(file.readline())
# Hey, This is Satyam,
print(file.readlines())
# ['How are you?\n', "I'm Good,\n", 'What about you?\n', "I'm fine too."]
file.close()


###################################################################################


file = open("10-data.txt", "r")
print(file.read())
# ['How are you?\n', "I'm Good,\n", 'What about you?\n', "I'm fine too."]
# Hey, This is Satyam,
# How are you?
# I'm Good,
# What about you?
# I'm fine too.
file.close()


###################################################################################


# append
file = open("10-data.txt", "a")
file.write("\nConversation Closed!")
file.close()
# Hey, This is Satyam,
# How are you?
# I'm Good,
# What about you?
# I'm fine too.
# Conversation Closed!

###################################################################################


# write
file = open("10-data.txt", "w")
file.write("Hello World!")
# Hello World!
file.close()


###################################################################################


# read + write
file = open("10-data.txt", "r+")
print(file.read())
# Hello World!
file.close()


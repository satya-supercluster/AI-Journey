name = input("Enter your name: ")
print(f"Hello, {name}!")

# Enter your name: Satyam
# Hello, Satyam!

######################################################

age = input("Enter your age: ")
if age.isnumeric():
    age = int(age)
    print("Eligible" if age >= 18 else "Not Eligible")
else:
    print("Invalid Input")

# Enter your age: 20
# Eligible

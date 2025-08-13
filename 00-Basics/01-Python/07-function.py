def add(a: int, b: int):
    return a+b


print(add(5, 3))
# 8

##############################


def greet(name: str, age: int):
    verdict = "eligible" if age >= 18 else "ineligible"
    print(f"Hi {name}! You are {verdict}")


greet("Satyam", 20)
# Hi Satyam! You are eligible

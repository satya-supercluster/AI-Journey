try:
    a = int(input("Enter Number A: "))
    b = int(input("Enter Number B: "))
    c = a / b
    print(f"{a} / {b} = {c}")
except Exception as err:
    print(f"Error: {err}")
finally:
    print("Finished")

print("Ended")

# Enter Number A: 12
# Enter Number B: 0
# Error: division by zero
# Finished
# Ended

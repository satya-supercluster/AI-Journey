x=3
key="hello"
print("Hello\""+key+str(x))
print(f"Hello{key}{x}")
print(f"""Hello
{key[3].upper()}
{x}""")

print(key.isalnum())
print(key.endswith("."))
print(key.isupper())

# Hello"hello3
# Hellohello3
# Hello
# L
# 3
# True
# False
# False

##############################################

print("z: " + ("present" if "z" in key else "not present"))
# z: not present

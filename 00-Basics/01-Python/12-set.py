import random

data: list = []
st: set = set()

data = [(random.randint(0, 5)) for _ in range(10)]
for item in data:
    st.add(item)

print(f"List: {data}")
print(f"Set: {st}")
# List: [3, 3, 3, 3, 1, 1, 4, 4, 3, 1]
# Set: {1, 3, 4}

if 1 in st:
    print("Yes")
# Yes

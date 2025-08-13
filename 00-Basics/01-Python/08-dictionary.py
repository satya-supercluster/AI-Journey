monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions['Mar'])
# March

##################################################

import random

numbers = [random.randint(0, 10) for _ in range(0, 10)]

counts = {}
for item in numbers:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1

for key, value in counts.items():
    print(f"{key} -> {value}")
# 6 -> 1
# 1 -> 2
# 3 -> 5
# 0 -> 1
# 8 -> 1

for key in counts.keys():
    print(f"{key} -> {counts[key]}")
# 6 -> 1
# 1 -> 2
# 3 -> 5
# 0 -> 1
# 8 -> 1

for value in counts.values():
    print(value)
# 1
# 2
# 5
# 1
# 1

for index, (key, value) in enumerate(counts.items()):
    print(f"Index{index}. {key} -> {value}")
# Index0. 6 -> 1
# Index1. 1 -> 2
# Index2. 3 -> 5
# Index3. 0 -> 1
# Index4. 8 -> 1

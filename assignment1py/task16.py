data = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
frequency = {}
for item in data:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1
print("Frequencies:", frequency)

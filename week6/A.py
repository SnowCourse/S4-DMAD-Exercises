import random

def createRandomPermutation(n):
    numbers = list(range(n))
    random.shuffle(numbers)
    return numbers

def countCircles(permutation):
    circles = 0
    visited = set()
    index = 0
    while index < len(permutation):
        value = permutation[index]
        if (index not in visited):
            visited.add(index)
            index = value
        else:
            circles += 1
            while index in visited:
                index += 1
    return circles

# permutation = createRandomPermutation(10)
# circles = countCircles(permutation)
# print(f"\n{permutation}\nCircles: {circles}\n")
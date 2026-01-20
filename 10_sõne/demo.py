numbers = [1, 2, 3, 4, 5]

another_numbers = numbers

separate_numbers = numbers[:]

def plus_one(numbers: list[int]):
    result = numbers[:]
    for i in range(len(numbers)):
        numbers[i] += 1
    return result

print(numbers)
plus_one(numbers)
print(numbers)
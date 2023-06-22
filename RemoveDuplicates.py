numbers = [7, 1, 2, 7, 9, 16, 13, 0, 5, 2, 8, 9, 18, 3]
unique_numbers = []

for number in numbers:
    if numbers.count(number) == 1:
        unique_numbers.append(number)

print(unique_numbers)
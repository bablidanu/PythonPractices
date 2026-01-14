# Program to find the largest number in a list

numbers = [10, 25, 3, 99, 45]

largest = numbers[0]  # assuming first element is largest

for num in numbers:
    if num > largest:
        largest = num

print("Largest number is:", largest)
numbers = [12, 5, 27, 8, 14]


largest = numbers[0] # set your largest to the index of numbers
smallest = numbers[0]
total = 0 # set your total variable as zero

for num in numbers:
    total += num
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num

average = total / len(numbers)
print(f"Smallest:{smallest}")
print(f"Largest:{largest}")
print(f"Total:{total}")
print(f"Average:{average}")





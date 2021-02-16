numbers = input()
numbers = [int(n) for n in numbers]
ordered_numbers = sorted(numbers, reverse=True)

for i in ordered_numbers: 
    print(i, end="")
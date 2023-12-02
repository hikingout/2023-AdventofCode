# Import input.txt file as a list of strings
with open('input.txt', 'r') as file:
    puzzle = [line.strip() for line in file]

#Combine leftmost and rightmost numbers for each string in puzzle into an f-string
total = 0

for i in puzzle:
    left = next((num for num in i if num.isdigit()), None)
    right = next((num for num in reversed(i) if num.isdigit()), None)
    combined = int(f"{left}{right}")
    total += combined

print(total)

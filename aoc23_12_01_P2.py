# Import input.txt file as a list of strings
with open('prompts/day1_input.txt', 'r') as file:
    puzzle = [line.strip() for line in file]

total = 0

#Dictionary of possible numbers
number_dict = {"1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9", "0": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9", "zero": "0"}

def find_left_number(line, number_dict):
    for start_idx in range(len(line)):
        for end_idx in range(start_idx + 1, len(line) + 1):
            substring = line[start_idx:end_idx]
            if substring in number_dict:
                return number_dict[substring]
    return None

def find_right_number(line, number_dict):
    reversed_line = line[::-1]
    for start_idx in range(len(reversed_line)):
        for end_idx in range(start_idx + 1, len(reversed_line) + 1):
            substring = reversed_line[start_idx:end_idx]
            if substring[::-1] in number_dict: # Check the normal order of the substring in the dictionary
                return number_dict[substring[::-1]]
    return None

for line in puzzle:
    left = find_left_number(line, number_dict)
    right = find_right_number(line, number_dict)
    combined = int(f"{left}{right}")
    total += combined
    #print(combined)

print("Total:", total)

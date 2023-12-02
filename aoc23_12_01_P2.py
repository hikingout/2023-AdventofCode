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



# Open input file, save as puzzle
with open('prompts/day2_input.txt', 'r') as file:
    lines = [line.strip() for line in file]

# Initialize puzzle dictionary to store the games
puzzle = {}
check = {"red": 12, "green": 13, "blue": 14}

def create_puzzle(lines):
    # Process each line to extract game ID and rounds
    for line in lines:
        game_id, rounds_str = line.split(':')
        game_id = int(game_id.split(' ')[1])
        rounds = [round.strip() for round in rounds_str.split(';') if round]

        # Initialize dictionary for each game_id
        puzzle[game_id] = {'rounds': {}}

        for round_id, round in enumerate(rounds, start=1):  # Start round_id with 1
            color_dict = {}
            colors = round.split(',')
            for color in colors:
                quantity, color_name = color.strip().split(' ')
                color_dict[color_name] = int(quantity)

            # Assign the colors dictionary to the round_id key within the game dictionary
            puzzle[game_id]['rounds'][round_id] = color_dict

#Pretty print the puzzle dictionary
def print_puzzle(puzzle):
    for game_id, game in puzzle.items():
        print(f"Game: {game_id}")
        for round_id, round in game['rounds'].items():
            print(f"Round: {round_id}")
            for color, quantity in round.items():
                print(f"\t{color}: {quantity}")
        print("")

#Sum the game_ids of possible games
def impossible_games(puzzle):
    game_id_sum = 0
    for game_id, game in puzzle.items():
        for round_id, round in game['rounds'].items():
            if any(quantity > check[color] for color, quantity in round.items()):
                break 
        else: 
            game_id_sum += game_id 
    return game_id_sum

#Find the minimum # of each color required in the game
def minimum_cubes(puzzle):
    for game_id, game in puzzle.items():
        minimum_cubes = {"red": 0, "green": 0, "blue": 0}
        for round_id, round in game['rounds'].items():
            for color, quantity in round.items():
                if minimum_cubes[color] < quantity:
                    minimum_cubes[color] = quantity
        print(f"Game: {game_id} Minimum cubes: {minimum_cubes}")

create_puzzle(lines)
#game_id_sum = impossible_games(puzzle)
#print("The sum of all possible game IDs is: ", game_id_sum)

minimum_cubes(puzzle)
#Part 1
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

def impossible_games(puzzle):
    game_id_sum = 0
    for game_id, game in puzzle.items():
        for round_id, round in game['rounds'].items():
            if any(quantity > check[color] for color, quantity in round.items()):
                break 
        else: 
            game_id_sum += game_id 
    return game_id_sum

create_puzzle(lines)
game_id_sum = impossible_games(puzzle)
print("The sum of all possible game IDs is: ", game_id_sum)

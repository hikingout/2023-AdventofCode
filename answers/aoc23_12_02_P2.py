#Part 2
# Open input file, save as puzzle
with open('prompts/day2_input.txt', 'r') as file:
    lines = [line.strip() for line in file]

# Initialize puzzle dictionary to store the games
puzzle = {}

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

#Find the minimum # of each color required in the game
## Multiply the minimum colors for each game by one another to get a game power
## Add all the game powers to get a game power sum
def minimum_cubes(puzzle):
    game_id_power_sum = 0
    for game_id, game in puzzle.items():
        minimum_cubes = {"red": 0, "green": 0, "blue": 0}
        for round_id, round in game['rounds'].items():
            for color, quantity in round.items():
                if minimum_cubes[color] < quantity:
                    minimum_cubes[color] = quantity
        game_id_power = 1
        for color_quantity in minimum_cubes.values():
            game_id_power *= color_quantity
        game_id_power_sum += game_id_power
        #print("Game ID:", game_id, "Power:", game_id_power)
    
    return game_id_power_sum
        
create_puzzle(lines)

minimum_cubes(puzzle)
game_id_power_sum = minimum_cubes(puzzle)
print("The sum of all possible game IDs is: ", game_id_power_sum)
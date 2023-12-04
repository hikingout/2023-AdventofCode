#Part 1

# Open input file, save as puzzle
with open('prompts/day4_input.txt', 'r') as file:
    lines = [line.strip() for line in file]

puzzle = {}

#Create puzzle dictionary
def create_puzzle(lines):
    for line in lines:
        card_id, card = line.split(":")
        card_id = int(card_id.strip("Card ").strip(":"))
        winning_numbers = card.split("|")[0].strip().split(" ")
        card_numbers = card.split("|")[1].strip().split(" ")
        puzzle[card_id] = {"winning_numbers": winning_numbers,
                           "card_numbers": card_numbers}

#Count # of matching numbers between winning_numbers and card_numbers for each card
def winners_count(puzzle):
    total_score = 0
    for card_id in puzzle:
        winning_numbers = puzzle[card_id]["winning_numbers"]
        card_numbers = puzzle[card_id]["card_numbers"]
        card_matches = 0
        card_score = 0
        for number in winning_numbers:
            if number in card_numbers:
                card_matches += 1
            card_score = 2 ** (card_matches - 1) if card_matches > 0 else 0
        puzzle[card_id]["card_matches"] = card_matches
        puzzle[card_id]["card_score"] = card_score
        total_score += card_score
    return total_score
    

def print_puzzle(puzzle):
    for card_id in puzzle:
        print (f"Card Id: {card_id}")
        #print (f"{puzzle[card_id]['winning_numbers']}")
        #print (f"{puzzle[card_id]['card_numbers']}")
        print (f"{puzzle[card_id]['card_matches']}")
        print (f"{puzzle[card_id]['card_score']}")


create_puzzle(lines)
total_score = winners_count(puzzle)
#print_puzzle(puzzle)
print (f"Total score: {total_score}")

#Part 1
# I was on the struggle bus for this one. I have not worked with grids before. I heavily relied on AI for help to figure out how to work in grids with pseudo-code prompts.

# Open input file, save as puzzle
with open('prompts/day3_input.txt', 'r') as file:
    lines = [line.strip() for line in file]

#Convert lines into grid called puzzle
puzzle = [list(line) for line in lines]
#print(puzzle)

#Define all numbers in the grid as a dictionary, potential_parts{}, with their number as the key and the coordinates of all of their characters as values.
def potential_parts(puzzle):
    potential_parts_dict = {}
    rows = len(puzzle)
    cols = len(puzzle[0]) if puzzle else 0

    for y in range(rows):
        number = ''
        for x in range(cols):
            if puzzle[y][x].isdigit():
                number += puzzle[y][x]
            elif number:
                coord = (y, x - len(number))
                if number not in potential_parts_dict:
                    potential_parts_dict[number] = [coord]
                else:
                    if coord not in potential_parts_dict[number]:
                        potential_parts_dict[number].append(coord)
                number = ''
        if number:  # Catch any number that ends at the row's end
            coord = (y, cols - len(number))
            if number not in potential_parts_dict:
                potential_parts_dict[number] = [coord]
            else:
                if coord not in potential_parts_dict[number]:
                    potential_parts_dict[number].append(coord)

    return potential_parts_dict


#Find engine parts by searching the grid for symbols that are not "." or a digit. Next, check if they are horizontally, vertically, or diagonally adjacent to any of the coordinates for the corresponding numbers in potential_parts. If a symbol is adjacent add the corresponding number to engine_parts. 
def find_engine_parts(puzzle, potential_parts_dict):
    engine_parts = {}
    rows = len(puzzle)
    cols = len(puzzle[0]) if puzzle else 0

    # List of relative neighbor positions (8 directions)
    neighbors = [(-1, -1), (-1, 0), (-1, 1),
                 (0, -1),           (0, 1),
                 (1, -1), (1, 0), (1, 1)]

    for y in range(rows):
        for x in range(cols):
            if puzzle[y][x].isdigit() or puzzle[y][x] == '.':
                continue  # Skip if the character is a digit or a dot

            # Check all adjacent positions
            for dy, dx in neighbors:
                ny, nx = y + dy, x + dx
                # Confirm the neighbor position is within the grid
                if 0 <= ny < rows and 0 <= nx < cols:
                    # Look through all numbers in potential_parts_dict
                    for number, positions in potential_parts_dict.items():
                        for pos in positions:
                            py, px = pos
                            if ny == py and nx >= px and nx < px + len(number):
                                # Use coordinates as a key to prevent duplicates
                                if (py, px) not in engine_parts:
                                    engine_parts[(py, px)] = number
                                break  # Stop checking neighbors once part of the engine is found

    return list(engine_parts.values())

potential_parts_dict = potential_parts(puzzle)
#print(sorted(potential_parts_dict.keys(), reverse=True))
#    print(key, potential_parts_dict[key])

engine_parts = find_engine_parts(puzzle, potential_parts_dict)
#print(sorted(engine_parts, reverse=True))
parts_sum = sum(int(part) for part in engine_parts)
print(f" The sum is {parts_sum}")

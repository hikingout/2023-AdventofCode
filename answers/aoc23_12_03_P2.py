#Part 2
# I was on the struggle bus for this one. I have not worked with grids before. I heavily relied on AI for help to figure out how to work in grids with pseudo-code prompts.

# Open input file, save as puzzle
with open('prompts/day3_input.txt', 'r') as file:
    lines = [line.strip() for line in file]

#Convert lines into grid called puzzle
puzzle = [list(line) for line in lines]
neighbors = [(-1, -1), (-1, 0), (-1, 1),
             (0, -1),           (0, 1),
             (1, -1),  (1, 0),  (1, 1)]

#Define all numbers in the grid as a dictionary, potential_parts{}, with their number as the key and the coordinates of all of their characters as values.
def potential_parts(puzzle, neighbors):
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

#Find engine parts by searching the grid for symbols that are not "." or a digit. Next, check if they are horizontally, vertically, or diagonally adjacent to any of the coordinates in potential_parts. If a symbol is adjacent add the corresponding number to engine_parts. 
def find_engine_parts(puzzle, potential_parts_dict, neighbors):
    engine_parts = {}
    rows = len(puzzle)
    cols = len(puzzle[0]) if puzzle else 0

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
                                # Use coordinates as a key to store both the number and its coordinates
                                if number not in engine_parts:
                                    engine_parts[number] = {pos}
                                else:
                                    engine_parts[number].add(pos)
                                break  # Stop checking neighbors once a part of the engine is found

    # Convert sets to lists before returning
    for number in engine_parts:
        engine_parts[number] = list(engine_parts[number])

    return engine_parts

#Find gears by searching the grid for "*" symbols. Next, check if they are horizontally, vertically, or diagonally adjacent to any of the coordinates for engine_parts. If it is adjacent to exactly two part numbers, add the corresponding number to gears{} in this format to the gears dictionary: {gear_id: [part_number_1, part_number_2, gear_ratio]}.]}} gear_ratio = part_number_1 * part_number_2
def find_gears(puzzle, engine_parts, neighbors):
    gears = {}
    gear_id = 1
    rows = len(puzzle)
    cols = len(puzzle[0]) if puzzle else 0

    for y in range(rows):
        for x in range(cols):
            if puzzle[y][x] != '*':
                continue  # Skip if the character is not an asterisk

            # Check all adjacent positions
            adjacent_parts = set()
            for dy, dx in neighbors:
                ny, nx = y + dy, x + dx
                # Confirm the neighbor position is within the grid
                if 0 <= ny < rows and 0 <= nx < cols:
                    # Look through all engine parts to see if it's adjacent to any
                    for number, positions in engine_parts.items():
                        for pos in positions:
                            py, px = pos
                            if ny == py and nx >= px and nx < px + len(number):
                                adjacent_parts.add(number)

            # Verify that the asterisk is adjacent to exactly two part numbers
            if len(adjacent_parts) == 2:
                part_number_1, part_number_2 = adjacent_parts
                gear_ratio = int(part_number_1) * int(part_number_2)
                gears[gear_id] = [int(part_number_1), int(part_number_2), gear_ratio]
                gear_id += 1

    return gears


#Execute the code
potential_parts_dict = potential_parts(puzzle, neighbors) #
engine_parts = find_engine_parts(puzzle, potential_parts_dict, neighbors)
gears = find_gears(puzzle, engine_parts, neighbors)
gears_sum = sum(gear[2] for gear in gears.values())
print(f"The sum of gear ratios is: {gears_sum}")





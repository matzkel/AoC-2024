def get_positions(data: list[list[str]]) -> set[tuple[int, int]]:
    """
    Return all positions (row and column indexes) that guard will visit before going out of bounds.
    """
    # First value signifies row, second value signifies column,
    # negative values move up/left, and positive down/right
    directions = [
        [-1, 0],
        [0, 1],
        [1, 0],
        [0, -1]
    ]
    direction_idx = 0
    positions = set()

    curr_pos = None
    for row_idx, row in enumerate(data):
        try:
            col_idx = row.index("^")
            curr_pos = (row_idx, col_idx)
        except: pass

    total_steps = 0
    while True:
        next_row, next_col = curr_pos[0] + directions[direction_idx][0], curr_pos[1] + directions[direction_idx][1]
        if (next_row < 0 or next_row >= len(data)) or (next_col < 0 or next_col >= len(data[0])):
            break
        if data[next_row][next_col] == "#":
            direction_idx = (direction_idx + 1) % 4
            continue
        # Check if guard is stuck in a loop.
        if total_steps >= 15_000:
            return set()
            # TODO: find better way to detect loops
            # because right now it takes too much time
            # and with comically huge inputs it may be wrong
        
        curr_pos = (next_row, next_col)
        positions.add(curr_pos)
        total_steps += 1
    return positions

def get_obstructions(data: list[list[str]]) -> int:
    """
    Return amount of positions where obstructions
    could be put, so that they create a loop.
    """
    obstructions = 0
    for row_idx in range(len(data)):
        for col_idx in range(len(data[0])):
            if data[row_idx][col_idx] == "^" or data[row_idx][col_idx] == "#":
                continue
            data[row_idx][col_idx] = "#"
            if len(get_positions(data)) == 0: obstructions += 1
            data[row_idx][col_idx] = "."
    return obstructions
    
def main():
    puzzle = []
    with open("data.txt", "r", encoding="UTF-8") as file:
        data = file.read()
        for line in data.split("\n"):
            if line == "": break
            puzzle.append(list(line))
    print(f"Amount of distinct positions: {len(get_positions(puzzle))}")
    print(f"Amount of possible places for obstructions to put guard in a loop: {get_obstructions(puzzle)}")

if __name__ == "__main__":
    main()

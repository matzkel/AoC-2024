def get_positions(data: list[list]) -> int:
    """
    Return amount of distinct positions that guard
    will visit before going out of bounds.
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

    cursor_pos = None
    for row_idx, row in enumerate(data):
        try:
            col_idx = row.index("^")
            cursor_pos = [row_idx, col_idx]
        except: pass

    data[cursor_pos[0]][cursor_pos[1]] = "X"
    positions = 1 # account for position where cursor stands
    while True:
        next_row, next_col = cursor_pos[0] + directions[direction_idx][0], cursor_pos[1] + directions[direction_idx][1]
        if (next_row < 0 or next_row >= len(data)) or (next_col < 0 or next_col >= len(data[0])):
            break
        if data[next_row][next_col] == "#":
            if direction_idx == 3: direction_idx = 0
            else: direction_idx += 1
            continue
        if data[next_row][next_col] == ".":
            positions += 1
        
        cursor_pos = [next_row, next_col]
        data[cursor_pos[0]][cursor_pos[1]] = "X"
    return positions

def main():
    puzzle = []
    with open("data.txt", "r", encoding="UTF-8") as file:
        data = file.read()
        for line in data.split("\n"):
            if line == "": break
            puzzle.append(list(line))
    print(get_positions(puzzle))

if __name__ == "__main__":
    main()

def count_word(data: list[list[str]], word: str) -> int:
    """
    Count and return amount of times certain word appears in the data set.
    word argument is case-sensitive.
    Example below:

    data = [
        ['.', '.', 'X', '.', '.', '.'],
        ['.', 'S', 'A', 'M', 'X', '.'],
        ['.', 'A', '.', '.', 'A', '.'],
        ['X', 'M', 'A', 'S', '.', 'S'],
        ['.', 'X', '.', '.', '.', '.']
    ], word 'XMAS' appears 4 times.
    """
    word_count = 0
    rows, cols = len(data), len(data[0])
    for row in range(rows):
        for col in range(cols):
            if data[row][col] != word[0]: continue
            # Calculate the row range, so list doesn't get out of bonds
            row_range = None
            if row == 0:
                row_range = range(row, row + 2)
            elif row == rows - 1:
                row_range = range(row - 1, row + 1)
            else:
                row_range = range(row - 1, row + 2)
            # Calculate the column range, so list doesn't get out of bounds
            col_range = None
            if col == 0:
                col_range = range(col, col + 2)
            elif col == cols - 1:
                col_range = range(col - 1, col + 1)
            else:
                col_range = range(col - 1, col + 2)
            
            for curr_row in row_range:
                for curr_col in col_range:
                    if _find_word(data, word[1:], row, col, curr_row, curr_col): word_count += 1
    return word_count

def _find_word(data: list[list[str]], word: str, prev_row: int, prev_col: int, row: int, col: int) -> bool:
    """
    Find the word recursively, return True if found.
    """
    if word == "": return True
    try:
        if data[row][col] != word[0]: return False
    except: return False
    
    # Keep going in the same direction
    row_direction = row - prev_row
    col_direction = col - prev_col

    # Fix bug where negative indexing can cause false positives
    if (row + row_direction < 0 or col + col_direction < 0) and not len(word) == 1:
        return False

    return _find_word(data, word[1:], row, col, row + row_direction, col + col_direction)

def main():
    letters = []
    with open("./data.txt", "r", encoding="UTF-8") as file:
        data = file.read()
        for line in data.split("\n"):
            if line == "": break
            letters.append([])
            for letter in line:
                letters[-1].append(letter)
    print(f"Amount of times 'XMAS' appears in data: {count_word(letters, "XMAS")}")

if __name__ == "__main__":
    main()

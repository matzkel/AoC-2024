def count_word(data: list[list[str]]) -> int: 
    """
    Count and return amount of times 'MAS' word appears
    in the data set with X pattern, like:

    M - S  S - M  ...
    - A -  - A -  ...
    M - S  S - M  ...
    """
    word_count = 0
    rows, cols = len(data), len(data[0])
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            if data[row][col] == "A":
                # Check both diagonals, from top to bottom
                left_right = {data[row - 1][col - 1], data[row + 1][col + 1]}
                if left_right != {"M", "S"}:
                    continue
                right_left = {data[row - 1][col + 1], data[row + 1][col - 1]}
                if right_left != {"M", "S"}:
                    continue

                word_count += 1
    return word_count

def main():
    letters = []
    with open("./data.txt", "r", encoding="UTF-8") as file:
        data = file.read()
        for line in data.split("\n"):
            if line == "": break
            letters.append([])
            for letter in line:
                letters[-1].append(letter)
    print(f"Amount of times 'MAS' appears in data with X pattern: {count_word(letters)}")

if __name__ == "__main__":
    main()

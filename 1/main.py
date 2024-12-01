def calc_total_distance(left: list, right: list) -> int:
    """
    Calculate distances between elements
    from left and right lists and return the sum.
    """
    left = sorted(left)
    right = sorted(right)

    distances = []
    for i in range(len(left)):
        distance = max(left[i], right[i]) - min(left[i], right[i])
        distances.append(distance)
    
    return sum(distances)

def calc_similarity_score(left: list, right: list) -> int:
    """
    Iterate through the left list and find amount of times
    the number appears in the right list and return the sum.
    """
    scores = []
    for number in left:
        scores.append(number * right.count(number))
    return sum(scores)

def main():
    left, right = [], []
    with open("./data.txt", "r", encoding="UTF-8") as file:
        data = file.read()
        for line in data.split("\n"):
            if line == "": break
            # Each list is separated by 3 spaces
            left.append(int(line.split("   ")[0]))
            right.append(int(line.split("   ")[1]))
         
    print(f"Total distance: {calc_total_distance(left, right)}")
    print(f"Similarity score: {calc_similarity_score(left, right)}")

if __name__ == "__main__":
    main()

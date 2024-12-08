def check_rule(rules: dict[str, list[int]], data: list[int]) -> bool:
    """
    Check data using custom set of rules.
    Return True if data is correct according to rules.
    """
    rule_keys = set(map(lambda k: int(k), rules.keys()))
    nums = data
    for idx_outer in range(len(nums)):
        if data[idx_outer] not in rule_keys: continue
        # right_num -> right side of the rule
        for right_num in rules[str(nums[idx_outer])]:
            for idx_inner in range(len(nums)):
                if nums[idx_inner] != right_num or idx_outer < idx_inner: continue
                return False
    return True

def sort_rule(rules: dict[str, list[int]], data: list[int]) -> list[int]:
    """
    Return sorted data using custom set of rules.
    """
    rule_keys = set(map(lambda k: int(k), rules.keys()))
    nums = data
    for idx_outer in range(len(nums)):
        if data[idx_outer] not in rule_keys: continue
        # right_num -> right side of the rule
        for right_num in rules[str(nums[idx_outer])]:
            for idx_inner in range(len(nums)):
                if nums[idx_inner] != right_num or idx_outer < idx_inner: continue
                nums[idx_outer], nums[idx_inner] = nums[idx_inner], nums[idx_outer]
    return nums

def main():
    rules = {}
    nums = []
    with open("./data.txt", "r", encoding="UTF-8") as file:
        is_rule = True
        data = file.read()
        for line in data.split("\n"):
            if line == "": 
                is_rule = False
                continue
            if is_rule:
                left, right = line.split("|")
                if left in rules:
                    rules[str(left)].append(int(right))
                else:
                    rules[str(left)] = [int(right)]
            else:
                nums.append([int(num) for num in line.split(",")])
    
    correct_nums = []
    incorrect_nums = []
    for num in nums:
        if check_rule(rules, num):
            correct_nums.append(num)
        else:
            incorrect_nums.append(num)
    middle_nums = sum([nums[len(nums) // 2] for nums in correct_nums])
    print(f"Sum of middle nums from correct lists (part 1): {middle_nums}")

    sorted_nums = []
    for num in incorrect_nums:
        correct_num = num
        # Rawdog it (Better way would be to modify the algorithm)
        while not check_rule(rules, num):
            correct_num = sort_rule(rules, correct_num)
        sorted_nums.append(correct_num)
    middle_nums = sum([nums[len(nums) // 2] for nums in sorted_nums])
    print(f"Sum of middle nums from initially incorrect lists (part 2): {middle_nums}")

if __name__ == "__main__":
    main()

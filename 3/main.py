import re

def get_funcs(data: str, conditions: bool = False) -> list[str]:
    """
    Parse a string and return list of functions.
    If conditions is true, account for 'do()' and 'don't()' functions.
    """
    if not conditions:
        return [f for f in re.findall(r"mul\(\d+,\d+\)", data)]

    funcs = [f for f in re.findall(r"do\(\)|don't\(\)|mul\(\d+,\d+\)", data)]
    result = []
    is_stopped = False

    for func in funcs:
        if func == "don't()":
            is_stopped = True
            continue
        if func == "do()":
            is_stopped = False
            continue

        if not is_stopped:
            result.append(func)
    return result

def parse_func(func: str) -> int:
    """
    Parse a function and return result of multiplication.
    """
    numbers = (
        int(func.split(",")[0][4:]), # strip of 'mul(' part
        int(func.split(",")[1][:-1]) # strip of ')' part
    )
    return numbers[0] * numbers[1]

def main():
    funcs = []
    funcs_conditions = []
    with open("./data.txt", "r", encoding="UTF-8") as file:
        data = file.read()
        funcs = get_funcs(data)
        funcs_conditions = get_funcs(data, True)
    
    nums = []
    for func in funcs:
        nums.append(parse_func(func))

    nums_conditions = []
    for func in funcs_conditions:
        nums_conditions.append(parse_func(func))

    print(f"Sum of all multiplications: {sum(nums)}")
    print(f"Sum of all multiplications (with conditions): {sum(nums_conditions)}")

if __name__ == "__main__":
    main()

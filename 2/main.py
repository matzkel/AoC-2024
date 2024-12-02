def count_reports(reports: list[list[int]]) -> int:
    """
    Count amount of safe reports, i.e. reports whose levels are either 
    all increasing or all decreasing and any two adjacent levels differ
    by at least one and at most three.
    """
    count = 0
    for report in reports:
        is_safe = _check_report(report)
        if is_safe:
            count += 1
    return count

def count_reports_dampener(reports: list[list[int]]) -> int:
    """
    Count amount of safe reports, i.e. reports whose levels are either 
    all increasing or all decreasing and any two adjacent levels differ
    by at least one and at most three. It can tolerate a single bad level
    in what otherwise would be the safe report.
    """
    count = 0
    for report in reports:
        is_safe = _check_report(report)
        if not is_safe:
            for i in range(len(report)):
                # Bruteforce all the way!
                # Not the most elegant solution out there
                temp_report = report[::]
                temp_report.pop(i)
                is_safe = _check_report(temp_report)
                if is_safe: break
        if is_safe:
            count += 1
    return count

def _check_report(report: list[int]) -> bool:
    """
    Check report for safety, i.e. report whose levels are either all increasing
    or all decreasing and any two adjacent levels differ by at least one and at most three.
    Return a tuple which tells if current report is safe, otherwise suppliment with value index.
    """
    is_safe = True
    increasing = report[0] - report[1] < 0
    for i in range(len(report) - 1):
        curr = report[i]
        next = report[i + 1]
        dist = report[i] - report[i + 1]
        # Report was increasing but started decreasing, therefore report is unsafe
        if increasing and dist > 0:
            is_safe = False
            break
        # Report was decreasing but started increasing, therefore report is unsafe
        elif not increasing and dist < 0:
            is_safe = False
            break
        # Two adjacent levels must differ by at least one and at most three, otherwise report is unsafe
        if abs(dist) < 1 or abs(dist) > 3:
            is_safe = False
            break
    return is_safe

def main():
    reports = []
    with open("./data.txt", "r", encoding="UTF-8") as file:
        data = file.read()
        for line in data.split("\n"):
            if line == "": break
            report = [int(num) for num in line.split(" ")]
            reports.append(report)
    print(f"Amount of safe reports (without dampener): {count_reports(reports)}")
    print(f"Amount of safe reports (with dampener): {count_reports_dampener(reports)}")

if __name__ == "__main__":
    main()

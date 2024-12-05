def check_report(report: list[int]) -> bool:
    levels = iter(report)
    levels_increase, levels_decrease = False, False

    last_level = next(levels)
    for level in levels:
        if not (1 <= abs(level - last_level) <= 3):
            return False
        elif level > last_level:
            if levels_decrease:
                return False
            levels_increase = True
        elif level < last_level:
            if levels_increase:
                return False
            levels_decrease = True
        else:
            raise Exception('impossible ?')
        last_level = level
    return True


safe_count = 0
with open('input.txt') as f:
    for row in f:
        report_ = [int(level) for level in row.rstrip().split()]

        if check_report(report_):
            safe_count += 1
            continue

        for i in range(len(report_)):
            retry_report = report_.copy()
            retry_report.pop(i - 1)
            if check_report(retry_report):
                safe_count += 1
                break

print(safe_count)

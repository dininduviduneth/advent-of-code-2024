def check_incremental(report):
    checklist = []
    for i in range(len(report) - 1):
        checklist.append((report[i] - report[i+1] >= -3) and (report[i] - report[i+1] <= -1))

    return all(checklist)

def check_decremental(report):
    checklist = []
    for i in range(len(report) - 1):
        checklist.append((report[i] - report[i+1] <= 3) and (report[i] - report[i+1] >= 1))

    return all(checklist)

safe_reports = 0

with open('data.txt', 'r') as file:
    for line in file:
        report = list(map(int, line.split()))

        if check_incremental(report) or check_decremental(report):
            safe_reports += 1

print(f"The number of safe reports is: {safe_reports}")
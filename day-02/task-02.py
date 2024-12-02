def check_incremental(report):
    checklist = []
    for i in range(len(report) - 1):
        checklist.append((report[i] - report[i+1] >= -3) and (report[i] - report[i+1] <= -1))
    
    if all(checklist):
        return True

    for d in range(len(report)):
        checklist = []
        dampened_report = report.copy()
        dampened_report.pop(d)

        for i in range(len(dampened_report) - 1):
            checklist.append((dampened_report[i] - dampened_report[i+1] >= -3) and (dampened_report[i] - dampened_report[i+1] <= -1))

        if all(checklist):
            return True
    
    return False

def check_decremental(report):
    checklist = []
    for i in range(len(report) - 1):
        checklist.append((report[i] - report[i+1] <= 3) and (report[i] - report[i+1] >= 1))
    
    if all(checklist):
        return True

    for d in range(len(report)):
        checklist = []
        dampened_report = report.copy()
        dampened_report.pop(d)
        
        for i in range(len(dampened_report) - 1):
            checklist.append((dampened_report[i] - dampened_report[i+1] <= 3) and (dampened_report[i] - dampened_report[i+1] >= 1))

        if all(checklist):
            return True
    
    return False

safe_reports = 0

with open('data.txt', 'r') as file:
    for line in file:
        report = list(map(int, line.split()))

        if check_incremental(report) or check_decremental(report):
            safe_reports += 1
        else:
            print(f"Unsafe report: {report}")

print(f"The number of safe reports is: {safe_reports}")
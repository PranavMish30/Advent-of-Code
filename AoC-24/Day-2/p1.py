def isSafe(report):
    left = 0
    right = left + 1

    if int(report[left]) != int(report[right]):
        trend = (int(report[left]) - int(report[right]))/abs(int(report[left]) - int(report[right]))
    else:
        return False
    while right != len(report):
        change = int(report[left]) - int(report[right])
        if (change*trend) in range(1,4):
            left += 1
            right = left + 1
            continue
        else:
            return False
    return True    


result = 0
with open("input.txt","r") as file:
    for line in file:
        report = line.strip().split()
        if isSafe(report):
            result += 1
        else:
            continue
print("The number of safe reports are : ",result)

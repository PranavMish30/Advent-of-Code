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
            i = 0
            newReport = report[1:len(report)]
            while not(isSafe(newReport)):
                i += 1
                if i == len(report):
                    break
                if i in range(0,len(report)):
                    if i == len(report)-1:
                        newReport = report[0:len(report)-1]
                    else:
                        newReport = report[0:i] + report[i+1:len(report)]

            if i == len(report):
                continue
            else:
                result += 1
                continue

print("The number of safe reports are : ",result)

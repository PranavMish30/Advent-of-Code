list1 = []
list2 = []
result = 0

with open("input.txt","r") as file:
    for line in file:
        nums = line.strip().split()
        list1.append(int(nums[0]))
        list2.append(int(nums[1]))

list1 = sorted(list1)
list2 = sorted(list2)

for i in range(len(list1)):
    result += abs(list1[i] - list2[i])

print("The result is: ",result)


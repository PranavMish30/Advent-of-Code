from collections import defaultdict
list1 = []
list2 = []
result = 0
similarity = 0

with open("input.txt","r") as file:
    for line in file:
        nums = line.strip().split()
        list1.append(int(nums[0]))
        list2.append(int(nums[1]))

frequency = defaultdict(int)
for i in range(len(list2)):
    frequency[list2[i]] += 1

for i in range(len(list1)):
    similarity += (list1[i]*frequency[list1[i]])
    
print("The similarity score is : ",similarity)

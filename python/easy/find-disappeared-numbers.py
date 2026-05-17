# nums = [4,3,2,7,8,2,3,1]
nums = [1, 1]
nums.sort()
arr = set()
res = []

for num in range(len(nums)):
    arr.add(nums[num])
for j in range(1,len(nums) + 1):
    if j not in arr:
        res.append(j)   
print(res)

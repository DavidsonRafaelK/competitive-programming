nums = [8, 1, 2, 2, 3]

arr = [0] * len(nums)
curr = 0
for num in range (len(nums)):
    curr = nums[num]
    for j in nums:
        print(curr, j)
        if j < curr:
            arr[num] += 1
        else:
            arr[num] += 0
print(arr)

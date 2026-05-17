# nums = [2, 2, 2, 0, 1]
# nums = [4,5,6,7,0,1,4]
# nums = [1, 3,5]
# nums = [3,3,1,3]
nums = [3, 1, 1]
low = 0
high = len(nums) - 1

while low < high:
    middle = (low +  high) // 2
    if nums[middle] == nums[high]:
        high = high -1
    elif nums[middle] > nums[high]:
        low = middle + 1
    else:
        high = middle
print(nums)
print(nums[low])

arr = [3,2,1,0,4]

max_reach = 0

for num in range(len(arr)):
    max_reach = max(max_reach, num + arr[num])
    print(num, max_reach)
    if num > max_reach:
       print(False)
    else:
        print(True)
print(True)

A = [1,3,2,4]
B = [3,1,2,4]

c = [0]

for num1, num2 in zip(A, B):
    if num1 in A:
        c[num1] += 1
        print(c)

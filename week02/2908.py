A, B = input().split()

num1 = A[2] + A[1] + A[0]
num2 = B[2] + B[1] + B[0]

if(int(num1) > int(num2)):
    print(num1)
else:
    print(num2)

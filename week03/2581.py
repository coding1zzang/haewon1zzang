M = int(input())
N = int(input())

numbers = [i for i in range(M, N + 1)] # M이상 N이하의 자연수
sosu = []

for num in numbers: 
    error = 0
    if num > 1:
        for i in range(2, num):  
            if num % i == 0: # 나누어 떨어지는 수가 있으면 소수가 아님
                error += 1  
        if error == 0:
            sosu.append(num)

if len(sosu) == 0:
    print(-1)
else:
    print(sum(sosu))
    print(min(sosu))
            

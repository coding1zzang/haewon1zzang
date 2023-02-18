N = int(input()) # 수의 개수

numbers = map(int, input().split()) # N개의 수
sum = 0

for num in numbers: 
    error = 0
    if num > 1:
        for i in range(2, num):  
            if num % i == 0: # 나누어 떨어지는 수가 있으면 소수가 아님
                error += 1  
        if error == 0:
            sum += 1  # error가 없으면 소수
            
print(sum)
N = int(input()) # 정수 N

for i in range(2, N + 1):
    if N % i == 0:
        while N % i == 0: # 같은 수로 계속 나누어 떨어질 때까지
            print(i)
            N /= i
        

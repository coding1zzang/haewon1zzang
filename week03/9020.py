T = int(input()) # 테스트 케이스의 수 T

# 소수 검사 함수
def isPrime(num):
    if num == 1:
        return False # 1은 소수가 아님
    else:
        for i in range(2, int(num ** 0.5) + 1): 
            if num % i == 0:
                return False
        return True
    
for _ in range (T):
    num = int(input())

    a, b = num // 2, num // 2 # 절반부터 시작
    
    while a > 0:
        if isPrime(a) and isPrime(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1
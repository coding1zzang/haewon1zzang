M, N = map(int, input().split())
# ** 에라토스테네스의 체 **
def isPrime(num):
    if num == 1:
        return False # 1은 소수가 아님
    else:
        for i in range(2, int(num ** 0.5) + 1): # 제곱근까지만 검사하면 됨!
            if num % i == 0:
                return False
        return True


for i in range(M, N + 1):
    if isPrime(i):
        print(i)
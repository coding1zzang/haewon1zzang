# 소수 검사 함수
def isPrime(num):
    if num == 1:
        return False # 1은 소수가 아님
    else:
        for i in range(2, int(num ** 0.5) + 1): # 제곱근까지만 검사하면 됨!
            if num % i == 0:
                return False
        return True

# 제한 범위 내에서 소수 미리 구해놓기
all_list = list(range(2, 246912))		
sosu = []								

for i in all_list:						
    if isPrime(i):						
        sosu.append(i)	


while True:
    N = int(input())
    cnt = 0
        
    if N == 0:
        break
    
    for i in sosu:			
       if N < i <= 2 * N:		
            cnt += 1	
    print(cnt)

x = int(input()) # 영수증에 적힌 총 금액
n = int(input()) # 영수증에 적힌 구매한 물건의 종류의 수

sum = 0
for _ in range(n):
    a, b = map(int, input().split()) # 각 물건의 가격 a, 개수 b
    sum += a * b
    
if(sum == x):
    print('Yes')
else:
    print('No')

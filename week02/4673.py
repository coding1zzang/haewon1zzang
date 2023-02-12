def d(n): # 생성자
    temp = n + n // 1000 + n % 1000 // 100 + n % 100 // 10 + n % 10
    return temp
    
num = [i for i in range(1, 10001)] # 1부터 10000까지의 숫자    
    
for j in range(1, 10001):
  n = d(j)
  if n in num:
    num.remove(n)

for k in num:
  print(k)

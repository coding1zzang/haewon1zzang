a = [] # 42로 나눈 나머지 저장할 배열

for _ in range(10):
    n = int(input())
    a.append(n % 42) # 42로 나눈 나머지 추가
    
a = list(set(a)) # 중복 제거

print(len(a))
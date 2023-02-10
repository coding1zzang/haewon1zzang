a = [] # 9개의 서로 다른 자연수를 담을 배열

for _ in range(9):
    a.append(int(input())) # 9번 입력 받기

print(max(a)) # 최댓값
print(a.index(max(a)) + 1) # 최댓값이 몇 번째 수인지 - index + 1
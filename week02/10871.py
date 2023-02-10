N, X = map(int, input().split()) # 수열 A를 이루는 정수의 개수 N, 정수 X
A = list(map(int, input().split())) # 수열 A

for i in A:
    if i < X: # X보다 작은 수 찾기
        print(i, end = ' ')
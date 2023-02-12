T = int(input()) # 테스트 케이스의 개수 T

for _ in range (T):
    R, S = input().split()
    for i in range(len(S)):
        print(int(R) * S[i], end = '')
    print()

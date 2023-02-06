import sys

t = int(sys.stdin.readline()) # 테스트 케이스의 수
for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)
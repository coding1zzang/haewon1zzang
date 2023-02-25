''' 프로그래머스 형식 '''
import sys

def solution(n, p): # 사람의 수 n, 각 사람이 돈을 인출하는데 걸리는 시간 p
    ans = 0
    p.sort()

    for i in range (n):
        ans += p[i] * (n - i)

    return ans

if __name__ == "__main__":
    # 입력
    input = sys.stdin.readline
    n = int(input())
    p = [*map(int, input().split())]

    # 연산
    answer = solution(n, p)

    # 출력
    print(answer)
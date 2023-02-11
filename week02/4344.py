C = int(input()) # 테스트 케이스의 개수 C

for _ in range(C):
    score = list(map(int, input().split()))
    avg = (sum(score) - score[0]) / score[0] # score[0]은 학생의 수

    cnt = 0
    for i in score[1: ]:
        if i > avg:
            cnt += 1
    print("%.3f" %((cnt / score[0]) * 100) + '%') # 소수점 3자리 출력
            
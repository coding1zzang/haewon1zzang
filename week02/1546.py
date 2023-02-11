N = int(input()) # 시험 본 과목의 개수 N

score = list(map(int, input().split())) # 현재 성적 입력
max = max(score) # 점수 중에 최대값

new_score = [i * 100 / max for i in score]

print(sum(new_score) / N) # 새로운 평균
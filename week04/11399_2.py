N = int(input()) # N명의 사람들
p = list(map(int, input().split())) # 각 사람이 돈을 인출하는데 걸리는 시간

p.sort() # 오름차순 정렬

ans = 0

for i in range (N):
    ans += p[i] * (N - i)

print(ans)
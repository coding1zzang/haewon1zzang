N = int(input()) # 1000보다 작거나 같은 자연수 N

cnt = 0
for i in range(1, N + 1):
    if i < 100:
        cnt += 1 # 1~99는 다 한수
    else:
        num = list(map(int, str(i))) # 문자열로 변환
        if num[0] - num[1] == num[1] - num[2]: # ex. 234 일 때, -1 == -1
            cnt += 1
            
print(cnt)
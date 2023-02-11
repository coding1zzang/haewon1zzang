N = int(input()) # 테스트 케이스의 개수

for _ in range(N):
    cnt = 0; result = 0
    s = input()
    for i in range(len(s)):
        if(s[i] == 'O'):
            cnt += 1
            result += cnt
        else:
            cnt = 0
    print(result)
'''
    각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력
'''
t = int(input()) # 테스트 케이스의 개수

for i in range(1, t+1):
    a, b = map(int, input().split())
    print("Case #" + str(i) + ": " + str(a + b)) # 정수형 str()로 바꿔주기
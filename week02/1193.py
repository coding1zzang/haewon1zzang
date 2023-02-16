X = int(input()) # X번째 분수 구하기

line = 1

while X > line:
    X -= line
    line += 1

''' num1 : 분자, num2 : 분모'''
if line % 2 == 0: # 분자 오름차순, 분모 내림차순
    num1 = X
    num2 = line - X + 1
elif line % 2 == 1: # 분자 내림차순, 분모 오름차순
    num1 = line - X + 1
    num2 = X

print(num1, '/', num2, sep="")  # 공백 없이 분수 형태로 출력

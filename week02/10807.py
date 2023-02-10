N = int(input()) # 정수의 개수 N
list = list(map(int, input().split())) # 정수 N개 입력 (list 이용)

v = int(input()) # 찾고자 하는 정수 V
print(list.count(v)) # list.count('찾고자 하는 값') : 찾고자 하는 값이 list에 몇 개나 있는지
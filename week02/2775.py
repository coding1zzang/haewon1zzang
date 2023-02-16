T = int(input()) # 테스트 케이스의 수 
'''
    ...
    3층 |   1   5   15  35
    2층 |   1   4   10  20
    1층 |   1   3   6   10
    0층 |   1   2   3   4
        -------------------
           1호 2호  3호  4호 ...
'''
    
for _ in range (T):
    k = int(input()) # k층
    n = int(input()) # n호
    
    people = [i for i in range(1, n + 1)] # 0층 : [1, 2, 3, ..., n]
    
    for x in range(k):
        for j in range (1, n):
            people[j] += people[j - 1]
            
    print(people[-1]) # 가장 마지막 수 출력
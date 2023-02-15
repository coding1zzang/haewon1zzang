A, B, C = map(int, input().split()) # 고정 비용, 가변 비용, 노트북 가격
'''
    C * n > A + B * n (n은 판매량)
    1) 손익분기점일 때 판매량 n = A / (C - B)
    2) 최초로 이익이 발생하는 판매량 n = A / (C - B) + 1
'''
if B >= C: 
    print(-1) # 손익분기점 존재 X
else:
    print(int(A / (C - B) + 1))
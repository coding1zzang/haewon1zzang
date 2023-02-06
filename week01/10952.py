while(True):
    a, b = map(int, input().split())
    
    if(a == 0 and b == 0): # 입력의 마지막
        break
    print(a + b)
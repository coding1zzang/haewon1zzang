x = int(input()) # x좌표
y = int(input()) # y좌표

if((x > 0) and (y > 0)):
    print(1) # 1사분면
elif((x < 0) and (y > 0)):
    print(2) # 2사분면
elif((x < 0) and (y < 0)):
    print(3) # 3사분면
else:
    print(4) # 4사분면


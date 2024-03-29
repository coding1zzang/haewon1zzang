'''
    [아이디어]
     이전 수의 일의자리 수가 다음 수의 십의자리 수가 되고,
     이전 수의 각 자리를 더한 것의 일의자리 수가 다음 수의 일의자리 수가 됨
     26 -> 68 -> 84 -> 42 -> 26   =  4번
     6(26 % 10)  ...
     8(2+6)     ...

'''
cnt = 0
n = int(input())
num = n

while(True):
    # temp = (이전 수의 일의자리 수 * 10) + (이전 수의 각 자리를 더한 것에서 일의 자리)
    temp = (n % 10) * 10 + (n // 10 + n % 10) % 10
    cnt += 1
    n = temp
    if(temp == num): # 원래의 수로 돌아오면 무한루프 빠져 나가기
        break

print(cnt)
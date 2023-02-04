a, b = map(int, input().split()) # 현재 시각 a시 b분
c = int(input()) # 요리하는데 필요한 시간(분)

total = a * 60 + b + c

if(total >= 1440):
    total -= 1440

print(total // 60, total % 60)

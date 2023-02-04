h, m = map(int, input().split()) # 현재 상근이가 설정한 놓은 알람 시간 h시 m분
    
total = h * 60 + m # 일단 다 분으로 만들기
if(total - 45 < 0):
    total += 1440 # 24시간은 1440분
    total -= 45
else:
    total -= 45

print(total // 60, total % 60)
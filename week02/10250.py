T = int(input())  # 테스트 케이스의 수

for _ in range (T):
    H, W, N = map(int, input().split()) # 호텔의 층 수, 각 층의 방 수, 몇 번째 손님인지
  
    if N % H == 0: 
        floor = H
        room = N // H
    else:
        floor = N % H
        room = N // H + 1 
        
    print(floor * 100 + room)

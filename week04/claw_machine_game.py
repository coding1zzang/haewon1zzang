def solution(board, moves):
    ans = 0 # 사라진 인형의 개수
    h = len(board) # 격자의 높이
    moves_cnt = len(moves) # 크레인 작동 횟수
    
    basket = []
    
    # --- 크레인 작동 ---
    for i in range(moves_cnt): 
        pos = moves[i] - 1 # 인덱스로는 -1 해준 값 (열)
        
        for j in range(h): # 행 - 작을수록 상단
            if board[j][pos] == 0: # 인형이 있을 때까지 아래로
                continue
            
            doll = board[j][pos]
            board[j][pos] = 0 # 빈칸으로 만들기
            
            if basket and doll == basket[-1]: # 꺼낸 인형과 바구니의 인형이 같으면
                basket.pop() # 터뜨려짐
                ans += 2
            else:
                basket.append(doll)
            break
    return ans

import sys

if __name__ == "__main__":
    # 입력
    input = sys.stdin.readline

    board = [[0,0,0,0,0], [0,0,1,0,3], [0,2,5,0,1], [4,2,4,4,2], [3,5,1,3,1]]
    moves = list(map(int, input().split()))

    # 연산
    answer = solution(board, moves)

    # 출력
    print(answer)
'''
    테스트 케이스의 수를 모름 → input() 함수는 파일의 끝일 때 EOFError를 발생
'''
while(True):
    try:
        a, b = map(int, input().split())
        print(a + b)
    except:
        break
        
    
a, b = map(int, input().split()) # 두 수 a, b 입력

if(a > b):
    print('>')
elif(a < b):
    print('<')
else:
    print('==')
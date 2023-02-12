S = input() # 단어 S, 알파벳 소문자
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for x in alphabet:
    print(S.find(x), end = ' ')
N = int(input()) # 단어의 개수 N

def isGroup(word):
    for i in range(len(word)):
        if i != len(word) - 1:
            if word[i] == word[i + 1]: # 두 단어가 같으면
                pass
            elif word[i] in word[i + 1: ]:
                return False
    return True

cnt = 0
        
for _ in range (N):
    word = input() # 그룹 단어인지 체크할 단어
    if isGroup(word):
        cnt += 1

print(cnt)
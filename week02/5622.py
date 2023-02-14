word = input()

dial = ['', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ'] # 2초, 3초, 4초, 5초, ...
ans = 0

for j in range(len(word)):
    for i in dial:
        if word[j] in i:
            ans += dial.index(i) + 2
print(ans)
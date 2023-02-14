word = input()

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in croatia:
    word = word.replace(i, 'c')  # 크로아티아 알파벳만 'c'로 변경

print(len(word))

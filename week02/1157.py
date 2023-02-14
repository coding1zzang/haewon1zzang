word = input().upper() # 대문자로 입력 
word_list = list(set(word)) # 단어 중복 제거해서 알파벳 저장
cnt = []

for i in word_list:
  cnt.append(word.count(i)) # 각 단어에서 알파벳 수 세기

MAX = max(cnt)
if cnt.count(MAX) > 1:
  print("?")

else:
  print(word_list[(cnt.index(MAX))])
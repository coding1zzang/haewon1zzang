a, b, c = map(int, input().split()) # 공백으로 구분하여 a, b, c 입력

print((a + b) % c)
print(((a % c) + (b % c)) % c)
print((a * b) % c)
print(((a % c) * (b % c)) % c)
a = int(input()) # 472
b = int(input()) # 385

print(a * (b % 10)) # 472 * 5
print(a * ((b % 100) // 10)) # 472 * 8
print(a * (b // 100)) # 472 * 3
print(a * b) # 472 * 385

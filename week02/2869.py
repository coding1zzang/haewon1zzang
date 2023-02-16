A, B, V = map(int, input().split())  # 낮에 A미터 올라가고, 밤에 B미터 미끄러짐, 나무막대 V미터
''' 
    달팽이가 정상에 도달하는데 x일이 걸린다면,
        Ax - B(x - 1) = V
        (A - B)x = V - B
        x = (V - B) / (A - B)
'''
x = (V - B) / (A - B)
if x == int(x):
    print(int(x))
else:
    print(int(x) + 1)

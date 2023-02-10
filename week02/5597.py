student = [i for i in range(1, 31)] # 전체 학생 출석 번호

for _ in range(28): # 제출자 출석번호 입력
    n = int(input())
    student.remove(n)

print(student[0])
print(student[1])
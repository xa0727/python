n=int(input())
students=()
for _ in range(n):
    data=input().split()
    student_id=int(data[0])
    name=data[1]
    score=float(data[2])
    students+=((student_id,name,score),)

scores=tuple(s[2] for s in students)
average=sum(scores)/len(scores)
max_score=max(scores)
max_student=None
for s in students:
    if s[2]==max_score:
        max_student=s
        break
print(scores)
print(f"平均成绩：{average:.2f}")
print(max_student)
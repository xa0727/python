def sort_students(students):
    return sorted(students,key=lambda x:(-x[1],x[2],x[0]))

if __name__=='__main__':
    students=eval(input())
    result=sort_students(students)
    print(result)
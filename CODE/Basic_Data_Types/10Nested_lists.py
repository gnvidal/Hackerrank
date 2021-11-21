def record(name, score):
    pass
if __name__ == '__main__':
    students=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        record(score, name)
        students.append([score,name])
    students=sorted(students)
    names = sorted(list(set([x[1] for x in students])))
    print(names[1])
    print(names[2])
    

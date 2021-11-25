if __name__ == '__main__':
    results=[]
    lowests=[]
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        results.append([score,name])
        
    second_lowest=results[1]

    if score==second_lowest:
        lowests.append(name)
    for name in sorted(lowests):
        print(name, end="\n")

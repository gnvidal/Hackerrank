results = []
second_lowest_names = []
scores = set()

for _ in range(int(input())):
    name = input()
    score = float(input())
    results.append([name, score])
    scores.add(score)
        
second_lowest = sorted(scores)[1]

for name, score in results:
    if score == second_lowest:
        second_lowest_names.append(name)

for name in sorted(second_lowest_names):
    print(name, end='\n')

from itertools import combinations
with open('day9/input.txt') as f:
    data=[int(l) for l in f.read().splitlines()]
for i in range(25, len(data)):
    flag=False
    for pair in combinations(data[i-25:i], 2):
        if pair[0]!=pair[1] and pair[0]+pair[1]==data[i]:
            flag=True
            break
    if not flag:
        print(data[i])
        break
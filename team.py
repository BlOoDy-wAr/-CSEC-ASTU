n = int(input())

solved = 0
for i in range(n):
    solve = list(map(str, input().split()))
    if eval("+".join(solve)) >= 2:
        solved+=1

print(solved)

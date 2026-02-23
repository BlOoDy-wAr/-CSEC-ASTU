matrix = [[],[],[],[],[]]

for i in range(5):
    row = list(map(int, input().split()))
    matrix[i] = row

loc_1 = []
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            loc_1 = [i,j]


cen_x = 2
cent_y = 2

ans = abs(loc_1[0] - cen_x) + abs(loc_1[1] - cent_y)
print(ans)

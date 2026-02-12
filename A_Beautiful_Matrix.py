matrix = []

for _ in range(5):
    row= list(map(int, input().split()))
    matrix.append(row)

total_move = 0
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            total_move += (abs(i+1-3) + abs(j+1-3))

print(total_move)


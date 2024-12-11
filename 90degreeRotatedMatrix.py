# 90 degree matrix

n = int(input())
mat = []

for i in range(n):
    row = list(map(int,input().split()))
    mat.append(row)
    
for i in range(n):
    for j in range(i+1,n):
        mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        
for i in range(n):
    mat[i] = mat[i][::-1]

for i in range(n):
    for j in range(n):
        print(mat[i][j], end=" ")
    print()
    
    
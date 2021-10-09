N=4
def transpose(matrix):
    for i in range(N):
        for j in range(i+1,N):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix


matrix = [[ 10, 20, 30, 40 ],
       [ 15, 25, 35, 45 ],
       [ 27, 29, 37, 48 ],
       [ 32, 33, 39, 50 ]]
transpose(matrix)
print(matrix)
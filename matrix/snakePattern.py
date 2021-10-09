# ### print matrix element in snake pattern
R=int(input("Enter Row value"))
C=int(input("Enter column value"))
def snakePattern(matrix):
    global R, C
    for i in range(R):
        if i % 2 == 0:
            for j in range(C):
                print(str(matrix[i][j]), end=" ")
        else:
            for j in range(C-1, -1, -1):
                print(str(matrix[i][j]), end=" ")



            # matrix=[]

#
# for _ in range(R):
#     a=[]
#     for _ in range(C):
#         a.append(int(input()))
#     matrix.append(a)
matrix = [[ 10, 20, 30, 40 ],
       [ 15, 25, 35, 45 ],
       [ 27, 29, 37, 48 ],
       [ 32, 33, 39, 50 ]]
snakePattern(matrix)
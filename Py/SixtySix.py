
matrix_1 = [[1,2,3],
            [4,5,6],
            [7,8,9]]

matrix_2 = [[3,4,5],
            [6,7,8],
            [9,10,11]]

matrix_3 = []

for i in range (len(matrix_1)):

    new_row =[]

    for j in range(len(matrix_1[0])):

        new_row.append(matrix_1[i][j]+matrix_2[i][j])

    matrix_3.append(new_row)

#for i in range (len(matrix_1)):
print(f"{matrix_1} + {matrix_2} = {matrix_3}")
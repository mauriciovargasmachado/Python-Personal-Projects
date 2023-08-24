
rows = int(input("Insert the number of rows required: "))
columns = int(input("Insert the number of rows required: "))

matrix =[]

for r in range(rows):
    row = []
    for c  in range(columns):
        row.append(int(input(f"Please insert the element {c} of the row: ")))
    matrix.append(row)
print(matrix)

for i in matrix:
    for element in i:
        print(element, end="")

    print("")


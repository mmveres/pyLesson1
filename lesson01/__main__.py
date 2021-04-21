def print_for_for():
    for i in range(0, 10, 1):
        # i - iteration
        print("*******i = ", i)
        for j in range(0, 10, 1):
            print("j = ", j)
        # -------------------


def print_triangle():
    for i in range(10):
        for j in range(10):
            if i == 9 or j == 0 or i == j:
                print(i, j, sep="", end=" ")
            else:
                print("  ", end=" ")
        print()


def print_by_reference(matrix):
    for row in matrix:
        for cell in row:
            print(cell, end="\t")
        print()


def print_by_index(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="\t")
        print()


def create_matrix_by_multy():
    matrix = list()
    count_row = int(input("Enter count row"))
    count_column = int(input("Enter column"))
    for i in range(count_row):
        matrix.append(list())
        for j in range(count_column):
            # cell = int(input(f"matrix[{i}][{j}] ="))
            cell = i * j;
            matrix[i].append(cell)
    return matrix

def create_matrix_from_console():
    matrix = list()
    count_row = int(input("Enter count row"))
    count_column = int(input("Enter column"))
    for i in range(count_row):
        matrix.append(list())
        for j in range(count_column):
            cell = int(input(f"matrix[{i}][{j}] ="))
            matrix[i].append(cell)
    return matrix

def create_matrix_from_file(filename):
    matrix = list()
    with open(filename,"r") as data_file:
        for row_str in data_file:
            row = list()
            cells_str = row_str.split(" ")
            for cell_str in cells_str:
                row.append(int(cell_str))
            matrix.append(row)
    return matrix

if __name__ == '__main__':
    matrix = create_matrix_from_file("matrix.txt")

    print(matrix)
    print_by_reference(matrix)
   # print_by_index(matrix)
    sum_matrix = 0
    sum_row_matrix = list()
    aver_row_matrix = list()
    for row in matrix:
        sum = 0
        for cell in row:
            sum+=cell
        print(sum)
        sum_matrix+=sum
        sum_row_matrix.append(sum)
        aver_row_matrix.append(sum/len(row))
    print(sum_matrix)
    print(sum_row_matrix)
    print(aver_row_matrix)


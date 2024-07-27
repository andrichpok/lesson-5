def get_matrix(n,m,value):
    matrix = []
    for i in range(n):
        string = [value]*m
        matrix.append(string)
    return matrix
list_1 = get_matrix(2,2,2)
list_2 = get_matrix(3,3,3)
list_3 = get_matrix(4,4,4)
print(list_1)
print(list_2)
print(list_3)
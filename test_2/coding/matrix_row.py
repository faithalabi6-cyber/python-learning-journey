#create a variable matrix
matrix = [[2, 4, 6], [1, 3, 5], [10, 20, 30]]


for i, row in enumerate (matrix, start =1): 
    total_row = 0
    for num in row:

        total_row += num
        
    print(f"Row{i} total :{total_row}")



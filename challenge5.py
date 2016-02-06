def answer(food, grid):
    N = len(grid)
    result = [[set() for j in range(N)] for i in range(N)]
    result[0][0] |= {0}
    # print result
    for row, row_val in enumerate(grid) :
        for col, col_val in enumerate(row_val) :
            if row != 0 :
                result[row][col] |= {col_val + a for a in result[row-1][col] if col_val + a <= food }
            if col != 0 :
                result[row][col] |=  {col_val + a for a in result[row][col-1] if col_val + a <= food }

    temp = result[N-1][N-1]
    temp = sorted(temp, reverse = True)
    for x in temp :
        if x <= food :
            return food-x
    return -1

# print answer(7, [[0, 2, 5], [1, 1, 3], [2, 1, 1]])
print answer(12, [[0, 2, 5], [1, 1, 3], [2, 1, 1]])
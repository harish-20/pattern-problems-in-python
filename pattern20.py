def pattern20(n):
    for rows in range(0, n+1):
        for cols in range(0, n):
            colsCheck = cols == 0 or cols == n-1
            rowsCheck = rows == 0 or rows == n
            character = '*' if colsCheck or rowsCheck else ' '
            print(character, end='')
        print()

pattern20(4)
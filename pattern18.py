def pattern18(n):
    noOfIterations = 2*n
    for rows in range(0, n):
        for topColumns in range(0, n):
            if(topColumns > n-rows):
                print(' ', end='')
                continue
            print( "*", end='')
        for bottomColumns in range(n, -1, -1):
            if(bottomColumns > n-rows):
                print(' ', end='')
                continue
            print('*', end='')
        print()
    for rows in range(n, -1, -1):
        for topColumns in range(0, n):
            if(topColumns > n-rows):
                print(' ', end='')
                continue
            print( "*", end='')
        for bottomColumns in range(n, -1, -1):
            if(bottomColumns > n-rows):
                print(' ', end='')
                continue
            print('*', end='')
        print()
    

pattern18(6)
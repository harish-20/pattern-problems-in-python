def pat14(n):
    for row in range(0,n):
        print(' '*(n-row),end='')
        for col in range(0,row):
            if(col==0 or col==row-1 or row==n-1):
                print('* ',end='')
            else:
                print('  ',end='')
        print()

pat14(7)
def pat13(n):
    for row in range(0,n):
        print(' '*(n-row),end='')
        for col in range(0,row):
            if(col==0 or col==row):
                print('* ',end='')
            else:
                print(' ',end='')
        print()

pat13(6)
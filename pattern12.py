def pat12(n):
    for row in range(0,2*n):
        if(row<n):
            print(' '*row,end='')
            for col in range(0,n-row):
                print('* ',end='')
        else:
            print(' '*(2*n-row-1),end='')
            for col in range(0,row-n+1):
                print('* ',end='')
        print()

pat12(5)


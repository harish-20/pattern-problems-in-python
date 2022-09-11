def pat10(n):
    for row in range(0,2*n):
        if(row<n):
            print(' '*row,end='')
            for col in range(n-row,0,-1):
                print(' *',end='')
        else:
            print(' '*(2*n-row),end='')
            for col in range(0,row-n+1):
                print('* ',end='')
        print('')

pat10(6)

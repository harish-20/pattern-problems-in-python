def pat9(n):
    for row in range(0,n):
        print(' '*row,end='')
        for col in range(2*n-2*row-1,0,-1):
            print("*",end='')
        print('')
    
pat9(5)


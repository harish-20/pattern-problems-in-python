def pat8(n):
    for row in range(0,n):
        for col in range(n+row, 0, -1):
            print('*' if col <= 2*row+1 else ' ',end='')
        print('')
        
pat8(10)
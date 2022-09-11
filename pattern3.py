def pat1(n):
    for row in range(0,n):
        print(' '*int(n-(row+1)),end='')
        for col in range(0,row+1):
            print('* ',end='')
        print('')
pat1(3)
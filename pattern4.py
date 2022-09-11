def pat4(n):
    for row in range(0,n):
        print(' '*row,end='')
        for col in range(0,n-row):
            print('* ',end='')
        print('')
pat4(int(input('Enter the n...')))
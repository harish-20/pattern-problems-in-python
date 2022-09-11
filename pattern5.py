def pat5(n):
    for row in range(1,2*n):
        for col in range(0,(row if row<n else (2*n)-(row))):
            print('* ',end='')
        print('')
pat5(int(input('Enter the n...')))
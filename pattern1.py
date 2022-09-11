def pat1(n):
    for row in range(0,n+1):
        for col in range(0,row):
            print ('* ',end='')
        print('')
pat1(int(input('Enter a num...')))


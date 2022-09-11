def pat15(n):
    for row in range(1,2*n):
        if(row <= n):
            for topcol in range(0,n+row-1):
                if (topcol == n-row or topcol == n+row-2):
                    print('*',end ='')
                else:
                    print(end =' ')
        else:        
            for dowcol in range(2*n-(row-n),0,-1):
                if (dowcol == 2*(n-(row-n)) or dowcol == 2):
                    print('*',end='')
                else:
                    print(end=' ')
        print()
pat15(int(input('Enter a number')))
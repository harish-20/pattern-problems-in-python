def pattern17(n):
    noOfIterations = (2 * n)
    for outerLoop in range(0, noOfIterations):
        if(outerLoop < (noOfIterations//2 + 1)):
            print(' ' * (n - outerLoop), end='')

            for innerLoopTop in range(outerLoop, 0, -1):
                print(innerLoopTop , end='')
            
            for innerLoopTop in range(1, outerLoop):
                print(innerLoopTop+1, end='')
            print()
        else:
            print(' ' * (outerLoop - n), end='')

            for innerLoopBottom in range(noOfIterations - outerLoop, 1, -1):
                print(innerLoopBottom, end='')

            for innerLoopBottom in range(1, noOfIterations - outerLoop + 1):
                print(innerLoopBottom, end='')
            print()
            
pattern17(5)
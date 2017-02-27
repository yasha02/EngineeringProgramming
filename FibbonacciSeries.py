#program to create Fibonacci Series

def fibonacciSeries(n):
    a = 0
    b = 1
    for i in range(1,n+1):
            c = a + b
            print b
            a = b
            b = c
fibonacciSeries(10)      
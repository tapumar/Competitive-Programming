def fib(n):
    a = 0
    b = 1;
    i = 0
    while (i < n):
        c = a
        a = b
        b = a + c
        i = i+1
    return a

n = int(input())
res = fib(n)
print(res)

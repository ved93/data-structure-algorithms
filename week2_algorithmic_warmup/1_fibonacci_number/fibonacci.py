# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)


def calc_fib_fast(n):
    if (n <= 1):
        return n
    st = [None]*(n)
    # print(len(st))
    st[0]= 1
    st[1] = 1
    for i in range(2,n):
        st[i] = st[i-1]+st[i-2]

    return st[n-1]


n = int(input())
# n= 0
print(calc_fib_fast(n))

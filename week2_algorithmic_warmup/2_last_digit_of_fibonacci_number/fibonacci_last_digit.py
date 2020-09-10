# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10



def get_fibonacci_last_digit(n):
    if n <= 1:
        return n

    # st = [None]*(n)
    # # print(len(st))
    # st[0]= 1
    # st[1] = 1
    # for i in range(2,n):
    #     st[i] = st[i-1]+st[i-2]

    # return str(st[n-1])[-1]

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10

    return current 




if __name__ == '__main__':
    # input = sys.stdin.read()
    n = int(input())
    # print(get_fibonacci_last_digit(n))
    print(get_fibonacci_last_digit(n))


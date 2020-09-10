# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    # print(values)
    # print(sorted(values/weights))
    res = {ind:i / j for ind,(i, j) in enumerate(zip(values, weights))} 
    # res = sorted(res, reverse=True)
    bst_ind = sorted(res, key=res.get, reverse=True)
    # for i in res:ß
    # while capacity > 0:
    for i,j in enumerate(bst_ind):
        if capacity == 0:
            break

        amt=min(weights[j], capacity)
        value = value+amt*(values[j]/weights[j])
        capacity -=amt

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))


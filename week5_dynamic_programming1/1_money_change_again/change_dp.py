# Uses python3
import sys


# import math

# money = int(input())
# denominations = [1, 3, 4]
# minCoins = [0] + [math.inf]*money

# for i in range(1, money+1):
#     for j in denominations:
#         if i>=j:
#             coins = minCoins[i-j]+1
#             if coins < minCoins[i]:
#                 minCoins[i] = coins

# print(minCoins[money])

def get_change(m):
    #write your code here
    coins = [0]*(m+1)
    coins[0] = 0
    for i in range(1,m+1):

        if i  < 3:
            coins[i] = i
        elif i < 5:
            coins[i] = 1
        else:
            coins[i]=min(coins[i-1], coins[i-3],coins[i-4])+1

    return coins[m]




if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))

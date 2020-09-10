# python3
import random

def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product



def max_pairwise_product_fast(arr):
    n1 = max(arr)
    arr.remove(n1)
    n2 = max(arr)
    return n1*n2






if __name__ == '__main__':
    # input_n = int(input())
    # input_numbers = [int(x) for x in input().split()]
    # assert (len(input_numbers) == input_n)

    # print(max_pairwise_product_fast(input_numbers))


    # # # Stress test
    from random import randint
    def max_prod_stress(N,M):
        while True:
            n = randint(2,N)
            A = [None]*n
            for i in range(n):
                A[i] = randint(0,M)
            print(A)
            result1 = max_pairwise_product(A)
            result2 = max_pairwise_product_fast(A)
            if result1==result2:
                print('OK')
            else:
                print('Wrong answer:',result1,result2)
                return





    max_prod_stress(10,100000)    

# 2nd way of stress test
    # def max_prod_stress(N,M):
    #     t = 0
    #     while True:   #t< M:
    #         n = random.randrange(2, N)
    #         # print(n)
    #         # if n > 100:
    #         #     n = 100


    #         numbers = random.sample(range(n), n)

    #         # print(numbers)
    #         result = max_pairwise_product(numbers)
    #         resultFast = max_pairwise_product_fast(numbers)

    #         if(result != resultFast):
    #             print("Wrong answer! Numbers:{} Basic:{} Fast:{}".format(numbers, result, resultFast))
    #             break
    #         else:
    #             print("OK")
            
    #         t = t+1
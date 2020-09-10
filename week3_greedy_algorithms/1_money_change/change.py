# Uses python3
import sys

def get_change(m):
    #write your code here
    if m < 5:
        return m
    elif (m >= 5) and (m < 10):
        ones=m%5
        return int(1+ones)

    else:
        # for i in [10,5,1]:
        left=m%10
        tens = (m-left)/10
        nums=get_change(left)

        return int(tens+nums)



def get_change_simpl(m):
    #write your code here
    return m//10 + (m%10)//5 + (m%5)



if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))

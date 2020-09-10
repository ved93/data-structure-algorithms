# Uses python3
import sys

"""
# Time Complexity : O(nlogn)
# Auxilary Space : O(1)/Constant
"""
def get_majority_elementv2(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    a.sort()
    count = j = 0
    for i in range(1, len(a)):
        if a[i] != a[i-1]:
            if count < i-j:
                count = i-j
            j = i
    if count > len(a)/2:
        return count
    return -1

"""
# Description : SPACE TIME TRADEOFF using dictionary
# Time Complexity : O(n)
# Auxilary Space : O(n)
"""
def get_majority(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    lookup = {}
    for i in a:
        if i not in lookup:
            lookup[i] = 1
        else:
            lookup[i] += 1
    maximum = max(lookup.values())
    if maximum > len(a)/2:
        return maximum
    return -1

# ------------------------------------- Using recursion ------------------------------------ #

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    mid = (left+right)//2
    x = get_majority_element(a,left,mid)
    y = get_majority_element(a,mid,right)

    xcount = get_count(a, mid, right,x) + get_count(a, left,mid,x)
    ycount = get_count(a, left, mid,y)+ get_count(a, mid, right,y)
    if xcount>ycount and xcount > (right-left)//2:
        return x 
    elif ycount>xcount and ycount > (right-left)//2:
        return y
    if x==y :
        return x
    
    return -1
    
    

def get_count(a, left, right,x):
    count = 0
    for i in range(left,right):
        if(a[i]==x):
            count+=1
    return count   

# ------------------------------------ ks ------------------------------------ #


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    # n = 5
    # a = [2,3,9,2,2]

    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)

# Uses python3



def edit_dist_dp(str1, str2, m,n):
    dp = [[0 for x in range(n+1)] for x in range(m+1)]

    #fill dp[][] in bottom up order
    for i in range(m+1):
        for j in range(n+1):

            #if 1st str is empty
            if i == 0 :
                dp[i][j] = j

            elif j == 0 :
                dp[i][j] = i

            #if last char is same as
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]

            #if last diff
            else:
                dp[i][j] = 1+min(dp[i][j-1], 
                dp[i-1][j], dp[i-1][j-1])
                
    return dp[m][n]


if __name__ == "__main__":
    str1 = "sunday"
    str2 = "saturday"
    print(edit_dist_dp(str1, str2, len(str1), len(str2)))

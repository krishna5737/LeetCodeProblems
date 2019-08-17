def longestCommonSubsequence(self, a: str, b: str) -> int:
        m = len(a)
        n = len(b)
   
        dpMatrix = [[0]*(n+1) for i in range(m+1)] 

        for i in range(1,m+1):
            for j in range(1,n+1):
                if(a[i-1] == b[j-1]):
                    dpMatrix[i][j] = dpMatrix[i-1][j-1] + 1
                else:
                    dpMatrix[i][j] = max(dpMatrix[i-1][j],dpMatrix[i][j-1])
        return(dpMatrix[m][n])

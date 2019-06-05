def gcd(self,a,b):
        if b == 0: 
            return a 
        else: 
            return self.gcd(b, a % b) 
    
    def rotate(self, nums, k):
        arr = nums
        n = len(arr)
        d = k
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        g_c_d = self.gcd(n,d)
        block_size = g_c_d
        print(g_c_d)
        for i in range(block_size):
            temp = arr[i]
            j = i
            while 1:
                k = j + d
                if(k>=n):
                    k = k-n
                if(k==i):
                    break
                arr[j] = arr[k]
                j = k
            arr[j] = temp

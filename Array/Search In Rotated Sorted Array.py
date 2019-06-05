class Solution(object):
    def binarySearch(self,arr,l,h,key):
        if h < l:
            return -1
        else:
            mid =  (l+h)//2
            if(key == arr[mid]):
                return mid
            elif(key>arr[mid]):
                return self.binarySearch(arr,mid+1,h,key)
            return self.binarySearch(arr,l,mid-1,key)
                
    def findPivot(self,arr,low,high):
        if low > high:
            return -1
        if low == high:
            return low
        mid = (low+high)//2
        
        if(mid<high and arr[mid] > arr[mid+1]):
            return mid
        if(mid>low and arr[mid] < arr[mid-1]):
            return mid-1
        if arr[low] >= arr[mid]:
            return self.findPivot(arr,low,mid-1)
        return self.findPivot(arr,mid+1,high)
            
        
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        arr = nums
        if(len(arr)==0):
            return -1
        if(len(arr)==1):
            if(arr[0]==target):
                return 0
            else:
                return -1
        # arr = [1,3,5,6,7,8,9]
        # print(self.binarySearch(arr,0,len(arr)-1,7))
        pivot = self.findPivot(nums,0,len(nums)-1)
        print(pivot)
        if(pivot == -1):
            return self.binarySearch(arr,0,len(arr)-1,target)
        if(arr[pivot] == target):
            return pivot
        if(arr[0] <= target):
            return self.binarySearch(arr,0,pivot-1,target)
        return self.binarySearch(arr,pivot+1,len(arr)-1,target)
            
        
        
        

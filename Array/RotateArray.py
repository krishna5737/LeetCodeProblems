#This code explains algorithm for shifting an array k times rightward
#def rightRotate( arr, d, n): 
  #reverseArray(arr, 0, n - 1); 
  #reverseArray(arr, 0, d - 1); 
  #reverseArray(arr, d, n - 1);
 
#def  leftRotate(arr,d,n):
  #reverseArray(arr, 0, d); 
  #reverseArray(arr, d+1, n); 
  #reverseArray(arr, 0, n);

class Solution(object):
    def reverseArray(self,arr,start,end):
        arr[start:end+1] = arr[start:end+1][::-1]
        arr[start:end+1] = arr[start:end+1][::-1]
        arr[start:end+1] = arr[start:end+1][::-1]
        
    def rotate(self, nums, k):
        k = k%len(nums)
        n = len(nums)
        d = k
        self.reverseArray(nums, 0, n - 1) 
        self.reverseArray(nums, 0, d - 1) 
        self.reverseArray(nums, d, n - 1)
    

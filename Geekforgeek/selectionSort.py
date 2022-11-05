#User function Template for python3

class Solution: 
    def select(self, arr, i):
        for i in range(len(arr)):
            return arr[i]
        # code here 
      
    
    def selectionSort(self, arr,n):
        l = len(arr)
        for i in range(l):
            minIndex = i
            for j in range(i+1, len(arr)):
                if arr[minIndex] > arr[j]:
                    minIndex = j
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
        
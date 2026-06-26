class Solution:
    def maxHeapify(self, nums: List[int], n: int, i: int):
        while True:
            l = 2*i+1
            r = 2*i+2
            largest = i
            if l < n and nums[l] > nums[largest]:
                largest = l
            if r < n and nums[r] > nums[largest]:
                largest = r
            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                i = largest
            else:
                break

    def buildMaxHeap(self, nums: List[int]):
        n = len(nums)
        p = (n - 2)//2
        for i in range(p, -1, -1):
            self.maxHeapify(nums, n, i)
    
    def heapSort(self, nums: List[int]):
        self.buildMaxHeap(nums)
        for i in range(len(nums)-1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.maxHeapify(nums, i, 0)
        
    def sortArray(self, nums: List[int]) -> List[int]:
        self.heapSort(nums)
        return nums
        
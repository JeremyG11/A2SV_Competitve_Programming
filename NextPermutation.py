class Solution:
    def reverser(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        maxLength = len(nums)
        index = -1
        for i in range(maxLength -1, 0, -1):
            if nums[i] > nums[i-1]:
                index = i -1
                break
        if index == -1:
            self.reverser(nums, 0, maxLength-1)
            return
        j = maxLength - 1

        for k in range(maxLength-1, index, -1):

            if nums[k] > nums[index]:
                j = k
                break
        nums[index], nums[j] = nums[j], nums[index]

        self.reverser(nums, index + 1, maxLength-1)

        return nums


y = Solution()
nums = [1,2,3]
print( y.nextPermutation(nums))
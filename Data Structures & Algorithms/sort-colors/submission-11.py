class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ## Insetion Sort
        # for i in range(len(nums)):
        #     j = i
        #     while j > 0:
        #         if nums[j] < nums[j-1]:
        #             nums[j],nums[j-1] = nums[j-1],nums[j]
        #         j -= 1
        
        # print(nums)

        # #Bubble Sort
        # for i in range(len(nums)-1,0,-1):
        #     for j in range(0,len(nums)-1):
        #         if nums[j] > nums[j+1]:
        #             nums[j],nums[j+1] = nums[j+1],nums[j]
        # print(nums)

        #Selection Sort
        for i in range(len(nums)):
            mini = i
            for j in range(i,len(nums)):
                if nums[j] < nums[mini]:
                    mini = j
            nums[i],nums[mini] = nums[mini],nums[i]
        print(nums)









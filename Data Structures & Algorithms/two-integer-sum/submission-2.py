class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tab= []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target and i !=j:
                    tab.append(i)
                    tab.append(j)
        return tab
                   


    
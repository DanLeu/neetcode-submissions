class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list_len = len(nums)

        for element_1 in range (list_len):
            for element_2 in range(element_1+1, list_len):
                if (nums[element_1]+nums[element_2]) == target:
                    return [element_1, element_2]
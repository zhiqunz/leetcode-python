"""
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index, i in enumerate(nums):
            if (target - i) in nums[index + 1:]:
                return [index, nums.index(target - i)]

    def towSum_dct(self, nums, target):
        """
                :type nums: List[int]
                :type target: int
                :rtype: List[int]
        """
        tmp_dct = {}
        for index, i in enumerate(nums):
            if target - i in tmp_dct:
                return [tmp_dct[target - i], index]

            tmp_dct[i] = index


if __name__ == "__main__":
    nums = [3, 2, 4]
    nums_1 = [2, 7, 11, 15]
    target = 6
    target_1 = 9
    solution = Solution()
    answer = solution.towSum_dct(nums, target)
    answer_1 = solution.towSum_dct(nums_1, target_1)
    print(answer)
    print(answer_1)

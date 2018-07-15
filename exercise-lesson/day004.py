"""
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2 。

请找出这两个有序数组的中位数。要求算法的时间复杂度为 O(log (m+n)) 。

示例 1:

nums1 = [1, 3]
nums2 = [2]

中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

中位数是 (2 + 3)/2 = 2.5
"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # 长的数组放在nums1
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        nums1_len = len(nums1)
        nums1_cut = nums1_len // 2 -1
        nums2_len = len(nums2)
        nums2_cut = nums2_len // 2 -1
        total_len = nums1_len + nums2_len
        odd_flg = False
        if total_len % 2 == 0:
            mid = total_len / 2 -1
        else:
            odd_flg = True
            mid = (total_len + 1) / 2 -1
        while nums2_cut != 0 and nums1_cut != 0:
            if nums1[mid] < nums2[nums2_cut]:
                if nums2_cut == 1:
                    nums2_cut == 0

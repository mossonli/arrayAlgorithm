#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Mosson"
"""
给定一个整数类型的数组 nums，请编写一个能够返回数组“中心索引”的方法。
我们是这样定义数组中心索引的：数组中心索引的左侧所有元素相加的和等于右侧所有元素相加的和。
如果数组不存在中心索引，那么我们应该返回 -1。如果数组有多个中心索引，那么我们应该返回最靠近左边的那一个。
输入: 
nums = [1, 7, 3, 6, 5, 6]
输出: 3
解释: 
索引3 (nums[3] = 6) 的左侧数之和(1 + 7 + 3 = 11)，与右侧数之和(5 + 6 = 11)相等。
同时, 3 也是第一个符合要求的中心索引。

输入: 
nums = [1, 2, 3]
输出: -1
解释: 
数组中不存在满足此条件的中心索引。
"""

# 解法1
class Solution(object):
    def pivotIndex(self, nums):
        len_nums = len(nums)
        if len_nums <= 0 or len_nums > 10000:
            return -1
        if max(nums) > 1000 or min(nums) < -1000:
            return -1
        for k,v in enumerate(nums):
            left, right = nums[0:k], nums[k+1:len_nums]
            if sum(left) == sum(right):
                return k
        return -1

# num1 = [1, 7, 3, 8, 6, 5, 6, 8]
# ret1 = Solution()
# key1 = ret1.pivotIndex(num1)
# print(key1)

# # 解法2
# class Solution2(object):
#     def pivotIndex(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         len_nums = len(nums)
#         if len_nums <= 0 or len_nums > 10000:
#             return -1
#         if max(nums) > 1000 or min(nums) < -1000:
#             return -1
#
#         sum_list = sum(nums)
#         left = 0
#         for k, v in enumerate(nums):
#             left += v
#             if k+1 >= len_nums:
#                 return -1
#             elif (left * 2 + nums[k+1]) == sum_list:
#                 return k
#         return -1
#
# #
# # num2 = [1, 7, 3, 8, 6, 5, 6, 8]
# num2 = [-1,-1,-1,-1,-1,-1]
# ret2 = Solution2()
# key2 = ret2.pivotIndex(num2)
# print(key2)

# 解法三：
class Solution(object):
    """
    时间复杂度：O(N)O(N)，其中 NN 是 nums 的长度。
    空间复杂度：O(1)O(1)，使用了 S 和 leftsum
    """
    def pivotIndex(self, nums):
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum - x):
                return i
            leftsum += x
        return -1

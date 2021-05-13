"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]



解题思路：
在遍历的同时，记录一些信息，以省去一层循环，这是“以空间换时间”的想法
使用哈希表，不但可以快速从数组nums中寻找是否存在目标元素target - x和目标元素的索引，而且可以将方法一中寻找数组nums是否存在target - x的时间复杂度从O(n)降低到O(1)
需要注意的是，对于每一个x，需要先查询哈希表中是否存在target - x，然后再将x插入到哈希表中，即可确保不会让x与自己匹配

"""
class Solution:
    def twoSum(self, nums, target):
        ret_map = {}
        for i in range(len(nums)):
            ret = target - nums[i]
            if ret in ret_map:
                return [ret_map[ret], i]
            ret_map[nums[i]] = i







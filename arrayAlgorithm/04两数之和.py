"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍

给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""
# 我的
class Solution1:
    def twoSum(self, nums, target):

        for i in range(len(nums)):
            other = target - nums[i]
            for j in range(1, len(nums)-1):
                if nums[j] == other:
                    print(i, j)

# 答案
class Solution:
    # @return a tuple, (index1, index2)
    # 8:42
    def twoSum(self, num, target):
        map = {}
        for i in range(len(num)):
            if num[i] not in map:
                map[target - num[i]] = i
                print(map)
            else:
                print(map, "===")
                return map[num[i]], i
        return -1, -1
ret = Solution()
r = ret.twoSum([3 ,4, 11, 4, 5], 8)
print(r)


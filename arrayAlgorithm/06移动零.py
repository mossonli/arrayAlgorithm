"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
示例:
输入: [1,0,3,12]
输出: [1,3,12,0,0]

说明:
必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
"""


class Solution:

    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        训练营的做法
        """
        tag = 0 # 非0数的计数器[也就是0位置的索引标记]
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[tag] = nums[i] # 将非元素记录到 tag 这个位置
                if i != tag:        # 如果索引tag 不等于 i
                    nums[i] = 0
                tag += 1
        print(tag)
        print(nums)
    def m2(self, nums):
        """
        n^2 的时间复杂度，比较低效
        :param nums:
        :return:
        """
        for i in nums:
            if i == 0:
                nums.remove(i)
                nums.append(i)
    def m3(self, nums):
        """
        和训练营的做法类似
        :param nums:
        :return:
        """
        z = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i],nums[z] = nums[z], nums[i]
                z+=1
        print(nums)
s = Solution()
s.moveZeroes([0,1,0,3,12])
s.m3([1, 0, 2, 18, 0, 12, 0, 10])





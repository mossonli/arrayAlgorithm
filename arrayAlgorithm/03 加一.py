#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Mosson"
"""
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:
输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。

示例 2:
输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。
"""
class Solution(object):
    def plusOne(self, digits):
        for i in range(len(digits)):
            if digits[-1 - i] == 9:
                print(digits[-1 - i])
                digits[-1 - i] = 0
                if -1-i == -len(digits):
                    digits[-1 - i] = 1
                    digits.append(0)
                    return digits
            else:
                digits[-1 - i] += 1
                return digits

ret = Solution()
print(ret.plusOne([9, 9, 9]))


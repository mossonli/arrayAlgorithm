"""
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
说明：你不能倾斜容器，且 n 的值至少为 2。
[1,8,6,2,5,4,8,3,7]
"""

# 方法1 枚举实现
"""
left bar x
right bar y
面积：(x-y)*height_diff
时间复杂度未 n^2
"""
a = [1,8,6,2,5,4,8,3,7] # 高度
max_area = 0
for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        area = (j-i) * min(a[i], a[j])
        max_area = max(max_area, area)
print(max_area)

# 方法2 由外往内部收敛
"""
O(n)
"""
class Solution:
    def maxArea(self, height) -> int:
        max_Area = 0
        left = 0
        right = len(height) -1
        h = 0
        while left < right:
            w = right - left                    # 宽度
            if height[left] < height[right]:
                h = height[left]
                left += 1
            else:
                h = height[right]
                right -= 1
            Area = h * w
            if max_Area < Area:
                max_Area = Area
        return max_Area


















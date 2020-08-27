"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

上到第n阶台阶，只能有两种走法从第n-1阶上去或者是从第n-2阶上去
f(n) = f(n-1)+f(n-2)    也就是斐波那契数列
开一个数组
a = [,,,,,]
for i in range(len(a)-1):
    a[i] = a[i-1] + a[i-2]
"""

class Solution:
    def climbStairs(self, n):
        if n <= 2: return n
        f1, f2, f3 = 1, 2, 3
        for i in range(3, n+1):
            f3 = f1+f2
            f1 = f2
            f2 = f3
        return f3


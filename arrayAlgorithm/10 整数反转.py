"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
输入: 123
输出: 321
输入: -123
输出: -321
输入: 120
输出: 21
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
// 商
% 余数
"""
def reverse(x):
    y = abs(x)
    res = 0
    boundary = (1<<31)-1 if x>0 else (1<<31)
    while y != 0:
        res = res*10 + y%10
        if res > boundary:
            return 0
        y = y // 10 # 商
    return res if res > 0 else -res

ret = reverse(34564)
print(ret)

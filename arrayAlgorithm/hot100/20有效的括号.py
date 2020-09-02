"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true

利用栈 先进后出
"""
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'{': '}', '[': ']', '(': ')'}
        if len(s) % 2 != 0:
            return False
        # 声明一个栈
        stack = []
        for i in s:
            if i in dic:
                stack.append(i)
            elif dic[stack.pop()] != i:
                return False

        return len(stack) == 1


s = Solution()
ret = s.isValid("{[]}[]")
print(ret)


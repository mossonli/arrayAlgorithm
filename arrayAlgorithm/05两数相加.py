"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""

"""
标签：链表
将两个链表看成是相同长度的进行遍历，如果一个链表较短则在前面补 00，比如 987 + 23 = 987 + 023 = 1010
每一位计算的同时需要考虑上一位的进位问题，而当前位计算结束后同样需要更新进位值
如果两个链表全部遍历完毕后，进位值为 11，则在新链表最前方添加节点 11
小技巧：对于链表问题，返回结果为头结点时，通常需要先初始化一个预先指针 pre，该指针的下一个节点指向真正的头结点head。
使用预先指针的目的在于链表初始化时无可用节点值，而且链表构造过程需要指针移动，进而会导致头指针丢失，无法返回结果。
"""

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         l3 = ListNode(0)
#         head = l3
#         step = 0
#         while l1 or l2:
#             x = l1.val if l1 else 0
#             y = l2.val if l2 else 0
#
#             result = x + y + step
#             step = result // 10
#
#             head.next = ListNode(result % 10)
#             head = head.next
#             l1 = l1.next if l1 else None
#             l2 = l2.next if l2 else None
#
#         if step == 1:
#             head.next = ListNode(1)
#
#         return l3.next

menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车站':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}
# while True:
#     for i in menu:print(i)
#     one = input(">:")
#     if one == "q":break
#     if one == "b":continue
#     for j in menu[one]:print(j)
#     two = input(">>:")
#     if two == "q": break
#     if two == "b": continue
#     for j in menu[one][two]: print(j)
#     three = input(">>>:")
#     if three == "q": break
#     if three == "b": continue
#     for j in menu[one][two][three]: print(j)

dic = {"k1": "v1v1", "k2": [11,22,33,44]}

def func(i):  # i为所传字典

    for k, v in i.items():
        if len(v) > 2:
            dic[k] = v[:2]
        else:
            continue
    return i


print(func(dic))















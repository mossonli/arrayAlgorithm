"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

思路：
    先将342逆序数字存储到链表中【也就是先存2 再存 4 再存 3】
"""

"""
标签：链表
将两个链表看成是相同长度的进行遍历，如果一个链表较短则在前面补 00，比如 987 + 23 = 987 + 023 = 1010
每一位计算的同时需要考虑上一位的进位问题，而当前位计算结束后同样需要更新进位值
如果两个链表全部遍历完毕后，进位值为 11，则在新链表最前方添加节点 11
小技巧：对于链表问题，返回结果为头结点时，通常需要先初始化一个预先指针 pre，该指针的下一个节点指向真正的头结点head。
使用预先指针的目的在于链表初始化时无可用节点值，而且链表构造过程需要指针移动，进而会导致头指针丢失，无法返回结果。
"""


class ListNode:
    """
    链表汇总保存数值以及节点的指向
    """

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    542
    465
    1007
    """
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = p = ListNode(None)  # 创建辅助结点 dummy和p都是辅助结点的名称，
        # dummy 是值为空的头结点，dummy的下一个结点就是新建的链表
        # 声明两个 链表对象 dummy和p，p参与while运算[参与运算指针结点位置就会发生变化]，
        # 你可以debug查看其实链表p就是咱们要的结果，但是在while循环中一此次的next将链表的指针位置发生变化，dummy是一个完整的链表，第一个元素是None
        s = 0  # 每一步求和的暂存变量
        print(dummy, "1=============")
        while l1 or l2 or s:
            s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            p.next = ListNode(s % 10)  # 构建新的list存储结果，其实用较长的加数链表也可以表示，%10求个位
            p = p.next
            s = s // 10  # 商
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            # 为什么会返回dummy.next，因为前面声明dummy和p的时候都是复制一个空的链表，返回dummy.next是为了去掉一个None
        return dummy.next

if __name__ == '__main__':

    s = Solution()

    # 链表1
    l1 = ListNode(2)
    l1.next = l11 = ListNode(4)
    l11.next = l12 = ListNode(5)
    print("创建链表l1", l1)
    # 链表2
    l2 = ListNode(5)
    l2.next = l21 = ListNode(6)
    l21.next = l22 = ListNode(4)
    print("创建链表l2", l1)

    ret = s.addTwoNumbers(l1, l2)
    print(ret, "ret -----")
    while ret:
        print("ret", ret)
        print("ret val", ret.val)
        print("ret next", ret.next)
        ret = ret.next

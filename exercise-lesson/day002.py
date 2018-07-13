"""
给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def get_next(self):
        if self.next is not None:
            return self.next
        else:
            return None

    def __repr__(self):
        if self.next is None:
            return str(self.val)
        else:
            return str(self.val) + "->" + repr(self.get_next())


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = None
        carry = 0
        # 循环条件 l1还有下一个 或者 l2还有下一个 或者 前一回相加的结果有进位
        while l1 or l2 or carry:
            add_result = getattr(l1, 'val', 0) + getattr(l2, 'val', 0) + carry
            # 进位处理
            if add_result >=10:
                carry = int(add_result / 10)
                lst_current = ListNode(add_result % 10)
            else:
                carry = 0
                lst_current = ListNode(add_result)
            # 第一次运行时，当前节点保存在result，否则保存在上一个的next
            if result is None:
                result = lst_current
            else:
                lst_previous.next = lst_current

            lst_previous = lst_current

            l1 = getattr(l1, 'next', None)
            l2 = getattr(l2, 'next', None)

        return result


def get_lst(num):
    num_str = str(num)
    l1 = None
    for i in num_str:
        lst_tmp = ListNode(int(i))
        if l1 is not None:
            lst_tmp.next = l1
        l1 = lst_tmp

    return l1


if __name__ == "__main__":
    lst1 = get_lst(5)
    lst2 = get_lst(5)
    s1 = Solution()
    lst3 = s1.addTwoNumbers(lst1, lst2)

    print(lst1)
    print(lst2)
    print(lst3)

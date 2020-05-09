# -*- coding: utf-8 -*-
# @Time: 2020/5/9 23:22
# @Author: GraceKoo
# @File: printListFromTailToHead.py
# @Desc:


class ListNode:
    # 链表的构造 初始化
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, list_node: ListNode):
        stack = []
        while list_node:
            stack.append(list_node.val)
            list_node = list_node.next
        # 将栈进行弹出
        # return stack[::-1]
        while stack:
            print(stack.pop())

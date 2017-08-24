# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class TreeNode(object):
    def __init__(self, data, left_child=None, right_child=None):
        self.val = data
        self.left = left_child
        self.right = right_child

class Tree(object):
    def __init__(self):
        self.root = TreeNode()
        self.queue = []
    
    def add(self, data):
        node = TreeNode(data)
        


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code heres
# -*- coding:utf-8 -*-
array = [
    [2,3,4,5,6,7,8,9],
    [3,4,5,6,7,8,9,11],
    [8,9,11,12,13,14,15,18]
]
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        is_inArray = False
        count = 0
        for l in array:
            is_inArray = (target in l)
            if(is_inArray):
            	count += 1
        if(count > 0):
        	is_inArray = True
        return is_inArray

def main():
    s = Solution()
    print(s.Find(7, array))

if __name__ == '__main__':
    main()

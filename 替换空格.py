# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        new_s = ''
        for i in s:
            if(i == " "):
                i = "%20"
                new_s += i
            else:
                new_s += i
        return new_s

def main():
    s = Solution()
    s.replaceSpace("hello world   ")

if __name__ == '__main__':
    main()

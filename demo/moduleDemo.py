' a test module '

__author__ = 'Tallulah Yang'

import sys

def test():
    args = sys.argv
    if len(args)==1:
            print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    #if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试
    test()
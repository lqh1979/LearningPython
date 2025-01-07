# 斐波那契数列模块

_author = 'Bobo'
__name__ = 'fibo'
__doc__="""
斐波那契数列模块
"""
def fib(n):
    """
       打印斐波那契数列

       参数:
       n (int): 斐波那契数列的最大值。
    """
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):
    """
       返回斐波那契数列

       参数:
       n (int): 斐波那契数列的最大值。
       """
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))

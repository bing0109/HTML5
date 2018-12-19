#coding=utf8

'''
1.有这样一个数列：1,1,2,3,5,8,13,21,34,....求出第30位的数值和递推公式，用python或伪代码答题

2,求以下表达式的值：1-2+3-4+5-6+7-8....+m,并写出递推公式，用python或伪代码答题

3. 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
'''


# 1


# 这个函数用到了递归，容易产生栈溢出，而且速度慢
def calcu(index_num):
    if index_num <= 2:
        number = 1
        return number
    else:
        number = calcu(index_num-1) + calcu(index_num-2)
        return number


# 这个函数避免了递归，不会栈溢出，速度快，推荐用这个
def calcu2(n):
    result = [1, 1]
    if n <= 2:
        number = 1
        return number
    else:
        i = 2
        while i < n:
            result.append((result[i-1]+result[i-2]))
            i += 1
        return result.pop()


num = calcu2(50)
print(num)

'''
推导式
n       num
1       1
2       1
3       2   num = n3 = n2 + n1
4       3   num = n4 = n3 + n2 = 2*n2 + n1
5       5   num = n5 = n4 + n3 = 3*n2 + 2*n1
6       8   num = n6 = n5 + n4 = 5*n2 + 3*n1
7       13  num = n7 = n6 + n5 = 8*n2 + 5*n1

n                                (n%2 + 1) + 1 
。。。。。。看了网上的资料，好像很麻烦
'''


# 2、求以下表达式的值：1-2+3-4+5-6+7-8....+m,并写出递推公式，用python或伪代码答题

def calcu3(num):
    if num == 1:
        return 1
    if num > 1:
        l = [1]
        for i in range(2, num+1):
            if i % 2 == 0:
                l.append(l[i-2] - i)
            else:
                l.append(l[i-2] + i)
        print(l)
        return l.pop()

print(calcu3(17))

'''
推导式
m位正整数
当n=2m-1时    num = (n-1)/2 +1
当n=2m时      num = -n/2
'''


# 3、一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）

class Anm():
    def __init__(self, n, m):
        self.m = int(m)
        self.n = int(n)
    def cal_anm(self):
        a = 1
        b = 1

        for i in range((self.n-self.m+1), self.n+1):
            a *= i
        for i in range(1, (self.m+1)):
            b *= i
        print(a,b,'---2525--')
        return a/b





def calcu4(n):
    l = []
    num = 0
    for k in range(0, n+1):
        if (n-k) % 2 == 0:
            l.append([k, (n-k)/2])

    for i in l:
        a = Anm(i[0]+i[1], i[1])
        num += a.cal_anm()
    print(l)
    return int(num)

print(calcu4(14), '----444----')

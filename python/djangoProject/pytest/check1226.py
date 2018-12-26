# coding=utf8

# 等待时间悖论
import random

d = [0, 0]
while d[1] < 50000:
    a = random.randint(0, 20)
    b = random.randint(10, 30)
    c = random.randint(0, 10)
    d[1] += 1
    if c <= a:
        d[0] += a-c

    if c > a:
        d[0] += b-c

    vag = d[0]/d[1]

print(vag)

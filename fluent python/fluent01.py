from collections import namedtuple as nt
from collections import deque as dq
import time
import datetime

Months = nt('month', 'year')
month_q = dq('Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split())
curr_mo = month_q.pop()
month_q.appendleft(curr_mo)
month_l = list('Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split())
print month_l

today = datetime.datetime.now()
curr_mo = today.strftime('%b')
mo = ''
while(mo != curr_mo):
    mo = month_l.pop()
    month_l.insert(0, mo)

print month_l

LastThree = month_l[9:12]
LastOne = month_l[-1:]

print 'LastThree are ', LastThree
print 'LastOne is ', LastOne

t = (2000, 1, 21, 1, 2, 3, 4, 5, 6)
t = time.mktime(t)
print time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t))
t = (2000, 2, 21, 1, 2, 3, 4, 5, 6)
t = time.mktime(t)
print time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t))
t = (2000, 3, 21, 1, 2, 3, 4, 5, 6)
t = time.mktime(t)
print time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t))
t = (2000, 4, 21, 1, 2, 3, 4, 5, 6)
t = time.mktime(t)
print time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t))
t = (2000, 5, 21, 1, 2, 3, 4, 5, 6)
t = time.mktime(t)
print time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t))
t = (2000, 6, 21, 1, 2, 3, 4, 5, 6)
t = time.mktime(t)
print time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t))
t = (2000, 7, 21, 1, 2, 3, 4, 5, 6)
t = time.mktime(t)
print time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t))
t = (2000, 8, 21, 1, 2, 3, 4, 5, 6)
t = time.mktime(t)
print time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t))
t = (2000, 9, 21, 1, 2, 3, 4, 5, 6)
t = time.mktime(t)
print time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t))
t = (2000, 10, 21, 1, 2, 3, 4, 5, 6)
t = time.mktime(t)
print time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t))
t = (2000, 11, 21, 1, 2, 3, 4, 5, 6)
t = time.mktime(t)
print time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t))
t = (2000, 12, 21, 1, 2, 3, 4, 5, 6)
t = time.mktime(t)
print time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t))


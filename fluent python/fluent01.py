from collections import namedtuple as nt
from collections import deque as dq

Months = nt('Months', 'month year')

month_q = dq('Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split())

print month_q

curr_mo = month_q.pop()

month_q.appendleft(curr_mo)

print  month_q
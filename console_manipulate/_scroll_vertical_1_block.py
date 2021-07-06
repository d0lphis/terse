import sys, time
from outputs import *

arr = str1.splitlines()
length = len(arr)

spanRow = 6

i = 0
while True:
    s = '                                                                           '
    for i in range(0, spanRow):
        sys.stdout.write('{}{}\n'.format(arr[i], s))
    # sys.stdout.write('{} {}'.format(i, i%3 == 0))
    sys.stdout.flush()
    arr.pop(0)
    if len(arr) >= spanRow:
        sys.stdout.write('\033[{}A\r'.format(spanRow))
    else:
        break
    time.sleep(0.2)

# i = 1
# for line in str1.splitlines():
#     if not i % 3:
#         sys.stdout.write('\033[{}A\r'.format(1))
#     sys.stdout.write('{}\n'.format(line))
#     sys.stdout.flush()
#     time.sleep(1)
#     i = i + 1


# for line in str1.splitlines():
#     sys.stdout.write('\r{}'.format(line))
#     sys.stdout.flush()
#     time.sleep(1)

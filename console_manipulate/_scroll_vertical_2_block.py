import sys, time
from outputs import *

arr1 = str1.splitlines()
arr2 = str2.splitlines()

spanWidth = 230
spanHeight = 9

i = 0
while True:
    s = ' '
    splitLine = '-------------------------------------------------------------------'

    if len(arr1) >= spanHeight:
      for i in range(0, spanHeight):
        lineStr = arr1[i]
        sys.stdout.write('{}{}\n'.format(lineStr, s*(spanWidth-len(lineStr))))
      arr1.pop(0)
      sys.stdout.write('{}\n'.format(splitLine))

    if len(arr2) >= spanHeight:
      for i in range(0, spanHeight):
        lineStr = arr2[i]
        sys.stdout.write('{}{}\n'.format(lineStr, s*(spanWidth-len(lineStr))))
      arr2.pop(0)

    sys.stdout.flush()

    if len(arr1) >= spanHeight:
        sys.stdout.write('\033[{}A\r'.format(spanHeight*2+1))
    elif len(arr1) < spanHeight and len(arr2) >= spanHeight:
        sys.stdout.write('\033[{}A\r'.format(spanHeight))
    elif len(arr1) < spanHeight and len(arr2) < spanHeight:
        break
    time.sleep(0.1)

# i = 1
# for line in str.splitlines():
#     if not i % 3:
#         sys.stdout.write('\033[{}A\r'.format(1))
#     sys.stdout.write('{}\n'.format(line))
#     sys.stdout.flush()
#     time.sleep(1)
#     i = i + 1


# for line in str.splitlines():
#     sys.stdout.write('\r{}'.format(line))
#     sys.stdout.flush()
#     time.sleep(1)

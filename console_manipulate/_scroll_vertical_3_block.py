import sys, time
from outputs import *

arr1 = str1.splitlines()
arr2 = str2.splitlines()
arr3 = str3.splitlines()

spanWidth = 230
spanHeight = 9

s = ' '
splitLine = '-------------------------------------------------------------------'

i = 0
try:
  while True:
    for i in range(0, spanHeight):
      lineStr = arr1[i]
      sys.stdout.write('{}{}\n'.format(lineStr, s*(spanWidth-len(lineStr))))
    sys.stdout.write('{}{}\n'.format(splitLine, s*(spanWidth-len(splitLine))))
    for i in range(0, spanHeight):
      lineStr = arr2[i]
      sys.stdout.write('{}{}\n'.format(lineStr, s*(spanWidth-len(lineStr))))
    sys.stdout.write('{}{}\n'.format(splitLine, s*(spanWidth-len(splitLine))))
    for i in range(0, spanHeight):
      lineStr = arr3[i]
      sys.stdout.write('{}{}\n'.format(lineStr, s*(spanWidth-len(lineStr))))
    sys.stdout.flush()

    if len(arr1) > spanHeight:
      arr1.pop(0)
    if len(arr2) > spanHeight:
      arr2.pop(0)
    if len(arr3) > spanHeight:
      arr3.pop(0)
    if len(arr1) == spanHeight and len(arr2) == spanHeight and len(arr3) == spanHeight:
      break
    else:
      sys.stdout.write('\033[{}A\r'.format(spanHeight*3+2))

    time.sleep(0.1)
except KeyboardInterrupt:
  sys.stdout.write('\033[{}B\r'.format(spanHeight*3+2))


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

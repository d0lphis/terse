# coding=utf-8

import os, sys, time
from outputs import *

# sys.stdout.write('{}{}\n'.format('\n', '#'*(270-len('\n'))))
# sys.stdout.write('{}{}\n'.format('', '#'*(270-len(''))))
# sys.stdout.write('{}\n'.format(len('')))
# sys.exit()

# sys.stdout.write('{}\n'.format('#'*270))
# sys.stdout.write('{}{}\n'.format('\n', '#'*(270-len('\n'))))
# sys.stdout.write('{}'.format('qqq'))
# sys.exit()

# while True:
#   sys.stdout.write('{}\n'.format('#'*270))
#   sys.stdout.write('{}{}\n'.format('\n', '#'*(270-len('\n'))))
#   sys.stdout.write('{}'.format('qqq'))
# sys.exit()



rows, columns = os.popen('stty size', 'r').read().split()

consoleWidth = int(columns)
spanHeight = 12
emptyMaskChar = ' '
splitLineChar = '─'
lps = 0
fps = 0.1

def WriteSpannedInfoToConsole(outputArray, w=consoleWidth, h=spanHeight):
  for x in range(0, h):
    lineStr = outputArray[x].replace('\t', '  ')
    sys.stdout.write('{}{}\n'.format(lineStr, emptyMaskChar*(w-len(lineStr))))

    time.sleep(lps)
  if len(outputArray) > h:
    outputArray.pop(0)
    # print(outputArray)
  return outputArray




dict = {
  0:str1.splitlines(),
  1:str2.splitlines(),
  2:str3.splitlines(),
}

try:
  while True:
    for i in dict:
      sys.stdout.write('{}\n'.format(splitLineChar*consoleWidth))
      dict[i] = WriteSpannedInfoToConsole(dict[i])

    allElemementPopDone = True
    for j in dict:
      if len(dict[j]) > spanHeight:
        allElemementPopDone = False
    if allElemementPopDone == True:
      break
    else:
      sys.stdout.write('\033[{}A\r'.format((spanHeight+1)*len(dict)))

    time.sleep(fps)
except KeyboardInterrupt:
  # sys.stdout.write('\033[{}B\r'.format(spanHeight*3+3))
  sys.exit()

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

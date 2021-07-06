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

console_width = int(columns)
span_height = 12
empty_mask_char = ' '
split_line_char = '─'
lps = 0
fps = 0.1

def write_spanned_info_to_console(output_array, w=console_width, h=span_height):
  for x in range(0, h):
    line_str = output_array[x].replace('\t', '  ')
    sys.stdout.write('{}{}\n'.format(line_str, empty_mask_char*(w-len(line_str))))

    time.sleep(lps)
  if len(output_array) > h:
    output_array.pop(0)
    # print(output_array)
  return output_array




dict = {
  0:str1.splitlines(),
  1:str2.splitlines(),
  2:str3.splitlines(),
}

try:
  while True:
    for i in dict:
      sys.stdout.write('{}\n'.format(split_line_char*console_width))
      dict[i] = write_spanned_info_to_console(dict[i])

    all_elemement_pop_done = True
    for j in dict:
      if len(dict[j]) > span_height:
        all_elemement_pop_done = False
    if all_elemement_pop_done == True:
      break
    else:
      sys.stdout.write('\033[{}A\r'.format((span_height+1)*len(dict)))

    time.sleep(fps)
except KeyboardInterrupt:
  sys.stdout.write('\033[{}B\r'.format(span_height*3+3))
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






# import time
# from multiprocessing import Process, Lock
# def print_with_lock(loc, i):
#     loc.acquire()
#     try:
#         print('hello world ', i)
#         time.sleep(1)
#     finally:
#         loc.release()
# if __name__ == '__main__':
#     lock = Lock()
#     for num in range(6):
#         p = Process(target=print_with_lock, args=(lock, num))
#         p.start()
#         p.join()
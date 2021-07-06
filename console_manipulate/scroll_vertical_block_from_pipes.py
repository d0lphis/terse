# coding=utf-8

import os, sys, time, subprocess, shlex
from outputs import *



rows, columns = os.popen('stty size', 'r').read().split()

console_width = int(columns)
span_height = 12
empty_mask_char = ' '
split_line_char = '─'
lps = 0
fps = 0.1

def write_spanned_info_to_console(output_array, w=console_width, h=span_height):
  arr_count = len(output_array)
  for x in range(0, h):
    if x < arr_count:
      line_str = output_array[x].replace('\t', '  ')
    else:
      line_str = ''
    sys.stdout.write('{}{}\n'.format(line_str, empty_mask_char*(w-len(line_str))))
    time.sleep(lps)
  if len(output_array) > h:
    output_array.pop(0)
    # print(output_array)
  return output_array



cmds = {
  # 0:'pushd /Users/will/Desktop/back/code/ewksp/wkc-glossary-service && git --no-pager show && popd',
  # 1:'pushd /Users/will/Desktop/back/code/ewksp/glossary20-storage && git --no-pager show && popd',
  # 2:'pushd /Users/will/Desktop/back/code/ewksp/wkc-assemblies && git --no-pager show && popd',
  # 0:'pushd /Users/will/Desktop/back/code/ewksp/wkc-glossary-service && git status && popd',
  # 1:'pushd /Users/will/Desktop/back/code/ewksp/glossary20-storage && git status && popd',
  # 2:'pushd /Users/will/Desktop/back/code/ewksp/wkc-assemblies && git status && popd',
  0:'pushd /Users/will/Desktop/back/code/ewksp/wkc-glossary-service && gitlgr -n 20 && echo && popd',
  1:'pushd /Users/will/Desktop/back/code/ewksp/glossary20-storage && gitlgr -n 20 && echo && popd',
  2:'pushd /Users/will/Desktop/back/code/ewksp/wkc-assemblies && gitlgr -n 20 && echo && popd',
  # 0:'ping localhost',
  # 1:'ping 127.0.0.1',
  # 2:'ping 0.0.0.0',
}

procs = {}
lines = {}
for i in cmds:
  procs[i]=subprocess.Popen(cmds[i], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  # procs[i]=subprocess.Popen(shlex.split('ping 9.21.55.53'), stdout=subprocess.PIPE)
  lines[i] = []
#print(procs)



try:
  while True:

    output = {}
    for i in procs:
      output[i] = procs[i].stdout.readline()
      if output[i]:
        out = output[i].rstrip('\n')
        if len(out) > console_width:
          out = out[:(console_width-3)]+'...'
        lines[i].append(out)
    #print(lines)

    for i in lines:
      sys.stdout.write('{}\n'.format(split_line_char*console_width))
      lines[i] = write_spanned_info_to_console(lines[i])

    all_element_pop_done = True
    for i in lines:
      if output[i] or procs[i].poll() is None:
        all_element_pop_done = False
    if all_element_pop_done == True:
      break
    else:
      sys.stdout.write('\033[{}A\r'.format((span_height+1)*len(lines)))

    time.sleep(fps)
except KeyboardInterrupt:
  sys.stdout.write('\033[{}B\r'.format(span_height*3+3))
  sys.exit()
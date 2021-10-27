# coding=utf-8

# $ python git_stats.py -p /Users/will/Desktop/back/code/gwksp/
# elasticsearch-7_10                                           7.10                                     √
# etcd-release_3_4                                             release-3.4                              ▲10
# gita                                                         master                                   ▼16
# hf-hf_trunk                                                  hf_trunk                                 ▲23▼1
# spark-master                                                 master                                   √ ^
# tflow-r_2_4                                                  r2.4                                     ▲8 ^
# api                                                          master                                   ▼29 ^
# wkc-glossary-service-master                                  will_dev                                 ▲274▼12 ^

from __future__ import print_function
import os, sys, time, re, argparse, subprocess, signal
from outputs import *



RED='\033[1;31m'
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
CYAN='\033[1;36m'
LIGHT_PURPLE='\033[1;35m'
NC='\033[0m'
STAT_FORMAT="%b%7s%b %-34s"



parser=argparse.ArgumentParser()
parser.add_argument('-t', '--target', help='branch@remote to check, e.g master@{u}, master@{upstream}')
parser.add_argument('-p', '--repobase', help='path that contains repos')
# parser.add_argument('-b', '--branch', help='local branch to check')
args=parser.parse_args()
# if args.target:
#   print("remote repo: % s" % args.target)
# if args.repobase:
#   print("remote repo: % s" % args.repobase)



def EXECUTE(cmd):
  p=subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  o=p.communicate()
  return {
    'out':str(o[0]),
    'err':str(o[1])
  }

def get_stat_by_rev():
  UPSTREAM='@{u}' if len(sys.argv) <= 1 else sys.argv[2]
  LOCAL=EXECUTE('git rev-parse @')['out']
  REMOTE=EXECUTE('git rev-parse '+UPSTREAM)['out']
  BASE=EXECUTE('git merge-base @ '+UPSTREAM)['out']
  sys.stdout.write(RED + UPSTREAM + NC + '\n')
  sys.stdout.write(GREEN + LOCAL + NC)
  sys.stdout.write(CYAN + REMOTE + NC)
  sys.stdout.write(LIGHT_PURPLE + BASE + NC)

  if LOCAL == REMOTE:
    sys.stdout.write(GREEN+'        ✓ '+NC+' up to date (local remote the same)')
  elif LOCAL == BASE:
    sys.stdout.write(LIGHT_PURPLE+' ▼ '+NC+' behind (others\' changes on upstream repo )')
  elif REMOTE == BASE:
    sys.stdout.write(CYAN+'         ▲ '+NC+' ahead (self changes committed to local repo)')
  else:
    sys.stdout.write(RED+'          ✗ '+NC+' diverged (both local and remote have changes)')

def get_stat_by_status():
  o=EXECUTE('git status')['out']
  out=None
  try:
    if 'Your branch is up to date' in o:
      # Your branch is up to date
      # print('{:8}'.format('✓'))             #✘
      out=GREEN+'√'+NC
    elif 'Your branch is behind' in o:
      #Your branch is behind 'upstream/release-wkc-cypress' by 1 commit, and can be fast-forwarded.
      found=re.search('.*Your branch is behind .* (\d+) commit.*', o)
      # print('▼{:7}'.format(found.group(1))) #⬇
      out=LIGHT_PURPLE+'▼'+found.group(1)+NC
    elif 'Your branch is ahead of' in o:
      #Your branch is ahead of 'upstream/master' by 1 commit.
      found=re.search('.*Your branch is ahead of .* by (\d+) commit.*', o)
      # print('▲{:7}'.format(found.group(1))) #⬆
      out=CYAN+'▲'+found.group(1)+NC
    elif 'have diverged' in o:
      #Your branch and 'upstream/master' have diverged, and have 1 and 4 different commits each, respectively.
      found=re.search('.*and have (\d+) and (\d+) different commits each.*', o)
      # print('▲{:3}▼{:3}'.format(found.group(1), found.group(2)))
      out=CYAN+'▲'+found.group(1)+LIGHT_PURPLE+'▼'+found.group(2)+NC
    return out
  except AttributeError:
    print('behind or ahead count parse error')






exec_script_path=os.path.dirname(os.path.realpath(__file__))
# print(exec_script_path)
# repo_home=os.path.abspath(os.getcwd()) if len(sys.argv) <= 1 else sys.argv[1]
repo_home=args.repobase if args.repobase else os.path.abspath(os.getcwd())
# print(repo_home)

for root, sub_folders, files in os.walk(repo_home):
  for sub_folder in sub_folders:
    sub_path=os.path.join(root, sub_folder)
    if os.path.exists(os.path.join(sub_path, ".git")):
      # print(sub_path)
      os.chdir(sub_path)
      stat=get_stat_by_status()
      branch_name=EXECUTE('git rev-parse --abbrev-ref HEAD')['out'].rstrip('\n')

      if EXECUTE('git status --porcelain')['out']:
        sys.stdout.write('{:60} {:40} {} {}\n'.format(sub_folder, branch_name, stat, YELLOW+'^'+NC))  #ᐃᐱ
        # printf "\n%60s %40s %-30s %b%1s%b %-19s" "$(basename $repo)" "${BARNCH_NAME}" "${GIT_STATUS}" "${RED}" "x" "${NC}" "Uncommitted Changes"
      else:
        sys.stdout.write('{:60} {:40} {}\n'.format(sub_folder, branch_name, stat))
        # printf "\n%60s %40s %-30s"               "$(basename $repo)" "${BARNCH_NAME}" "${GIT_STATUS}"

  #   print(os.path.join(root, sub_folder))
  # for file in files:
  #   print(os.path.join(root, file))
  break


# os.killpg(os.getpgid(pro.pid), signal.SIGTERM)
sys.exit()



rows, columns=os.popen('stty size', 'r').read().split()

console_width=int(columns)
span_height=12
empty_mask_char=' '
split_line_char='─'
lps=0
fps=0.1

def write_spanned_info_to_console(output_array, w=console_width, h=span_height):
  arr_count=len(output_array)
  for x in range(0, h):
    if x < arr_count:
      line_str=output_array[x].replace('\t', '  ')
    else:
      line_str=''
    sys.stdout.write('{}{}\n'.format(line_str, empty_mask_char*(w-len(line_str))))
    time.sleep(lps)
  if len(output_array) > h:
    output_array.pop(0)
    # print(output_array)
  return output_array



cmds={
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

procs={}
lines={}
for i in cmds:
  procs[i]=subprocess.Popen(cmds[i], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  # procs[i]=subprocess.Popen(shlex.split('ping 9.21.55.53'), stdout=subprocess.PIPE)
  lines[i]=[]
#print(procs)



try:
  while True:

    output={}
    for i in procs:
      output[i]=procs[i].stdout.readline()
      if output[i]:
        out=output[i].rstrip('\n')
        if len(out) > console_width:
          out=out[:(console_width-3)]+'...'
        lines[i].append(out)
    #print(lines)

    for i in lines:
      sys.stdout.write('{}\n'.format(split_line_char*console_width))
      lines[i]=write_spanned_info_to_console(lines[i])

    all_element_pop_done=True
    for i in lines:
      if output[i] or procs[i].poll() is None:
        all_element_pop_done=False
    if all_element_pop_done == True:
      break
    else:
      sys.stdout.write('\033[{}A\r'.format((span_height+1)*len(lines)))

    time.sleep(fps)
except KeyboardInterrupt:
  sys.stdout.write('\033[{}B\r'.format(span_height*3+3))
  sys.exit()
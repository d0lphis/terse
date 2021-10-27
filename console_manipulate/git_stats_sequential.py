# coding=utf-8

# $ python git_stats.py -p /code/rwksp -e   #fetch, stat
# $ python git_stats.py -p /code/rwksp -r   #stash, fetch rebase, stash pop, stat
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


LIGHT_RED='\033[1;31m'
RED='\033[1;31m'
BOLD_RED='\033[1m\033[31m'

LIGHT_YELLOW='\033[0;33m'
YELLOW='\033[1;33m'
BOLD_YELLOW='\033[1m\033[33m'

LIGHT_GREEN='\033[1;32m'
GREEN='\033[0;32m'
BOLD_GREEN='\033[1m\033[32m'

LIGHT_CYAN='\033[1;36m'
CYAN='\033[1;36m'
BOLD_CYAN='\033[1m\033[36m'

PURPLE='\033[0;35m'
LIGHT_PURPLE='\033[1;35m'
BOLD_PURPLE='\033[1m\033[35m'

LIGHT_GRAY='\033[0;37m'

NC='\033[0m'

STAT_FORMAT="%b%7s%b %-34s"

ACT_SYMBOL='●'
#⬤⚪⚫🌑⭕🔴🔵〇🔘➰⧭⓿⓪🄋⓵ⓐ🅐Ⓐ
#●◯○⚬•∙
#◓◑◒◐◷◶◴◵◔◕
#⨀⚆⚇⚈⚉⦾⦿◉✪◌❂⦻⊛☢❍☸❏❐❑❒
#〶⨁⨂⊝⊖⊜⦶⦷◍⦸⊘⦹⦺◖◗
#◙◚◛⧇◠◡⟟⫱⧲⧳⦲∅⦵⧂⧃◜◝◞◟
#🌑🌒🌓🌔🌕🌖🌗🌘
#🌕🌖🌗🌘🌑🌒🌓🌔🌕

#http://www.i2symbol.com/symbols/style-letters
#🍀🌿🌵🍃🌱🌾🍂🍁🌺🌸🌹🌷💐🍇🌻🏵🌼💮⚾⚽🏀🏈🎾🎱🚩💯🍺🍹🍻🍷🍸🍵🎺🎻🎷🎸🌟💫🔥💧🌊🌀🌈🍥🍭
#☕ℱℋℌℒ℘ℛ℟℣ℬℭℰℳℵ☡ℴℏℊ℔
import itertools

# for c in itertools.cycle(['|', '/', '-', '\\']):
# for c in itertools.cycle(['⬍', '⬈', '➞', '⬊', '⬍', '⬋', '⬅', '⬉']):
# for c in itertools.cycle(['◜', '◝', '◞', '◟']):
#
# for c in itertools.cycle(['.', '..', '...']):
# for c in itertools.cycle(['.', '..', '...', '..']):
#
# for c in itertools.cycle(['.', 'o', 'O', '@', '*']):
# for c in itertools.cycle(['⚆', '⚇', '◌']):
# for c in itertools.cycle(['☘', '❀', '❁', '❀']):
# for c in itertools.cycle(['⁎', '⁑', '⁂', '⁑']):
# for c in itertools.cycle(['◇', '◈', '◆']):
#
# for c in itertools.cycle(['┤', '┘', '┴', '└', '├', '┌', '┬', '┐']):
# for c in itertools.cycle(['◓', '◑', '◒', '◐']):
# for c in itertools.cycle(['⊖', '⦸', '⦶', '⊘']):
# for c in itertools.cycle(['▖', '▘', '▝', '▗']):
# for c in itertools.cycle(['◢', '◣', '◤', '◥']):
# for c in itertools.cycle(['◴', '◷', '◶', '◵']):
# for c in itertools.cycle(['◰', '◳', '◲', '◱']):
# for c in itertools.cycle(['▌', '▀', '▐', '▄']):
# for c in itertools.cycle(['⣾', '⣽', '⣻', '⢿', '⡿', '⣟', '⣯', '⣷']):
# for c in itertools.cycle(['⠁', '⠂', '⠄', '⡀', '⢀', '⠠', '⠐', '⠈']):
# for c in itertools.cycle(['⡀', '⡁', '⡂', '⡃', '⡄', '⡅', '⡆', '⡇', '⡈', '⡉', '⡊', '⡋', '⡌', '⡍', '⡎', '⡏', '⡐', '⡑', '⡒', '⡓', '⡔', '⡕', '⡖', '⡗', '⡘', '⡙', '⡚', '⡛', '⡜', '⡝', '⡞', '⡟', '⡠', '⡡', '⡢', '⡣', '⡤', '⡥', '⡦', '⡧', '⡨', '⡩', '⡪', '⡫', '⡬', '⡭', '⡮', '⡯', '⡰', '⡱', '⡲', '⡳', '⡴', '⡵', '⡶', '⡷', '⡸', '⡹', '⡺', '⡻', '⡼', '⡽', '⡾', '⡿', '⢀', '⢁', '⢂', '⢃', '⢄', '⢅', '⢆', '⢇', '⢈', '⢉', '⢊', '⢋', '⢌', '⢍', '⢎', '⢏', '⢐', '⢑', '⢒', '⢓', '⢔', '⢕', '⢖', '⢗', '⢘', '⢙', '⢚', '⢛', '⢜', '⢝', '⢞', '⢟', '⢠', '⢡', '⢢', '⢣', '⢤', '⢥', '⢦', '⢧', '⢨', '⢩', '⢪', '⢫', '⢬', '⢭', '⢮', '⢯', '⢰', '⢱', '⢲', '⢳', '⢴', '⢵', '⢶', '⢷', '⢸', '⢹', '⢺', '⢻', '⢼', '⢽', '⢾', '⢿', '⣀', '⣁', '⣂', '⣃', '⣄', '⣅', '⣆', '⣇', '⣈', '⣉', '⣊', '⣋', '⣌', '⣍', '⣎', '⣏', '⣐', '⣑', '⣒', '⣓', '⣔', '⣕', '⣖', '⣗', '⣘', '⣙', '⣚', '⣛', '⣜', '⣝', '⣞', '⣟', '⣠', '⣡', '⣢', '⣣', '⣤', '⣥', '⣦', '⣧', '⣨', '⣩', '⣪', '⣫', '⣬', '⣭', '⣮', '⣯', '⣰', '⣱', '⣲', '⣳', '⣴', '⣵', '⣶', '⣷', '⣸', '⣹', '⣺', '⣻', '⣼', '⣽', '⣾', '⣿']):
#
# for c in itertools.cycle(['▏', '▎', '▍', '▌', '▋', '▊', '▉', '▊', '▋', '▌', '▍', '▎', '▏']):
# for c in itertools.cycle(['▁', '▂', '▃', '▄', '▅', '▆', '▇', '█', '▇', '▆', '▅', '▄', '▃', '▁']):
# for c in itertools.cycle(['▉', '▊', '▋', '▌', '▍', '▎', '▏', '▎', '▍', '▌', '▋', '▊', '▉']):
# for c in itertools.cycle(['︷', '︵', '︹', '︺', '︶', '︸', '︶', '︺', '︹', '︵']):
# for c in itertools.cycle(['◡◡', '⊙⊙', '◠◠']):
# for c in itertools.cycle(['🕛', '🕧', '🕐', '🕜', '🕑', '🕝', '🕒', '🕞', '🕓', '🕟', '🕔', '🕠', '🕕', '🕡', '🕖', '🕢', '🕗', '🕣', '🕘', '🕤', '🕙', '🕥', '🕚', '🕦']):
# for c in itertools.cycle(['🌑', '🌒', '🌓', '🌔', '🌕', '🌖', '🌗', '🌘']):
#   sys.stdout.write('\rloading ' + c + ' ' + c + ' ' + c + ' ' + c + ' ' + c + ' ' + c + ' ' + c + ' ' + c + ' ')
#   sys.stdout.flush()
#   time.sleep(0.1)

# sys.exit()

parser=argparse.ArgumentParser()
parser.add_argument('-t', '--target', help='branch@remote to check, e.g master@{u}, master@{upstream}')
parser.add_argument('-p', '--repobase', help='path that contains repos')
parser.add_argument('-e', '--withfetch', action='store_true', help='fetch before stats')
parser.add_argument('-r', '--withrebase', action='store_true', help='stash, fetch, rebase, stash pop, before stats')
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
    'err':str(o[1]),
    'cod':str(p.returncode)
  }

def get_stat_of_exec(cmd):
  res=EXECUTE(cmd)
  o=res['out']
  e=res['err']
  c=res['cod']
  # sys.stdout.write(o)
  # sys.stdout.write(e)

  # if o != "None":
  #   res="√"
  # if e != "None":
  #   res="x"
  sys.stdout.write(c)

# get_stat_of_exec('git pull upstream spark_trunk')
# sys.exit()

def get_stat_by_git_rev():
  UPSTREAM='@{u}' if len(sys.argv) <= 1 else sys.argv[2]
  LOCAL=EXECUTE('git rev-parse @')['out']
  REMOTE=EXECUTE('git rev-parse '+UPSTREAM)['out']
  BASE=EXECUTE('git merge-base @ '+UPSTREAM)['out']
  sys.stdout.write(BOLD_RED + UPSTREAM + NC + '\n')
  sys.stdout.write(BOLD_GREEN + LOCAL + NC)
  sys.stdout.write(BOLD_CYAN + REMOTE + NC)
  sys.stdout.write(BOLD_PURPLE + BASE + NC)

  if LOCAL == REMOTE:
    sys.stdout.write(BOLD_GREEN+'        ✓ '+NC+' up to date (local remote the same)')
  elif LOCAL == BASE:
    sys.stdout.write(BOLD_PURPLE+' ▼ '+NC+' behind (others\' changes on upstream repo )')
  elif REMOTE == BASE:
    sys.stdout.write(BOLD_CYAN+'         ▲ '+NC+' ahead (self changes committed to local repo)')
  else:
    sys.stdout.write(BOLD_RED+'          ✗ '+NC+' diverged (both local and remote have changes)')

def get_stat_by_git_status():
  o=EXECUTE('git status')['out']
  out=None
  try:
    if 'Your branch is up to date' in o:
      # Your branch is up to date
      # print('{:8}'.format('✓'))             #✘
      out=BOLD_GREEN+'√'+NC
    elif 'Your branch is behind' in o:
      #Your branch is behind 'upstream/release-wkc-cypress' by 1 commit, and can be fast-forwarded.
      found=re.search('.*Your branch is behind .* (\d+) commit.*', o)
      # print('▼{:7}'.format(found.group(1))) #⬇
      out=BOLD_PURPLE+'▼'+found.group(1)+NC
    elif 'Your branch is ahead of' in o:
      #Your branch is ahead of 'upstream/master' by 1 commit.
      found=re.search('.*Your branch is ahead of .* by (\d+) commit.*', o)
      # print('▲{:7}'.format(found.group(1))) #⬆
      out=BOLD_CYAN+'▲'+found.group(1)+NC
    elif 'have diverged' in o:
      #Your branch and 'upstream/master' have diverged, and have 1 and 4 different commits each, respectively.
      found=re.search('.*and have (\d+) and (\d+) different commits each.*', o)
      # print('▲{:3}▼{:3}'.format(found.group(1), found.group(2)))
      out=BOLD_CYAN+'▲'+found.group(1)+BOLD_PURPLE+'▼'+found.group(2)+NC
    elif 'You are currently rebasing branch' in o:
      out=BOLD_RED+'‽'+NC
    return out
  except AttributeError:
    print('behind or ahead count parse error')




exec_script_path=os.path.dirname(os.path.realpath(__file__))
# print(exec_script_path)
# repo_home=os.path.abspath(os.getcwd()) if len(sys.argv) <= 1 else sys.argv[1]
repo_home=args.repobase if args.repobase else os.path.abspath(os.getcwd())
# print(repo_home)

for root, sub_folders, files in os.walk(repo_home):
  for sub_folder in sorted(sub_folders):
    sub_path=os.path.join(root, sub_folder)
    if os.path.exists(os.path.join(sub_path, ".git")):
      # print(sub_path)
      os.chdir(sub_path)

      branch_name=EXECUTE('git rev-parse --abbrev-ref HEAD')['out'].rstrip('\n')



      #EXECUTE('git branch --set-upstream-to=upstream/$(git rev-parse --abbrev-ref HEAD)')



      stat_stash=' '
      if args.withfetch is True or args.withrebase is True:
        res=EXECUTE('git stash')
        if res['cod'] == "0":
          stat_stash=LIGHT_GREEN+ACT_SYMBOL+NC
          if "No local changes to save" in res['out']:
            stat_stash=LIGHT_GRAY+ACT_SYMBOL+NC
        else:
          stat_stash=LIGHT_RED+ACT_SYMBOL+NC

      stat_pull=' '
      if args.withrebase is True:
        if EXECUTE('git pull --rebase upstream $(git rev-parse --abbrev-ref HEAD)')['cod'] == "0":
          stat_pull=LIGHT_GREEN+ACT_SYMBOL+NC
        else:
          stat_pull=LIGHT_RED+ACT_SYMBOL+NC

      #EXECUTE('git push origin $(git rev-parse --abbrev-ref HEAD) -f')

      stat_stash_pop=' '
      if args.withrebase is True:
        res=EXECUTE('git stash pop')
        if res['cod'] == "0":
          stat_stash_pop=LIGHT_GREEN+ACT_SYMBOL+NC
        elif res['cod'] == "1":                     #[1] No stash entries found.
          stat_stash_pop=LIGHT_GRAY+ACT_SYMBOL+NC
        else:                                       #[128] untracked working tree files would be overwritten by merge, aborting...
          stat_stash_pop=LIGHT_RED+ACT_SYMBOL+NC
      
      symbol_for_sync=stat_stash+' '+stat_pull+' '+stat_stash_pop



      stat_status=get_stat_by_git_status()



      has_not_committed_changes=False
      if EXECUTE('git status --porcelain')['out']:
        has_not_committed_changes=True
        stat_status=stat_status+'\t'+BOLD_YELLOW+'^'+NC
      else:
        has_not_committed_changes=False



      sys.stdout.write('{:60} {:40} {} {}\n'.format(sub_folder, branch_name, symbol_for_sync, stat_status))  #ᐃᐱ



        # sys.stdout.write('{:60} {:40} {} {}\n'.format(sub_folder, branch_name, stat_status, BOLD_YELLOW+'^'+NC))  #ᐃᐱ
        # # printf "\n%60s %40s %-30s %b%1s%b %-19s" "$(basename $repo)" "${BARNCH_NAME}" "${GIT_STATUS}" "${BOLD_RED}" "x" "${NC}" "Uncommitted Changes"

        # sys.stdout.write('{:60} {:40} {}\n'.format(sub_folder, branch_name, stat_status))
        # # printf "\n%60s %40s %-30s"               "$(basename $repo)" "${BARNCH_NAME}" "${GIT_STATUS}"

  #   print(os.path.join(root, sub_folder))
  # for file in files:
  #   print(os.path.join(root, file))
  break


# os.killpg(os.getpgid(pro.pid), signal.SIGTERM)
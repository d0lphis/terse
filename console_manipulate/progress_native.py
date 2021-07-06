# coding=utf-8
from __future__ import print_function
from __future__ import division
import sys, time






from time import sleep
def show_percent():
    N=12
    for i in range(N):
        # print(f'{i/N*100:.1f} %', end='\r')
        sys.stdout.write('{0:.1f} %\r'.format(i/N*100))
        sys.stdout.flush()
        sleep(0.5)
    sys.stdout.write('\n')
show_percent()



def show_digital_clock():
    while True:
        localtime = time.localtime()
        result = time.strftime("%I:%M:%S %p", localtime)
        # print(result, end="", flush=True)
        # print("\r", end="", flush=True)
        sys.stdout.write('\r{}'.format(result))
        sys.stdout.flush()
show_digital_clock()






def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()
def show_progress():
    total = 100
    i = 0
    # for i in range(total+1):
    while i <= total:
        progress(i, total, status='Doing very long job')
        i += 5
        time.sleep(0.1)					# emulating long-playing job
    # print("")
    sys.stdout.write('\n')
show_progress()






def progress_color(count, total, status=''):
    red='\033[01;31m'
    gre='\033[02;32m'
    yel='\033[00;33m'
    blu='\033[01;34m'

    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percentage = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)
    
    if percentage <= 50:
        col = red
    elif percentage > 50 and percentage <= 80:
        col = yel
    elif percentage > 80 and percentage <= 99:
        col = gre
    else:
        col = blu

    sys.stdout.write('\r{0}[{1}] {2}%  {3}'.format(col, bar, percentage, status))
    sys.stdout.flush()
def show_progress_color():
    total = 100
    i = 0
    while i <= total:
        progress_color(i, total, status='Doing very long job')
        i += 5
        time.sleep(0.1)					# emulating long-playing job
    sys.stdout.write('\n')
show_progress_color()






def progress_solid (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    # print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    sys.stdout.write('\r{} |{}| {}% {}{}'.format(prefix, bar, percent, suffix, printEnd))
    # Print New Line on Complete
    if iteration == total: 
        print()
def show_progress_solid():
    items = list(range(0, 57))
    l = len(items)

    # Initial call to print 0% progress
    progress_solid(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
    for i, item in enumerate(items):
        progress_solid(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
        time.sleep(0.1)
show_progress_solid()






import random
def show_progress_asterisk_multiline(count):
    all_progress = [0] * count
    sys.stdout.write("\n" * count) # Make sure we have space to draw the bars
    while any(x < 100 for x in all_progress):
        time.sleep(0.000001)
        # Randomly increment one of our progress values
        unfinished = [(i, v) for (i, v) in enumerate(all_progress) if v < 100]
        index, _ = random.choice(unfinished)
        all_progress[index] += 1

        # Draw the progress bars
        sys.stdout.write(u"\u001b[1000D") # Move left
        sys.stdout.write(u"\u001b[" + str(count) + "A") # Move up
        for progress in all_progress: 
            width = int(progress / 1)
            print("[" + "*" * width + " " * (100 - width) + "]")
show_progress_asterisk_multiline(20)
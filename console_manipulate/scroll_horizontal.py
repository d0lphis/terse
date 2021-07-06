import sys, time

def RotateHorizontalShow():
    content=str('Do not judge each day by the harvest you reap but by the seeds that you plant. ')
    while True:
        sys.stdout.write('\r{}'.format(content))
        sys.stdout.flush()
        content = content[1:] + content[0]
        time.sleep(0.1)

RotateHorizontalShow()

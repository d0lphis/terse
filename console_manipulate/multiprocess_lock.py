from __future__ import print_function


# from multiprocessing import Process
# import os, sys

# def f(name):
#     print('{0:<15}'.format('hello '+name), 'module name:', '{0:<15}'.format(__name__), 'parent process:', '{0:<15}'.format(os.getppid()), 'process id:', '{0:<15}'.format(os.getpid()))

# if __name__ == '__main__':
#     for num in range(6):
#         p = Process(target=f, args=('bob '+str(num),))
#         p.start()
#         p.join()
# sys.exit()






import time
from multiprocessing import Process, Lock
def print_with_lock(loc, i):
    loc.acquire()
    try:
        print('hello world ', i)
        time.sleep(1)
    finally:
        loc.release()
if __name__ == '__main__':
    lock = Lock()
    for num in range(6):
        p = Process(target=print_with_lock, args=(lock, num))
        p.start()
        p.join()





# from StringIO import StringIO
# from multiprocessing import Process, Queue
# import sys, time
# # Proxy classes that both write to and capture strings
# # sent to stdout or stderr, respectively.
# class TeeOut(StringIO):
#     def write(self, s):
#         StringIO.write(self, s)
#         sys.__stdout__.write(s)
# class TeeErr(StringIO):
#     def write(self, s):
#         StringIO.write(self, s)
#         sys.__stderr__.write(s)
# class Parent(object):
#     def run(self):
#         # Start child process.
#         queue = Queue()

#         for i in range(3):
#             child = Process(target=self.spawn, args=(queue,))
#             child.start()
#             child.join()
#         # Do someting with out and err...
#         out = queue.get()
#         err = queue.get()
#     def spawn(self, queue):
#         # Save everything that would otherwise go to stdout.
#         out = sys.stdout = TeeOut()
#         err = sys.stderr = TeeErr()

#         try:
#             # Do something...
#             sys.stdout.write('out 1\n')
#             sys.stderr.write('error 1\n')
#         finally:
#             # Restore stdout, stderr and send their contents.
#             sys.stdout = sys.__stdout__
#             sys.stderr = sys.__stderr__
#             queue.put(out.getvalue())
#             queue.put(err.getvalue())
# if __name__ == '__main__':
#     Parent().run()

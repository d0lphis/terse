import sys, time
import multiprocessing
import progress_native_solid


def func(param):
    native_progress.run_progress()
    #time.sleep(1)
    #print param

if __name__ == '__main__':
    print 'starting execution'
    launchTime = time.clock()
    params = range(10)
    pool=multiprocessing.Pool(processes=100) #use N processes to download the data
    _=pool.map(func,params)
    print 'finished'

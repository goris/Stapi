#!/usr/bin/python

import multiprocessing
import stats_worker
import sys, getopt

host = 'localhost';
concurrent = -1

def getArgs(argv):
    global host, concurrent

    try:
        opts, args = getopt.getopt(argv,"hc:s:",["concurrency=","server="])
    except getopt.GetoptError:
        print 'stapi.py -c <concurrency> -s <host> si'
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print 'stapi.py -c <concurrency> -s <host>'
            sys.exit()
        elif opt in ("-c", "--concurrency"):
            concurrent = int(arg)
        elif opt in ("-s", "--server"):
            host = arg
    return

if __name__ == '__main__':

    getArgs(sys.argv[1:])
    print "args: {0}, {1}".format(host, concurrent)

    jobs =  []
    for i in range (concurrent):
        process = multiprocessing.Process(target = stats_worker.worker)
        jobs.append(process)
        process.start()


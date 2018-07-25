import asyncio
import sys
import os
import math
import time
from concurrent.futures import(
    ProcessPoolExecutor, ThreadPoolExecutor, CancelledError)
from concurrent.futures.process import BrokenProcessPool

def is_prime(n):
    if n%2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n+1, 2):
        if n%i == 0:
            return False
        
    return True

class ProcessingSession:
    def __init__(self, config):
        self.runing = True
        self.config = config

        if(config['mode']=='process'):
            self.executor = ProcessPoolExecutor(config['parallel'])
        elif(config['mode']=='thread'):
            self.executor = ThreadPoolExecutor(config['parallel'])
        else:
            errx('Run mode must be either process or thread')

    def run_task_is_prime(self):
        primes = self.config['PRIMES']
        start_time=time.time()
        for number, prime in zip(primes, self.executor.map(is_prime,primes)):
            print('{n} is prime: {result}'.format(n=number,result=prime))
        print('Finished in {}s'.format(time.time()-start_time))



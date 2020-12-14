import os
from multiprocessing import Process
def pe():
    os.system('python -u DataReceiverPE.py')
def fs():
    os.system('python -u DataReceiverFS.py')
if __name__ == '__main__':
    process1 = Process(target=pe)
    process1.start()
    process2 = Process(target=fs)
    process2.start()


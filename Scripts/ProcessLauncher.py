from multiprocessing import Process
from DataGeneratorFS import start as fs
from DataGeneratorPE import start as pe

if __name__ == '__main__':
    process2 = Process(target=fs)
    process2.start()
    process1 = Process(target=pe)
    process1.start()



from thread import Thread
import os
import math
import time

def calc():
    for i in range(4000000):
        math.sqrt(i)

threads = []
cpus = os.cpu_count()
print("Núcleos en tu CPU: ", cpus)
for i in range(cpus):
    print("registrando el hilo %d" % i)
    threads.append(Threads(target = calc))

start = time.time()

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

end = time.time()
print("Se tardó: ", end-start)

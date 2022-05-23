from threading import Thread
from time import sleep


def func():
    for j in range(10):
        print("child thread " + str(10 - j))
        sleep(0.9)
    print("child end")


th = Thread(target=func)
th.start()

for i in range(10):
    print("main thread " + str(10 - i))
    sleep(1)
print("main end")

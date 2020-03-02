

import threading
import time

event = threading.Event()

def lighter():
    count = 0
    event.set()
    while True:
        if count >5 and count < 10:
            event.clear()
            print("\033[41;1mred light is on...\033[0m")
        elif count >10:
            event.set()
            count = 0
        else:
            print("\033[42;1mgreen light is on...\033[0m")

        time.sleep(1)
        count += 1

def car(name):
    while True:
        if event.is_set():#代表是绿灯
            print("[%s] is running ..." %name)
            time.sleep(1)
        else:
            print("[%s]see the red light,waiting...." %name)
            event.wait()
            print("\033[34;1m[%s]green light is on,start..\033[0m")

light = threading.Thread(target=lighter,)
light.start()
car1 = threading.Thread(target=car,args=("宝马",))


car1.start()
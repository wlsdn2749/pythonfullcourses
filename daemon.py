# daemon thread = a thread that runs in background , non-daemon thread cannot normally be killed
#
#                 ex. background tasks, garbage collection, waiting for input, long running process


import threading
import time

def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for: ", count, "seconds") # daemon processing is terminate when main thread end
    

x = threading.Thread(target=timer, daemon=True)
x.start()

# x.setDaemon(True)
print(x.isDaemon())

answer = input("Do you wish to exit?")
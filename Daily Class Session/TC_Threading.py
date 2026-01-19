import threading

def task():
    print("thread is running")
t = threading.Thread(target = task)
t.start()
t.join()

print("main thread ends")
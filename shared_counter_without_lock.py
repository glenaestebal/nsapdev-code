
import time, random, threading

shared_counter_without_lock = 0
count = 15

def increment_without_lock(thread_ID):
    global shared_counter_without_lock
    for i in range (count):
        local = shared_counter_without_lock
        local += 1
        time.sleep(random.randint(0,2))
        shared_counter_without_lock = local
        print("Thread %i increments counter with value %i" %(thread_ID, shared_counter_without_lock))

def decrement_without_lock(thread_ID):
    global shared_counter_without_lock
    for i in range(count):
        local = shared_counter_without_lock
        local -= 1
        time.sleep(random.randint(0,2))
        shared_counter_without_lock = local
        print("Thread %i decrements counter with value %i" %(thread_ID, shared_counter_without_lock))

if __name__ == "__main__":
    t1 = threading.Thread(target=increment_without_lock, args=(1,))
    t2 = threading.Thread(target=decrement_without_lock, args=(2,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("The value of shared variable with race condition is %s" %(shared_counter_without_lock))
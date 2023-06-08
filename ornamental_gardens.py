
import random
import threading
import time

# creating an object
class turnstile(threading.Thread):
    def __init__(self, threadID, name, visitor):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = visitor
        self.total = 0
    
    def run(self):
        for i in range(self.counter):
            global total

            tlock.acquire() # acquiring the created lock/locking the lock

            # updating how many people went inside the garden through the respective turnstile
            self.total = total
            print("Garden current total ({}): {:d} \r \n".format(self.name, self.total))
            print("{} turnstile: visitor {:d} arrived \r \n".format(self.name, i+1))

            # start of critical section
            self.total = self.total+1
            time.sleep(random.uniform(0,1))
            total = self.total
            # end of critical section

            tlock.release() # releasing the lock

            print("Garden new total count ({}): {:d} \r \n".format(self.name, total))
            time.sleep(random.uniform(0,1))


if __name__ == "__main__":
    total = 0
    tlock = threading.Lock() # created some form of lock

    east_turnstile = turnstile(1, "East", 3)
    west_turnstile = turnstile(2, "West", 3)

    east_turnstile.start()
    west_turnstile.start()

    east_turnstile.join()
    west_turnstile.join()
# 设计循环队列
class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.k = k
        # 初始为[0,0,..]
        self.l = [0] * k
        self.size = 0
        # self.h => head; self.t => tail
        self.h = self.t = 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.l[self.t] = value
        self.t = (self.t + 1) % self.k
        self.size += 1
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.l[self.h] = 0
        self.h = (self.h + 1) % self.k
        self.size -= 1
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        return self.l[self.h] if self.size else -1

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        return self.l[self.t - 1] if self.size else -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        if not self.size:
            return True
        return False

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        if self.size == self.k:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(10)
obj.enQueue(4)
param_1 = obj.enQueue(5)
param_2 = obj.deQueue()
param_3 = obj.Front()
param_4 = obj.Rear()
param_5 = obj.isEmpty()
param_6 = obj.isFull()


# 多线程
import threading
import queue
import random


def producer():
    while True:
        gcondition.acquire()
        n = random.randint(1, 100)
        if q.full():
            gcondition.wait()
        q.put(n)
        print(threading.current_thread().getName() + ':%s %s' % (n, q.queue))
        gcondition.notify_all()
        gcondition.release()


def consumer():
    while True:
        gcondition.acquire()
        if q.empty():
            gcondition.wait()
        n = q.get()
        print(threading.current_thread().getName() + ':%s %s' % (n, q.queue))
        gcondition.notify_all()
        gcondition.release()


q = queue.Queue()
q.maxsize = 10
gcondition = threading.Condition()

t1 = threading.Thread(name='producer1', target=producer).start()
# t2 = threading.Thread(name='producer2', target=producer).start()
t3 = threading.Thread(name='consumer', target=consumer).start()

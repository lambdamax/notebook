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
        # self.l的第一个位置
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
        return self.l[self.t-1] if self.size else -1

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

print(param_1)
print(obj.l)
print(param_2)
print(obj.l)
print(param_3)
print(obj.l)
print(param_4)
print(obj.l)
print(param_5)
print(obj.l)
print(param_6)
print(obj.l)

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class MyCircularQueue:
    def __init__(self, k: int):
        self.k = k
        self.length = 0
        self.head = ListNode(-1)
        self.tail = self.head

    def enQueue(self, value: int) -> bool:
        if self.length == self.k:
            return False
        node = ListNode(value)
        self.length += 1
        self.tail.next = node
        self.tail = self.tail.next

        if self.length == 1:
            self.head.next = node

        print("enq")

        return True

    def deQueue(self) -> bool:
        if self.length == 0:
            return False

        self.head.next = self.head.next.next
        self.length -= 1

        if self.length == 0:
            self.tail = self.head

        print("deq")
        return True
        
    def Front(self) -> int:
        if self.length > 0:
            return self.head.next.val
        
        return -1

    def Rear(self) -> int:
        if self.length > 0:
            return self.tail.val

        return -1

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
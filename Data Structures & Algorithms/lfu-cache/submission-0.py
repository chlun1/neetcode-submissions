from collections import defaultdict


class ListNode:
    def __init__(self, key=-1, val=-1):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.left = ListNode()
        self.right = ListNode()
        self.length = 0
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

        node.prev = None
        node.next = None

        self.length -= 1

    def insert(self, node):
        prev = self.right.prev
        nxt = self.right
        node.prev = prev
        prev.next = node
        node.next = nxt
        nxt.prev = node
        self.length += 1


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.counts = {}
        self.count2list = defaultdict(LinkedList)
        self.lfu_count = 0

    def increment(self, count, node):
        self.count2list[count].remove(node)
        self.count2list[count + 1].insert(node)
        self.counts[node.key] += 1

        if count == self.lfu_count and self.count2list[count].length == 0:
            self.lfu_count += 1

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            count = self.counts[key]
            self.increment(count, node)

            return node.val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            count = self.counts[key]
            self.increment(count, node)
            return
            
        if len(self.cache) == self.capacity:
            to_delete = self.count2list[self.lfu_count].left.next
            self.count2list[self.lfu_count].remove(to_delete)
            del self.cache[to_delete.key]
            del self.counts[to_delete.key]

        node = ListNode(key, value)
        self.cache[key] = node
        self.counts[key] = 1
        self.count2list[1].insert(node)
        self.lfu_count = 1




# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
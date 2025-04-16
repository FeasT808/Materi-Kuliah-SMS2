class MyQueue: 
    def __init__(self):
        self.items = []
    def show(self):
        print(self.items)
    def enQueue(self, item):
        self.items.append(item)
    def deQueue(self):
        return self.items.pop(0)   
    def isEmpty(self):
        return self.items == []    
    def front(self):
        return self.items[0]
queue = MyQueue()   
print(queue.isEmpty()) # True
queue.enQueue(1)
queue.enQueue(2)
queue.enQueue(3)           
queue.show() # [1, 2, 3]
print(f"antrian terdepan adalah: {queue.front()}")
queue.deQueue() # 1 
print(f"antrian terdepan adalah: {queue.front()}")


















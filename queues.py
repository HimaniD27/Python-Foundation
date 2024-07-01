from collections import queue
# queues in python are double ended queues by default
queue.append(2)
queue.append(4)
queue.popleft() #this operation done in constant time
queue.appendleft(6)
queue.pop()
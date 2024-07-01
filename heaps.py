#a data structure to find min and max of a set of values frequently
#under the hood they are arrays
import heapq

minHeap=[]
heapq.heappush(minHeap,3)  #by default - minHeap
heapq.heappush(minHeap,2)
heapq.heappush(minHeap,8)

print(minHeap[0])  #min is always at index O


#looping through heaps:   #smallest to greatest
while len(minHeap):
    print(heapq.heappop(minHeap))
    



#no max heaps by deafult, workaround is to use minheap and multiply by -1 when push and pop.
maxHeap=[]
heapq.heappush(maxHeap,-3)
heapq.heappush(maxHeap,-2)
heapq.heappush(maxHeap,-8)
print(-1*maxHeap[0])  #max is also always at index O




#looping through heaps:  # greatest to smallest
while len(maxHeap):
    print(-1*heapq.heappop(maxHeap))
    
    


#buliding a heap from some initial values you have
arr=[8,2,6,7,5]   #do it in linear time
heapq.heapify(arr)
while arr:
    print(heapq.heappop(arr))
    


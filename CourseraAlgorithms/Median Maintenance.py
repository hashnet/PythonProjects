import math
from enum import Enum

class HType(Enum):
    minHeap = 0
    maxHeap = 1


def insert(heap, num, type):
    heap.append(num)
    i = len(heap)-1
    while i != 0:
        p = (i-1)//2

        if type == HType.minHeap:
            if heap[p] > heap[i]:
                heap[p], heap[i] = heap[i], heap[p]
            else:
                break
        elif type == HType.maxHeap:
            if heap[p] < heap[i]:
                heap[p], heap[i] = heap[i], heap[p]
            else:
                break

        i = p


def extract(heap, type):
    if len(heap) == 0:
        return None

    num = heap[0]
    heap[0], heap[len(heap)-1] = heap[len(heap)-1], heap[0]
    del heap[len(heap)-1]
    i = 0;

    while i < len(heap):
        c1 = (i * 2) + 1
        c2 = c1 + 1

        if c1 < len(heap):
            if c2 < len(heap):
                if type == HType.minHeap:
                    if heap[c1] <= heap[c2]:
                        c = c1
                    else:
                        c = c2
                elif type == HType.maxHeap:
                    if heap[c1] >= heap[c2]:
                        c = c1
                    else:
                        c = c2
            else:
                c = c1
        else:
            break

        if type == HType.minHeap:
            if heap[i] > heap[c]:
                heap[i], heap[c] = heap[c], heap[i]
            else:
                break
        elif type == HType.maxHeap:
            if heap[i] < heap[c]:
                heap[i], heap[c] = heap[c], heap[i]
            else:
                break

        i = c

    return num


def view(heap):
    if len(heap) == 0:
        return None

    return heap[0]


f = open("files/median.txt", "r")
# f = open("files/sample.txt", "r")
count = int(f.readline())

heapLow = []
heapHigh = []
median = 0
for i in range(count):
    a = int(f.readline())

    if len(heapLow) == len(heapHigh):
        if len(heapHigh) == 0:
            insert(heapLow, a, HType.maxHeap)
        else:
            num = extract(heapHigh, HType.minHeap)

            minim = min(a, num)
            maxim = max(a, num)

            insert(heapLow, minim, HType.maxHeap)
            insert(heapHigh, maxim, HType.minHeap)

    elif len(heapLow) > len(heapHigh):
        num = extract(heapLow, HType.maxHeap)

        minim = min(a, num)
        maxim = max(a, num)

        insert(heapLow, minim, HType.maxHeap)
        insert(heapHigh, maxim, HType.minHeap)

    m = view(heapLow)
    median = (median + view(heapLow)) % 10000
    print("median = ", m, "sum % mod = ", median)


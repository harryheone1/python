from typing import List


class Heap:
    # construct array
    def __init__(self, nums: List[int]):
        self.arr = nums

    # heapify the array
    def build_heap(self, nums: List[int]):
        self.arr = nums
        start = int((len(nums) - 2) / 2)
        for i in range(start, -1, -1):
            self.heapify_top(i)
        return self.arr

    # add a element
    def push(self, num: int):
        self.arr.append(num)
        self.heapify()
        return self.arr

    # remove first element
    def pop(self):
        if not self.arr:
            raise Exception()
        res = self.arr[0]
        self.arr[0] = self.arr[len(self.arr) - 1]
        self.arr.pop()
        self.heapify_top(0)
        return res

    # get first
    def first(self):
        return self.arr[0] if self.arr else None

    # heapify normal
    def heapify(self):
        def get_prev(idx: int):
            if idx % 2 == 0:
                res = int((idx + 1) / 2) - 1
            else:
                res = int((idx + 1) / 2 - 1)

            return res

        cur = len(self.arr) - 1
        prev = get_prev(cur)

        while cur > 0 and self.arr[cur] < self.arr[prev]:
            self.arr[cur], self.arr[prev] = self.arr[prev], self.arr[cur]
            cur = prev
            prev = get_prev(cur)

        return self.arr

    # heapify from top
    def heapify_top(self, start):
        cur = start
        while (2 * cur + 1) < len(self.arr) and self.arr[cur] > min(self.arr[2 * cur + 1], self.arr[2 * cur + 2]):
            nxt = 2 * cur + 1
            if self.arr[2 * cur + 1] > self.arr[2 * cur + 2]:
                nxt = 2 * cur + 2
            self.arr[cur], self.arr[nxt] = self.arr[nxt], self.arr[cur]
            cur = nxt
        return self.arr

# input = [1, 4, 5]
# heap = Heap(input)
# print(heap.arr)
# print(heap.first())
# print(heap.push(3))
# print(heap.pop())
# print(heap.arr)

input = [5, 4, 1]
heap = Heap(list())
print(heap.build_heap(input))

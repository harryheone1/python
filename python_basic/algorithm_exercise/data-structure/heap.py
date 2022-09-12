from typing import List


class Heap:

    def __init__(self, arr: List[int]):
        self.arr = arr
        self.build_heap()

    def heapify_top(self, index):
        arr = self.arr

        while True:
            left_swap = 2 * index + 1 < len(arr) and arr[2 * index + 1] < arr[index]
            right_swap = 2 * index + 2 < len(arr) and arr[2 * index + 2] < arr[index]
            if left_swap and right_swap:
                left_swap = arr[2 * index + 1] < arr[2 * index + 2]

            if left_swap:
                arr[index], arr[2 * index + 1] = arr[2 * index + 1], arr[index]
                index = 2 * index + 1
            elif right_swap:
                arr[index], arr[2 * index + 2] = arr[2 * index + 2], arr[index]
                index = 2 * index + 2
            else:
                break

    def heapify_bottom(self, index):
        arr = self.arr
        while index >= 0:
            p_idx = int((index - 1) / 2)
            if arr[p_idx] > arr[index]:
                arr[p_idx], arr[index] = arr[index], arr[p_idx]
                index = p_idx
            else:
                break

    def get_min(self):
        if self.arr:
            return self.arr[0]

    def delete_root(self):
        if self.arr:
            arr = self.arr
            res = arr[0]
            val = arr.pop()
            if arr:
                arr[0] = val
                self.heapify_top(0)
            return res

    def insert_node(self, val: int):
        arr = self.arr
        arr.append(val)
        self.heapify_bottom(len(arr) - 1)

    def build_heap(self):
        arr = self.arr
        start = int((len(arr) - 2) / 2)
        for i in range(start, -1, -1):
            # add while loop later
            # ci =
            self.heapify_top(i)


count = 10
input_ = [i for i in range(count) if i % 2 == 0]
test = Heap(input_[::-1])
test.insert_node(5)
test.insert_node(3)

for i in range(10):
    print(i, test.get_min())
    test.delete_root()

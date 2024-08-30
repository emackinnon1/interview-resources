class MedianFinder:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num):
        print("incoming", num)
        self.max_heap.append(num)
        self.max_heap.sort()
        self.min_heap.append(self.max_heap[0])
        self.max_heap.pop(0)
        self.min_heap.sort(reverse=True)
        # if not len(self.max_heap) or (self.max_heap[0] >= num):
        #     self.max_heap.append(num)
        #     self.max_heap.sort(reverse=True)
        # else:
        #     self.min_heap.append(num)
        #     self.min_heap.sort(reverse=True)
        print(
            "before rebalance: ",
            self.max_heap,
            self.min_heap,
        )

        if len(self.max_heap) - len(self.min_heap) >= 1:
            self.min_heap.append(self.max_heap.pop(len(self.max_heap) - 1))
            self.min_heap.sort(reverse=True)
        elif len(self.max_heap) - len(self.min_heap) <= 0:
            self.max_heap.append(self.min_heap.pop(0))
            self.max_heap.sort(reverse=True)
        print(
            "after rebalance: ",
            self.max_heap,
            self.min_heap,
        )

    def findMedian(self):
        if len(self.min_heap) < len(self.max_heap):
            print(
                "max heap head and len",
                float(self.max_heap[len(self.max_heap) - 1]), len(self.max_heap),
                "min heap head and len",
                float(self.min_heap[0]) if self.min_heap else self.min_heap, len(self.min_heap)
            )
            return self.max_heap[len(self.max_heap) - 1]
        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        else:
            print(
                "max heap head and len",
                float(self.max_heap[len(self.max_heap) - 1]), len(self.max_heap),
                "min heap head and len",
                float(self.min_heap[0]), len(self.min_heap)
            )
            return (
                (float(self.max_heap[len(self.max_heap)-1]) + float(self.min_heap[0])) / 2
            )


def test_func(test_actions):
    res = []
    for i, t in enumerate(test_actions):
        # print("index", i)
        if i == 0:
            finder = MedianFinder()
            res.append("null")
            continue
        if len(t):
            finder.addNum(t[0])
            res.append("null")
        else:
            res.append(finder.findMedian())
    return res



# print("TEST 1 =======================")
cases = [[], [1], [2], [], [3], []]
print(test_func(cases))
# print("TEST 2 =======================")
# cases = [[], [1], []]
# print(test_func(cases))
# print("TEST 3 =======================")
# cases = [[], [-1], [], [-2], [], [-3], [], [-4], [], [-5], []] 
# expected = [null,null,-1.00000,null,-1.50000,null,-2.00000,null,-2.50000,null,-3.00000]
# print(test_func(cases))

# print("TEST 4 =======================")

# tests = [
#     [],
#     [12],
#     [],
#     [10],
#     [],
#     [13],
#     [],
#     [11],
#     [],
#     [5],
#     [],
#     [15],
#     [],
#     [1],
#     [],
#     [11],
#     [],
#     [6],
#     [],
#     [17],
#     [],
#     [14],
#     [],
#     [8],
#     [],
#     [17],
#     [],
#     [6],
#     [],
#     [4],
#     [],
#     [16],
#     [],
#     [8],
#     [],
#     [10],
#     [],
#     [2],
#     [],
#     [12],
#     [],
#     [0],
#     [],
# ]
# res = []
# finder3 = None

# for i, t in enumerate(tests):
#     print("index", i)
#     if i == 0:
#         finder3 = MedianFinder()
#         res.append("null")
#         continue
#     if len(t):
#         finder3.addNum(t[0])
#         res.append("null")
#     else:
#         res.append(finder3.findMedian())
# print(res)
# exp = [
#     "null",
#     "null",
#     12,
#     "null",
#     11.0,
#     "null",
#     12,
#     "null",
#     11.5,
#     "null",
#     11,
#     "null",
#     11.5,
#     "null",
#     11,
#     "null",
#     11.0,
#     "null",
#     11,
#     "null",
#     11.0,
#     "null",
#     11,
#     "null",
#     11.0,
#     "null",
#     11,
#     "null",
#     11.0,
#     "null",
#     11,
#     "null",
#     11.0, # diff: 13.5
#     "null",
#     11,
#     "null",
#     10.5,
#     "null",
#     10,
#     "null",
#     10.5, # diff: 11.0
#     "null",
#     10,
# ]
# print(res == exp)

import unittest
from heap import *

# add more classes and tests

class HeapTestCase(unittest.TestCase):
    
    def setUp(self):
        self.heap = MinHeap()
    
    def is_min_heap(self, L, rooti=0):
        # no kids
        if rooti > len(L) // 2 + 1:
            return True
        l = left(rooti)
        r = right(rooti)
        if l < len(L) and L[rooti] > L[l]:
            return False
        if r < len(L) and L[rooti] > L[r]:
            return False
        return self.is_min_heap(L, l) and self.is_min_heap(L, r)
        
    def test_empty(self):
        with self.assertRaises(EmptyHeapException):
            self.heap.extract_min()
    
    def test_insert_solo(self):
        self.heap.insert(5)
        self.assertEqual(self.heap._data[0], 5)
        self.assertTrue(self.is_min_heap(self.heap._data))

    def test_insert_multi(self):
        for i in (6, 8, 4, 3, 6, 1, 7):
            self.heap.insert(i)
        self.assertTrue(self.is_min_heap(self.heap._data))


    def test_extract_solo(self):
        self.heap._data = [3]
        self.assertEqual(self.heap.extract_min(), 3)


    def test_extract_multi(self):
        self.heap._data = [2, 3, 5, 4]
        out = []
        for i in range(4):
            out.append(self.heap.extract_min())
        self.assertEqual(len(out), 4)
        #print(out)
        for i in (5, 3, 2, 4):        
            self.assertTrue(i in out)
        self.assertEqual(out, sorted(out))
        
    def test_extract_multi2(self):
        self.heap._data = [1, 3, 2, 4]
        out = []
        for i in range(4):
            out.append(self.heap.extract_min())
        self.assertEqual(len(out), 4)
        #print(out)
        for i in (1, 3, 2, 4):        
            self.assertTrue(i in out)
        self.assertEqual(out, sorted(out))



    def test_min_heapify_lil(self):
        self.heap = MinHeap([7, 99, 2])
        self.assertTrue(self.is_min_heap(self.heap._data))
        self.assertEqual(self.heap._data, [2, 99, 7])


    def test_min_heapify_big(self):
        self.heap = MinHeap([7, 99, 2, 17, 19, 25, 3, 1, 36])
        self.assertTrue(self.is_min_heap(self.heap._data))
        self.assertEqual(self.heap._data, [1, 7, 2, 17, 19, 25, 3, 99, 36])


if __name__ == "__main__":
    unittest.main()

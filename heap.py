# helper functions

def left(index):
    '''Return index's left child index.
    '''
    return index * 2 + 1


def right(index):
    '''Return index's right child index.
    '''
    return index * 2 + 2


def parent(index):
    '''Return index's parent index.'''
    return (index - 1) // 2


class EmptyHeapException(Exception):
    '''Custom exception for empty heap
    '''
    pass


class MinHeap:

    def __init__(self, L=None):
        '''Create a new MinHeap.
        This method is complete.'''

        if not L:
            self._data = []
        else:
            self._data = L
            self._min_heapify()


    def __len__(self):
        '''Return the length of the MinHeap.
        This method is complete.'''

        return len(self._data)


    def __str__(self):
        '''Return a string representation of the heap.
        This method is complete.'''

        return str(self._data)


    def insert(self, v):
        '''Insert v in self. Maintain heap property.'''

        self._data.append(v)

        # precolate up only if the heap list has more than one elements
        if len(self._data) != 1:
            self._percolate_up()


    def extract_min(self):
        '''Remove minimal value in self. Restore heap property.
        Raise EmptyHeapException if heap is empty.'''

        if len(self._data) == 0:
            raise EmptyHeapException()

        if len(self._data) == 0:
            return self._data.pop(0)

        # pop out the root element
        smallest = self._data.pop(0)

        # perform heapfiy on the whole heap list
        self._min_heapify()

        return smallest


    def _percolate_up(self):
        '''Restore heap property of self after
        adding new item'''

        i = len(self._data) - 1

        # iteratively find parents
        while i != 0:
            p = parent(i)
            # swap parent with the child if the parent is bigger 
            # and repeat the process on the upper level
            if self._data[p] > self._data[i]:
                self._data[p], self._data[i] = self._data[i], self._data[p]
                i = p
            else:
                break


    def _percolate_down(self, i):
        ''' Restore heap property of subtree
        rooted at index i.
        '''

        # while larger than at least one child
        # swap with smaller child and repeat

        smallest = i

        l = left(i)
        r = right(i)

        # check if the left child exists and is the smaller one
        if l < len(self._data) and self._data[smallest] > self._data[l]:
            smallest = l

        # check if the right child exists and is the smaller one
        if r < len(self._data) and self._data[smallest] > self._data[r]:
            smallest = r

        # swap the parent with the smallest child
        # and repeat the process on the lower level
        if smallest != i:
            self._data[i], self._data[smallest] = self._data[smallest], self._data[i]
            self._percolate_down(smallest)


    def _min_heapify(self):
        '''Turn unordered list into min-heap.'''

        # for each node in the first half of the list
        # percolate down

        for i in range(len(self._data) // 2, -1, -1):
            self._percolate_down(i)

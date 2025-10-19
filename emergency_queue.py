class Patient:
    def __init__(self,name,severity):
        self.name=name
        self.severity=severity

    def __lt__(self,other):
        return self.severity<other.severity
    
    def __repr__(self):
        return (f"{self.name}, Severity {self.severity}")  



class MinHeap:
    def __init__(self):
        self.heap=[]

    def insert(self,patient):
        self.heap.append(patient)
        self._heapify_up(len(self.heap)-1)

    def _heapify_up(self,index):
        parent=(index-1)//2
        if index>0 and self.heap[index]<self.heap[parent]:
            self.heap[index],self.heap[parent]<self.heap[parent],self.heap[index]
            self._heapify_up(parent)

    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap)==1:
            return self.heap.pop()
        root=self.heap[0]
        self.heap[0]=self.heap.pop()
        self._heapify_down(0)
        return root
    

    def _heapify_down(self,index):
        smallest=index
        left=2*index+1
        right=2*index+2
        if left<len(self.heap) and self.heap[left]< self.heap[smallest]:
            smallest=left
        if right<len(self.heap) and self.heap[right]< self.heap[smallest]:
            smallest=right
        if smallest!=index:
            self.heap, self.heap[smallest]< self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)



    def peek(self):
        return self.heap[0] if self.heap else None
    
    def is_empty(self):
        return len(self.heap)==0




# Test your MinHeap class here including edge cases
if __name__ == "__main__":
    pq = MinHeap()
    pq.insert(Patient("Alice", 5))
    pq.insert(Patient("Bob", 2))
    pq.insert(Patient("Charlie", 8))
    pq.insert(Patient("Diana", 1))

    print("Initial Queue:", pq.heap)
    while not pq.is_empty():
        print("Next patient:", pq.extract_min())


from copy import deepcopy


class Heap:
    def __init__(self):
        self.heap = [0]
        self.size = 0
        
    #/////----- INSERT OPERATION -----/////
    def arrange(self, k):
        while k // 2 > 0:
            if self.heap[k] < self.heap[k//2]:
                self.heap[k], self.heap[k//2] = self.heap[k//2], self.heap[k]
            k //= 2
    
    def insert(self, item):
        self.heap.append(item)
        self.size += 1
        self.arrange(self.size)
    
    #/////----- POP OPERATION -----/////
    def minindex(self, k):
        if k * 2 + 1 > self.size:
            return k * 2
        elif self.heap[k*2] < self.heap[k*2+1]:
            return k * 2
        else:
            return k * 2 + 1
    
    def sink(self, k):
        while k*2 <= self.size:
            mi = self.minindex(k)
            if self.heap[k] > self.heap[mi]:
                self.heap[k], self.heap[mi] = self.heap[mi], self.heap[k]
            k = mi
    def pop(self):
        item = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.sink(1)
        return item
    
    def heap_sort(self):
        sorted_list = []
        for node in range(self.size):
            n = self.pop()
            sorted_list.append(n)
        return sorted_list



h = Heap()
for i in (4, 8, 7, 2, 9, 10, 5, 1, 3, 6):
    h.insert(i)
  
print('fila actual',  h.heap)


while True: 
    
    print('=====================/////// IMSS ///////=====================')
    usuario = input("\ningresa tu nombre: \n" )

    prioridad = int(input("hola max, que tan mal te sientes del 1 al 10?: "))
    
    h.insert(prioridad)
    
    print('\nhola', usuario, ', hay en espera', h.size, 'usuarios\n')
    #print(h.heap)

    dup_h = deepcopy(h)
                
    n = 1000
    
    lugar = 0 

    while n != prioridad: 
        n = dup_h.pop()
        lugar += 1
        
    while n == prioridad: 
        n = dup_h.pop()
        lugar += 1
    
    print("======= TU NUMERO ES:", lugar-1, '=======', '\n')




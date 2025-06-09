class BubbleSort:
    def __init__(self, data):
        self.data = data

    def sort(self):
        n = len(self.data)
        for i in range(n):
            for j in range(0,n-i-1):
                if self.data[j] > self.data[j+1]:
                    self.data[j], self.data[j+1] = self.data[j+1], self.data[j]
        return self.data
    

    def sortDescending(self):
        n = len(self.data)
        for i in range(n):
            for j in range(0,n-i-1):
                if self.data[j] < self.data[j+1]:
                    self.data[j], self.data[j+1] = self.data[j+1], self.data[j]
        return self.data
    
    
#example usage
data_array = [63,23, 42, 11 , 31, 29, 90]
sorted_array = BubbleSort(data_array).sort()
print("Sorted data terkecil:", sorted_array)
sorted_array_Descending = BubbleSort(data_array).sortDescending()
print("sorted data Terbesar :",sorted_array_Descending )












































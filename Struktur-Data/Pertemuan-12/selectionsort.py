class SelectionSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        n = len(self.arr)
        for i in range(n):
            min_index = i 
            for j in range(i+1, n):
                if self.arr[j] < self.arr[min_index]:
                    min_index = j
            self.arr[i], self.arr[min_index] = self.arr[min_index], self.arr[i]
        return self.arr
    
    def sortDescending(self):
        n = len(self.arr)
        for i in range(n):
            min_index = i 
            for j in range(i+1, n):
                if self.arr[j] > self.arr[min_index]:
                    min_index = j
            self.arr[i], self.arr[min_index] = self.arr[min_index], self.arr[i]
        return self.arr
#Example usage

data_array = [63, 23, 42, 11, 31, 29, 90]
sorted_array = SelectionSort(data_array).sort()
print("Sorted data terkecil:", sorted_array)    
sorted_array_descending = SelectionSort(data_array).sortDescending()
print("Sorted data terbesar:", sorted_array_descending)










































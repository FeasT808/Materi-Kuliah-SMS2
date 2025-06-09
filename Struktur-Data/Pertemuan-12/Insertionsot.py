class Insertionsot:
    def __init__(self, data):
        self.data = data

    def sort(self):
        for i in range(1, len(self.data)):
            key = self.data[i]
            j = i - 1
            while j >= 0 and key < self.data[j]:
                self.data[j + 1] = self.data[j]
                j -= 1
            self.data[j + 1] = key
        return self.data
    
    def Descendingsort(self):
        for i in range(1, len(self.data)):
            key = self.data[i]
            j = i - 1
            while j >= 0 and key > self.data[j]:
                self.data[j + 1] = self.data[j]
                j -= 1
            self.data[j + 1] = key
        return self.data
    
#Example usage

data_array = [63, 23, 42, 11, 31, 29, 90]
sorted_array = Insertionsot(data_array).sort()
print("Sorted data terkecil:", sorted_array)
sorted_array_Descending = Insertionsot(data_array).Descendingsort()
print("Sorted data terbesar:", sorted_array_Descending)









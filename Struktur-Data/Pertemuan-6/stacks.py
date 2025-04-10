
class Stacks:
    def  __init__(self):
     # inisiasi variabel menjadi Stacks
        self.items = []
    def push(self, item):
        # 1.Implementasi Push (Menambahkan data ke dalam Stacks)
        self.items.append(item)
    def isEmpty(self):
    # 4. Impementasi isEmpty(cek stack kosong atau tidak)
        if (len(self.items)==0):
            print("Stack Kosong")
        print (f"isi Stacks: {self.items}")
    def pop(self):
    # 2.Implementasi konsep Pop (Mengambil / Menghapus elemen)
        if not len(self.items)==0:
            return self.items.pop()
        return "Staks Kosong"
    def top(self):
        #3. Implementasi Top (untuk Melihat tumpukan teratas)
        print (self.items[-1])
        
# Penggunaan Class dan Function
myTumpuk = Stacks()
myTumpuk.push("Page 1")
myTumpuk.push("Page 2")
myTumpuk.push("page 3")
myTumpuk.isEmpty()
myTumpuk.pop()
myTumpuk.isEmpty()
myTumpuk.top()








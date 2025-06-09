class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        idx = self._hash(key)
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                self.table[idx][i] = (key, value)
                print("Kontak diperbarui.")
                return
        self.table[idx].append((key, value))
        print("Kontak berhasil ditambahkan.")

    def delete(self, key):
        idx = self._hash(key)
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                del self.table[idx][i]
                print("Kontak berhasil dihapus.")
                return
        print("Kontak tidak ditemukan.")

    def search(self, key):
        idx = self._hash(key)
        for k, v in self.table[idx]:
            if k == key:
                return v
        return None

    def display_by_key(self, key):
        value = self.search(key)
        if value:
            print(f"Kontak: {key} -> {value}")
        else:
            print("Kontak tidak ditemukan.")

    def display_all(self):
        found = False
        for bucket in self.table:
            for k, v in bucket:
                print(f"{k} -> {v}")
                found = True
        if not found:
            print("Tidak ada kontak yang tersimpan.")

def main():
    ht = HashTable()
    while True:
        print("\nMenu Simpan Kontak:")
        print("1. Insert Contact")
        print("2. Hapus Contact")
        print("3. Tampil Kontak Berdasar Keys")
        print("4. Tampil semua kontak")
        print("5. Exit")
        choice = input("Pilih menu (1-5): ")
        if choice == '1':
            key = input("Masukkan nama kontak: ")
            value = input("Masukkan nomor telepon: ")
            ht.insert(key, value)
        elif choice == '2':
            key = input("Masukkan nama kontak yang akan dihapus: ")
            ht.delete(key)
        elif choice == '3':
            key = input("Masukkan nama kontak yang dicari: ")
            ht.display_by_key(key)
        elif choice == '4':
            ht.display_all()
        elif choice == '5':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
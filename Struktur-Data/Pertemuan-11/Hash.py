import streamlit as st
class HashTable:
    def __init__(self, size):
        self.size  = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size
    
    def insert(self, key, value):
        idx = self.hash_function(key)
        if self.table[idx] is None:
            self.table[idx] = []
        self.table[idx].append((key, value))

    def search(self, key):
        idx = self.hash_function(key)
        if self.table[idx] is not None:
            for k, v in self.table[idx]:
                if k == key:
                    return v
        return None
                     
    def delete(self, key):
        idx = self.hash_function(key)
        if self.table[idx] is not None:
            for i, (k, v) in enumerate(self.table[idx]):
                if k == key:
                    del self.table[idx][i]
                    return True
        return None
    
if 'hash_table' not in st.session_state:
    st.session_state.hash_table = HashTable(20)

st.title("Hash Table")
menu = st.sidebar.selectbox("Menu", ["Insert", "Search", "Delete", "Display"])

if menu == "Insert":
    st.subheader("Insert Data")
    kode_produk = st.number_input("Kode Produk", min_value=0, step=1)
    nama_produk = st.text_input("Nama Produk") 
    if st.button("Insert"):
        st.session_state.hash_table.insert(kode_produk, nama_produk)
        st.success(f"Data {nama_produk} dengan kode {kode_produk} berhasil dimasukkan.")

if menu == "Search":
    st.subheader("Search Data")
    kode_produk = st.number_input("Kode Produk", min_value=0, step=1)
    if st.button("Search"):
        result = st.session_state.hash_table.search(kode_produk)
        if result:
            st.success(f"Data ditemukan: {result}")
        else:
            st.error("Data tidak ditemukan.")

if menu == "Delete":
    st.subheader("Delete Data")
    kode_produk = st.number_input("Kode Produk", min_value=0, step=1)
    if st.button("Delete"):
        result = st.session_state.hash_table.delete(kode_produk)
        if result:
            st.success(f"Data dengan kode {kode_produk} berhasil dihapus.")
        else:
            st.error("Data tidak ditemukan.")

if menu == "Display":
    st.subheader("Display Hash Table")
    for k, v in enumerate(st.session_state.hash_table.table):
        st.write(f"Index {k}: {v}")
       
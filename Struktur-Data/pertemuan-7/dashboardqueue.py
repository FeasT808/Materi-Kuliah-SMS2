from gtts import gTTS
import streamlit as st
st.title("Sistem Antrian Pasien di RSUD Surabaya")
def genertate_tts(text,filename="antrian.mp3"):
    tts = gTTS(text=text, lang='id', slow=True)
    tts.save(filename)
    return filename
#membuat sebuah session unutk antrian 
if "queue" not in st.session_state :
    st.session_state.queue = []
if "current" not in st.session_state:
    st.session_state.current = 0    
with st.form("form"):
    nomor = st.text_input("Masukan Nomor Antrian")
    submit = st.form_submit_button("Tambah")
    if submit and nomor:
        st.session_state.queue.append(nomor)
        st.success(f"Nomor antrian {nomor} berhasil ditambahkan")
st.subheader("Daftar Antrian")
for i, nomor in enumerate(st.session_state.queue):
    st.write(f"{i+1}. {nomor}")
if st.button("Panggil Daftar Antrian"):
    if st.session_state.queue:
        panggil = st.session_state.queue.pop(0)
        st.session_state.current += 1
        teks = f" Atas Nama {panggil} silahkan menuju loket"
        st.success(teks)
        filename = genertate_tts(teks)
        audio_file = open(filename, "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3", autoplay=True)
    else:
        st.warning("tidak ada antrian")

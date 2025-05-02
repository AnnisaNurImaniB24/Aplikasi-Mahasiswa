import streamlit as st
import pandas as pd
import matplotlib.pyplotpip as plt

# =========================
# Form Biodata & Pengalaman
# =========================
st.title('Keluh Kesah Mahasiswa Gen Z')

with st.form(key='keluh_kesah_form'):
    nama = st.text_input('Nama')
    nim = st.text_input('NIM')
    program_studi = st.text_input('Program Studi')
    angkatan = st.number_input('Angkatan', min_value=2000, max_value=2100, step=1)
    universitas = st.text_input('Universitas/Kampus')
    kartu_identitas = st.file_uploader('Upload Kartu Identitas Mahasiswa', type=['jpg', 'jpeg', 'png', 'pdf'])
    ipk = st.number_input('Indeks Prestasi Kumulatif (IPK)', min_value=0.0, max_value=4.0, step=0.01, format='%.2f')
    tanggal_lahir = st.date_input('Tanggal Lahir')
    agama = st.text_input('Agama')
    alamat = st.text_area('Alamat')
    riwayat_pendidikan = st.text_area('Riwayat Pendidikan')
    pengalaman_organisasi = st.text_area('Pengalaman Organisasi')
    kemampuan = st.text_area('Kemampuan')
    hobi = st.text_area('Hobi')
    kekurangan = st.text_area('Kekurangan')
    kelebihan = st.text_area('Kelebihan')
    warna_favorit = st.text_input('Warna Favorit')
    makanan_favorit = st.text_input('Makanan Favorit')

    submit_button = st.form_submit_button(label='Submit Biodata')

if submit_button:
    if kartu_identitas is not None:
        st.success('Data biodata berhasil disubmit!')
        st.markdown("**Preview Kartu Identitas:**")
        if kartu_identitas.type.startswith('image/'):
            st.image(kartu_identitas, use_column_width=True)
        else:
            st.write(f"File '{kartu_identitas.name}' berhasil diupload.")
    else:
        st.warning('Mohon upload Kartu Identitas Mahasiswa.')

# =========================
# Form Rating dan Kesan
# =========================
st.title('Rating dan Kesan Mahasiswa')

with st.form(key='rating_form'):
    rating_jurusan = st.slider('Rating Jurusan/Prodi (1-10)', 1, 10, 5)
    kesan_mahasiswa = st.text_area('Kesan Selama Menjadi Mahasiswa')
    satu_kata_mata_kuliah = st.text_input('Satu Kata untuk Mata Kuliah')
    pesan_dosen = st.text_area('Pesan untuk Dosen Tercinta')

    submit_button_rating = st.form_submit_button(label='Submit Rating dan Kesan')

if submit_button_rating:
    st.success('Data rating dan kesan berhasil disubmit!')

# =========================
# Form Kisah Cinta Mahasiswa
# =========================
st.title('Kisah Cinta Mahasiswa')

with st.form(key='kisah_cinta_form'):
    st.subheader('Status Kisah Cinta')
    cinta_ditolak = st.checkbox('Cinta/Sayang Ditolak')
    cinta_diterima = st.checkbox('Cinta/Sayang Diterima')

    st.subheader('Lokasi dan Status Hubungan')
    seprodi = st.checkbox('Seprodi/Sejurusan')
    beda_jurusan = st.checkbox('Beda Jurusan/Beda Prodi')
    sekampus = st.checkbox('Sekampus')
    beda_kampus = st.checkbox('Beda Kampus')

    cerita_kisah_cinta = st.text_area('Ceritakan Kisah Cinta Anda')

    submit_button_cinta = st.form_submit_button(label='Submit Kisah Cinta')

if submit_button_cinta:
    st.success('Kisah cinta berhasil disubmit!')

    st.markdown("**Ringkasan Kisah Cinta Anda:**")
    status_hubungan = []
    lokasi_hubungan = []

    if cinta_ditolak:
        status_hubungan.append("Cinta/Sayang Ditolak")
    if cinta_diterima:
        status_hubungan.append("Cinta/Sayang Diterima")

    if seprodi:
        lokasi_hubungan.append("Seprodi/Sejurusan")
    if beda_jurusan:
        lokasi_hubungan.append("Beda Jurusan/Beda Prodi")
    if sekampus:
        lokasi_hubungan.append("Sekampus")
    if beda_kampus:
        lokasi_hubungan.append("Beda Kampus")

    st.write("Status hubungan: ", ", ".join(status_hubungan) if status_hubungan else "Tidak dipilih")
    st.write("Lokasi hubungan: ", ", ".join(lokasi_hubungan) if lokasi_hubungan else "Tidak dipilih")
    st.write("Cerita Anda:")
    st.write(cerita_kisah_cinta if cerita_kisah_cinta.strip() else "Anda belum menuliskan cerita kisah cinta.")

# =========================
# Form Impian, Target, Planning, dan Cita-cita
# =========================
st.title('Impian, Target, Planning, dan Cita-cita')

with st.form(key='impian_form'):
    impian = st.text_area('Impian Anda')
    target = st.text_area('Target Anda')
    planning = st.text_area('Planning Anda')
    cita_cita = st.text_area('Cita-cita Anda')

    submit_button_impian = st.form_submit_button(label='Submit Impian dan Cita-cita')

if submit_button_impian:
    st.success('Impian, target, planning, dan cita-cita berhasil disubmit!')
    st.markdown("### Ringkasan Impian dan Cita-cita")
    st.write(f"**Impian:** {impian}" if impian.strip() else "Impian belum diisi.")
    st.write(f"**Target:** {target}" if target.strip() else "Target belum diisi.")
    st.write(f"**Planning:** {planning}" if planning.strip() else "Planning belum diisi.")
    st.write(f"**Cita-cita:** {cita_cita}" if cita_cita.strip() else "Cita-cita belum diisi.")

# =========================
# Statistik Mahasiswa & Pendidikan
# =========================
st.title('Statistik Mahasiswa dan Pendidikan')

# Data dummy total mahasiswa dari tahun 2020-2025
tahun = [2020, 2021, 2022, 2023, 2024, 2025]
total_mahasiswa = [150, 180, 210, 240, 270, 300]

# Membuat dataframe
data = {'Tahun': tahun, 'Total Mahasiswa': total_mahasiswa}
df = pd.DataFrame(data)

# Menampilkan tabel
st.subheader('Total Mahasiswa Tahun 2020-2025')
st.dataframe(df)

# Grafik Total Mahasiswa
fig, ax = plt.subplots(figsize=(6, 3))
ax.bar(df['Tahun'], df['Total Mahasiswa'], color='skyblue')
ax.set_xlabel('Tahun')
ax.set_ylabel('Total Mahasiswa')
ax.set_title('Grafik Total Mahasiswa Tahun 2020-2025')
ax.tick_params(axis='x', rotation=0)
st.pyplot(fig)

# Pie chart Pendidikan
kategori = ['Tidak Sekolah', 'SD', 'SMP', 'SMA', 'Perguruan Tinggi']
presentasi = [10, 20, 25, 30, 15]

fig2, ax2 = plt.subplots(figsize=(5, 3))
ax2.pie(presentasi, labels=kategori, autopct='%1.1f%%', startangle=90)
ax2.set_title('Persentase Masyarakat yang Mengenyam Pendidikan (dalam %)')
st.pyplot(fig2)

# Grafik Bar Mahasiswa dan Teknologi
st.subheader("Tingkat Penguasaan Teknologi oleh Mahasiswa")
kategori_teknologi = ['Tidak Paham Teknologi', 'Paham Teknologi', 'Menguasai Teknologi']
persen_teknologi = [25, 50, 25]

fig3, ax3 = plt.subplots(figsize=(6, 3))
ax3.bar(kategori_teknologi, persen_teknologi, color=['red', 'orange', 'green'])
ax3.set_ylabel('Persentase (%)')
ax3.set_title('Tingkat Pemahaman Teknologi Mahasiswa (dalam %)')
for i, v in enumerate(persen_teknologi):
    ax3.text(i, v + 1, str(v) + '%', ha='center')
st.pyplot(fig3)

# Tambahan Statistik Generasi Muda
st.title("Statistik Generasi Muda")
usialabel = ['<15', '15-24', '25-34', '35-44', '45+']
usiapersen = [10, 35, 25, 20, 10]

fig4, ax4 = plt.subplots(figsize=(6, 3))
ax4.bar(usialabel, usiapersen, color='purple')
ax4.set_ylabel('Persentase (%)')
ax4.set_title('Distribusi Usia Generasi Muda')
st.pyplot(fig4)

# =========================
# Pendapat tentang Pendidikan & Teknologi
# =========================
st.title('Pendidikan vs Melek Teknologi')

col1, col2 = st.columns(2)

with col1:
    st.subheader('Kenapa Mahasiswa Bisa Tidak Berpendidikan Tapi Harus Melek Teknologi?')
    alasan_melek_tek = st.text_area('Alasan Kenapa Harus Melek Teknologi')

with col2:
    st.subheader('Pro dan Kontra Tidak Mengenyam Pendidikan tapi Melek Teknologi')
    pro_kontra = st.text_area('Berikan Pendapat Pro dan Kontra')

submit_masukan = st.button('Submit Pendapat')

if submit_masukan:
    st.success('Terima kasih atas pendapat Anda!')
    st.write('**Alasan Kenapa Mahasiswa Harus Melek Teknologi:**')
    st.write(alasan_melek_tek if alasan_melek_tek.strip() else 'Belum diisi.')
    st.write('**Pro dan Kontra Tidak Mengenyam Pendidikan tapi Melek Teknologi:**')
    st.write(pro_kontra if pro_kontra.strip() else 'Belum diisi.')


st.caption("© 2025 Keluh Kesah Mahasiswa | Streamlit App")
st.caption("Dibuat dengan ❤️ oleh [Nurichxy]")
import streamlit as st

def luas_persegi(sisi):
    return sisi * sisi

def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

def luas_lingkaran(jari_jari):
    return 3.14 * jari_jari * jari_jari

def keliling_persegi(sisi):
    return 4 * sisi

def keliling_persegi_panjang(panjang, lebar):
    return 2 * (panjang + lebar)

def keliling_lingkaran(jari_jari):
    return 2 * 3.14 * jari_jari

rumus_luas = {
    "Persegi": luas_persegi,
    "Persegi Panjang": luas_persegi_panjang,
    "Lingkaran": luas_lingkaran
}

rumus_keliling = {
    "Persegi": keliling_persegi,
    "Persegi Panjang": keliling_persegi_panjang,
    "Lingkaran": keliling_lingkaran
}

st.title("Hitung Luas dan Keliling Bangun Datar")

pilihan = st.selectbox(
    "Pilih operasi perhitungan:",
    ["Luas", "Keliling"]
)

def pilih_rumus(pilihan):
    if pilihan == "Luas":
        return rumus_luas
    else:
        return rumus_keliling

rumus = pilih_rumus(pilihan)

bangun_datar = st.radio(
    "Pilih bangun datar:",
    list(rumus.keys())
)

if bangun_datar == "Persegi":
    sisi = st.number_input("Masukkan sisi")

elif bangun_datar == "Persegi Panjang":
    panjang = st.number_input("Masukkan panjang")
    lebar = st.number_input("Masukkan lebar")

elif bangun_datar == "Lingkaran":
    jari_jari = st.number_input("Masukkan jari-jari")

if st.button("Hitung"):
    if bangun_datar == "Persegi":
        hasil = rumus[bangun_datar](sisi)

    elif bangun_datar == "Persegi Panjang":
        hasil = rumus[bangun_datar](panjang, lebar)

    elif bangun_datar == "Lingkaran":
        hasil = rumus[bangun_datar](jari_jari)

    st.markdown(f"### Hasil Perhitungan: **{hasil}**")


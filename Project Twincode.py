import datetime, os, time, sys, random

# Warna ANSI
class Color:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    MAGENTA = '\033[95m'
    BOLD = '\033[1m'
    END = '\033[0m'

# DB Motivasi
MOTIVASI = [
    "Mimpi besar dimulai dari langkah kecil hari ini!",
    "Kampus impian menunggu versi terbaik dari dirimu!",
    "Jurusan yang tepat = kehidupan yang bahagia!",
    "Setiap usaha hari ini adalah tiket menuju masa depan cerah.",
    "Kamu unik, jurusanmu juga harus spesial!"
]

# (UNIV_TOP DIHAPUS SESUAI PERMINTAAN)

# Tips Belajar
TIPS_BELAJAR = {
    'Matematika': "Latihan soal HOTS 30 menit/hari + pahami konsep.",
    'IPA': "Buat mind map + kerjakan 10 soal prediksi UTBK setiap hari.",
    'IPS': "Baca koran + hubungkan materi dengan isu terkini.",
    'Bahasa Inggris': "Baca artikel BBC/CNN 15 menit + catat 10 kata baru.",
    'Bahasa Indonesia': "Latihan membaca teks 500 kata + jawab 5 pertanyaan HOTS.",
    'PPKN': "Hafal UUD 1945 & isu aktual + latihan soal etika negara."
}

# Simulasi UTBK
SOAL_UTBK = [
    ("Hasil dari 2^5 adalah...", ["16", "32", "64", "128"], "32"),
    ("Ibu kota Brasil adalah...", ["Rio", "Sao Paulo", "Brasilia", "Manaus"], "Brasilia"),
    ("Luas lingkaran jari-jari 7 cm (π=22/7)...", ["44", "154", "22", "49"], "154"),
    ("Sinonim dari 'abadi' adalah...", ["sementara", "kekal", "hilang", "baru"], "kekal"),
    ("Reaksi fotosintesis menghasilkan...", ["Oksigen", "Karbon dioksida", "Nitrogen", "Hidrogen"], "Oksigen"),
    ("pH air hujan normal adalah...", ["5-6", "7", "8-9", "10"], "5-6"),
    ("Hukum Newton ke-2 adalah...", ["F=ma", "F=Gm1m2/r²", "E=mc²", "P=V×I"], "F=ma"),
    ("Ibukota Jawa Tengah adalah...", ["Semarang", "Surakarta", "Yogyakarta", "Magelang"], "Semarang"),
    ("Urutan planet dari Matahari yang benar adalah...", ["Venus-Bumi-Mars", "Bumi-Mars-Venus", "Mars-Venus-Bumi", "Venus-Mars-Bumi"], "Venus-Bumi-Mars"),
    ("Bilangan prima terkecil adalah...", ["1", "2", "3", "5"], "2"),
    ("Benua terbesar di dunia adalah...", ["Asia", "Afrika", "Amerika", "Eropa"], "Asia"),
    ("Rumus luas segitiga adalah...", ["a×t", "1/2×a×t", "a×a", "2×a×t"], "1/2×a×t"),
    ("Negara dengan penduduk terbanyak adalah...", ["India", "China", "USA", "Indonesia"], "India"),
    ("Hasil dari 15 × 12 adalah...", ["160", "150", "180", "200"], "180"),
    ("Kata baku dari 'antri' adalah...", ["antri", "antre", "antra", "entre"], "antre"),
    ("Simbol kimia dari Emas adalah...", ["Ag", "Fe", "Au", "Cu"], "Au"),
    ("Kerajaan Hindu tertua di Indonesia adalah...", ["Majapahit", "Kutai", "Sriwijaya", "Tarumanegara"], "Kutai"),
    ("Jumlah sisi pada prisma segi lima adalah...", ["5", "7", "10", "12"], "7"),
    ("Gunung tertinggi di Indonesia adalah...", ["Rinjani", "Semeru", "Puncak Jaya", "Kerinci"], "Puncak Jaya"),
    ("Antonim dari 'optimis' adalah...", ["percaya diri", "pesimis", "cerah", "teguh"], "pesimis"),
    ("Ibukota Australia adalah...", ["Sydney", "Melbourne", "Canberra", "Perth"], "Canberra"),
    ("Tokoh penemu lampu pijar adalah...", ["Einstein", "Newton", "Edison", "Tesla"], "Edison"),
    ("Luas persegi dengan sisi 12 cm adalah...", ["144", "124", "100", "120"], "144"),
    ("Protein terdapat banyak pada...", ["Nasi", "Daging", "Gula", "Minyak"], "Daging"),
    ("Garis horizontal pada grafik adalah sumbu...", ["X", "Y", "Z", "W"], "X"),
    ("Tingkat penyerapan cahaya oleh tumbuhan dilakukan oleh...", ["klorofil", "plasma", "sitoplasma", "mitokondria"], "klorofil"),
    ("Ibukota Laos adalah...", ["Hanoi", "Vientiane", "Phnom Penh", "Bangkok"], "Vientiane"),
    ("Hasil dari √144 adalah...", ["10", "11", "12", "13"], "12"),
    ("Bapak Proklamator Indonesia adalah...", ["Soekarno-Hatta", "Soekarno-Sudirman", "Hatta-Sjahrir", "Soekarno-Soedirman"], "Soekarno-Hatta"),
    ("Lambang sila pertama Pancasila adalah...", ["Rantai", "Pohon beringin", "Bintang", "Banteng"], "Bintang"),
]

# 30 SOAL QUIZ → Mapping jurusan
QUIZ_JURUSAN = [
    ("Apakah kamu senang memecahkan soal logika atau matematika?", "Matematika"),
    ("Apakah kamu menikmati pelajaran IPA (Fisika, Kimia, Biologi) lebih dari pelajaran lainnya?", "IPA"),
    ("Apakah kamu suka memahami cara kerja mesin, alat, atau perangkat elektronik?", "Teknik Mesin"),
    ("Apakah kamu tertarik belajar pemrograman atau teknologi komputer?", "Teknik Informatika"),
    ("Apakah kamu lebih suka bekerja dengan data dibanding berinteraksi dengan banyak orang?", "Statistika"),
    ("Apakah kamu suka menggambar, mendesain, atau membuat karya seni?", "Desain Komunikasi Visual"),
    ("Apakah kamu senang berbicara di depan umum atau melakukan presentasi?", "Ilmu Komunikasi"),
    ("Apakah kamu tertarik mempelajari perilaku manusia dan psikologi?", "Psikologi"),
    ("Apakah kamu suka mengorganisir acara atau merencanakan kegiatan?", "Manajemen"),
    ("Apakah kamu senang membaca atau menulis cerita, artikel, atau opini?", "Sastra Inggris"),
    ("Apakah kamu lebih suka bekerja di lapangan dibanding di ruangan/office?", "Teknik Sipil"),
    ("Apakah kamu tertarik mempelajari bisnis, jual beli, dan manajemen?", "Manajemen"),
    ("Apakah kamu suka berdebat atau membahas isu hukum dan sosial?", "Hukum"),
    ("Apakah kamu tertarik bekerja di rumah sakit atau bidang kesehatan?", "Kedokteran"),
    ("Apakah kamu suka mempelajari bahasa asing?", "Sastra Inggris"),
    ("Apakah kamu memiliki ketertarikan pada dunia perbankan atau keuangan?", "Akuntansi"),
    ("Apakah kamu senang menganalisis grafik, angka, atau statistik?", "Statistika"),
    ("Apakah kamu tertarik pada desain rumah, gedung, atau tata ruang?", "Arsitektur"),
    ("Apakah kamu suka mengerjakan eksperimen di laboratorium?", "Farmasi"),
    ("Apakah kamu nyaman bekerja dengan anak-anak atau membantu orang lain belajar?", "Pendidikan"),
    ("Apakah kamu suka merakit atau memperbaiki sesuatu?", "Teknik Elektro"),
    ("Apakah kamu tertarik pada dunia pariwisata, perhotelan, atau pelayanan pelanggan?", "Manajemen"),
    ("Apakah kamu senang bermain alat musik, menyanyi, atau seni pertunjukan?", "Seni Rupa"),
    ("Apakah kamu tertarik belajar tentang ekonomi makro dan mikro?", "Manajemen"),
    ("Apakah kamu suka mempelajari lingkungan, bumi, dan alam?", "Kesehatan Masyarakat"),
    ("Apakah kamu tertarik dengan teknologi mesin kendaraan (otomotif)?", "Teknik Mesin"),
    ("Apakah kamu suka memikirkan ide bisnis baru?", "Bisnis Digital"),
    ("Apakah kamu ingin bekerja di bidang pemerintahan atau administrasi publik?", "Hubungan Internasional"),
    ("Apakah kamu tertarik keamanan siber atau digital forensik?", "Ilmu Komputer"),
    ("Apakah kamu suka membantu teman memahami pelajaran?", "Pendidikan")
]

# Loading Animation
def loading_animation(pesan="Memproses", durasi=2.5):
    print()
    bar_length = 40
    total_steps = 100
    step_duration = durasi / total_steps
    emojis = ["Thinking", "Brain", "Lightbulb", "Rocket", "Trophy", "Star", "Fire", "Check", "Party", "Smile"]
    for i in range(total_steps + 1):
        percent = i
        filled = int(bar_length * i // total_steps)
        bar = "█" * filled + "░" * (bar_length - filled)
        emoji = emojis[i % len(emojis)]
        sys.stdout.write(f"\r{Color.CYAN}{Color.BOLD} {pesan} {emoji} {Color.GREEN}[{bar}]{Color.END} {percent:>3}%")
        sys.stdout.flush()
        time.sleep(step_duration)
    print(f"\n{Color.GREEN}{Color.BOLD} {pesan} SELESAI!{Color.END} ")
    time.sleep(0.4)

# Input Nilai
def input_data_pengguna():
    print("="*70)
    print(f"{Color.MAGENTA}{Color.BOLD} SELAMAT DATANG DI SISTEM REKOMENDASI JURUSAN KULIAH!{Color.END}")
    print("="*70)
    nama = input(f"{Color.YELLOW} Masukkan nama kamu: {Color.END}").strip() 
    print(f"\n{Color.CYAN}Halo, {nama}! Silakan isi nilai rapor kamu.{Color.END}\n")
    print(f"{Color.BOLD} MASUKKAN NILAI RAPOR (0-100) | ketik 'u' untuk undo{Color.END}")
    print(f"{Color.YELLOW} Kosongkan semua = kembali ke menu{Color.END}")
    print("="*70)

    nilai = {}
    history = []
    keys = ['Matematika', 'IPA', 'IPS', 'Bahasa Inggris', 'Bahasa Indonesia', 'PPKN']

    for k in keys:
        while True:
            inp = input(f"{Color.CYAN} {k}: {Color.END}").strip()
            if inp.lower() == 'u' and history:
                last = history.pop()
                del nilai[last]
                print(f"{Color.YELLOW} Undo! {last} dihapus.{Color.END}")
                if not nilai:
                    return None, None
                k = last
                continue
            if inp == "":
                if not nilai: return None, None
                break
            try:
                v = float(inp)
                if 0 <= v <= 100:
                    nilai[k] = v
                    history.append(k)
                    break
                else:
                    print(f"{Color.YELLOW} Nilai harus 0-100!{Color.END}")
            except:
                print(f"{Color.YELLOW} Masukkan angka atau 'u'!{Color.END}")
    return nama, nilai

# Grafik ASCII
def grafik_ascii(nilai):
    print("\n" + "="*70)
    print(f"{Color.BOLD} GRAFIK NILAI MATA PELAJARAN{Color.END}")
    print("="*70)
    for mata, skor in nilai.items():
        bar = "█" * int(skor / 2)
        print(f" {mata:18} | {Color.GREEN}{bar:<25}{Color.END} {skor:>5.1f}")
    print("-"*70)

# Tips Belajar
def tips_belajar(nilai):
    print("\n" + "="*70)
    print(f"{Color.BOLD} TIPS BELAJAR KHUSUS{Color.END}")
    print("="*70)
    ada = False
    for mata, skor in nilai.items():
        if skor < 70:
            tip = TIPS_BELAJAR.get(mata, "Fokus pada latihan soal & pahami konsep.")
            print(f" {mata}: {skor:.1f} → {tip}")
            ada = True
    if not ada:
        print(f"{Color.GREEN} Semua nilai bagus! Pertahankan!{Color.END}")
    print("-"*70)

# Hitung Jam Belajar
def hitung_jam_belajar(nilai):
    if not nilai or all(v >= 80 for v in nilai.values()): return
    kekurangan = sum(max(0, 85 - v) for v in nilai.values())
    jam = int(kekurangan * 4)
    if jam > 0:
        print(f"\nButuh ± {jam} jam belajar ekstra untuk rata-rata 85.")
        print(f" → {jam//24} hari (6 jam/hari).")
        print("-"*70)

# Simpan Riwayat
def simpan_riwayat(nama, nilai, rekomendasi):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    try:
        with open("riwayat.txt", "a", encoding="utf-8") as f:
            f.write(f"\n{'='*50}\n")
            f.write(f"{timestamp} - {nama}\n")
            f.write(f"Nilai: {nilai}\n")
            for jur, sk in rekomendasi:
                f.write(f" - {jur} ({sk:.1f})\n")
            f.write("="*50 + "\n")
        print(f"{Color.GREEN}Riwayat disimpan!{Color.END}")
    except Exception as e:
        print(f"{Color.YELLOW}Gagal menyimpan: {e}{Color.END}")

# Simulasi UTBK
def simulasi_utbk():
    print("\n" + "="*70)
    print(f"{Color.BOLD} SIMULASI MINI UTBK (30 SOAL){Color.END}")
    print("="*70)
    soal = random.sample(SOAL_UTBK, 30)
    skor = 0
    poin_per_soal = 100 / 30
    for i, (q, p, a) in enumerate(soal, 1):
        print(f"\nSoal {i}: {q}")
        for j, c in enumerate(p, 65):
            print(f" {chr(j)}. {c}")
        jawab = input("Jawaban (A/B/C/D): ").strip().upper()
        correct = chr(65 + p.index(a))
        if jawab and jawab[0] == correct:
            skor += poin_per_soal
            print(f"{Color.GREEN} Benar! +{poin_per_soal:.2f}{Color.END}")
        else:
            print(f"{Color.YELLOW} Salah! Jawaban: {a}{Color.END}")
        time.sleep(1)
    print(f"\nSKOR AKHIR: {Color.BOLD}{skor:.1f}/100{Color.END}")
    input("\nTekan Enter...")

# Quiz Jurusan
def quiz_jurusan():
    print("\n" + "="*70)
    print(f"{Color.MAGENTA}{Color.BOLD} QUIZ MINAT & BAKAT (30 PERTANYAAN){Color.END}")
    print("="*70)

    poin = {}
    soal_dipilih = random.sample(QUIZ_JURUSAN, 30)

    for idx, (q, jurusan) in enumerate(soal_dipilih, 1):
        while True:
            jawab = input(f"{Color.YELLOW}[{idx}/30] {q}{Color.END} (y/t): ").strip().lower()
            if jawab in ['y', 'ya', 'yes', 't', 'tidak', 'no', '']:
                break
            print(f"{Color.YELLOW}Masukkan 'y' atau 't'!{Color.END}")

        if jawab in ['y', 'ya', 'yes']:
            poin[jurusan] = poin.get(jurusan, 0) + 1

    return poin

# Hitung Skor Rapor
def hitung_skor_nilai(nilai):
    m = nilai.get('Matematika', 0)
    i = nilai.get('IPA', 0)
    s = nilai.get('IPS', 0)
    bi = nilai.get('Bahasa Inggris', 0)
    bin = nilai.get('Bahasa Indonesia', 0)
    ppkn = nilai.get('PPKN', 0)

    skor = {
        "Teknik Informatika": (m*0.55 + bi*0.25 + i*0.15 + ppkn*0.05),
        "Kedokteran": (i*0.65 + m*0.20 + bi*0.10 + ppkn*0.05),
        "Hukum": (s*0.50 + bin*0.25 + ppkn*0.20 + bi*0.05),
        "Manajemen": (s*0.45 + m*0.30 + bi*0.15 + ppkn*0.10),
        "Psikologi": (s*0.45 + bin*0.25 + bi*0.20 + ppkn*0.10),
        "Ilmu Komunikasi": (bi*0.45 + bin*0.35 + s*0.15 + ppkn*0.05),
        "Arsitektur": (m*0.40 + i*0.30 + s*0.20 + ppkn*0.10),
        "Farmasi": (i*0.60 + m*0.25 + bi*0.10 + ppkn*0.05),
        "Teknik Sipil": (m*0.50 + i*0.40 + ppkn*0.10),
        "Akuntansi": (m*0.50 + s*0.35 + bi*0.10 + ppkn*0.05),
        "Hubungan Internasional": (s*0.45 + bi*0.30 + bin*0.15 + ppkn*0.10),
        "Desain Komunikasi Visual": (bin*0.40 + bi*0.30 + s*0.20 + ppkn*0.10),
        "Sastra Inggris": (bi*0.65 + bin*0.25 + s*0.10),
        "Kesehatan Masyarakat": (i*0.50 + s*0.30 + bi*0.15 + ppkn*0.05),
        "Teknik Industri": (m*0.50 + s*0.30 + bi*0.15 + ppkn*0.05),
        "Sistem Informasi": (m*0.45 + bi*0.35 + s*0.15 + ppkn*0.05),
        "Statistika": (m*0.70 + i*0.20 + ppkn*0.10),
        "Ilmu Komputer": (m*0.60 + bi*0.25 + i*0.15),
        "Pendidikan Dokter Gigi": (i*0.60 + m*0.25 + bi*0.10 + ppkn*0.05),
        "Seni Rupa": (bin*0.45 + bi*0.30 + s*0.20 + ppkn*0.05)
    }
    return skor

# Gabungkan Nilai + Quiz
def gabungkan_skor(skor_nilai, poin_quiz):
    max_poin = 30
    skor_akhir = {}

    for jurusan in skor_nilai:
        poin = poin_quiz.get(jurusan, 0)
        bobot_quiz = (poin / max_poin) * 100 if max_poin > 0 else 0
        skor_akhir[jurusan] = (skor_nilai[jurusan] * 0.6) + (bobot_quiz * 0.4)

    return sorted(skor_akhir.items(), key=lambda x: x[1], reverse=True)[:7]

# Main
def main():
    print(f"\n{Color.CYAN}{Color.BOLD} REKOMENDASI JURUSAN KULIAH {Color.END}")
    print(f"{Color.YELLOW} {datetime.datetime.now().strftime('%d %B %Y | %H:%M WIB')}{Color.END}\n")

    while True:
        print(" MENU UTAMA ".center(70, "="))
        print(f"{Color.CYAN}1. Rekomendasi Jurusan Lengkap{Color.END}")
        print(f"{Color.CYAN}2. Simulasi Mini UTBK{Color.END}")
        print(f"{Color.CYAN}3. Lihat Riwayat{Color.END}")
        print(f"{Color.CYAN}4. Keluar{Color.END}")
        pilihan = input(f"\n{Color.MAGENTA}Pilih (1-4): {Color.END}").strip()

        if pilihan == "1":
            nama, nilai = input_data_pengguna()
            if nilai is None:
                input(f"\n{Color.YELLOW}Tekan Enter untuk kembali...{Color.END}")
                continue

            loading_animation("Menganalisis nilai rapor", 2.5)
            grafik_ascii(nilai)

            loading_animation("Menjalankan quiz minat & bakat", 1)
            poin_quiz = quiz_jurusan()

            loading_animation("Menggabungkan nilai + minat", 3)
            skor_nilai = hitung_skor_nilai(nilai)
            rekomendasi = gabungkan_skor(skor_nilai, poin_quiz)

            print("\n" + "="*70)
            print(f"{Color.MAGENTA}{Color.BOLD} REKOMENDASI JURUSAN UNTUK {nama.upper()}{Color.END}")
            print("="*70)
            print(f"{Color.CYAN}{Color.BOLD}Berdasarkan Nilai + Minat & Bakatmu:{Color.END}")

            for i, (j, s) in enumerate(rekomendasi, 1):
                print(f"{Color.GREEN} {i}. {'TOP' if i==1 else ' '} {j} → {s:.1f}/100{Color.END}")

            # (FITUR KAMPUS TARGET DIHAPUS DI BAGIAN INI)

            tips_belajar(nilai)
            hitung_jam_belajar(nilai)

            print(f"\n{Color.YELLOW}MOTIVASI HARI INI:{Color.END}\n \"{random.choice(MOTIVASI)}\"")
            simpan_riwayat(nama, nilai, rekomendasi)
            input(f"\n{Color.CYAN}Tekan Enter untuk kembali...{Color.END}")

        elif pilihan == "2":
            simulasi_utbk()
        elif pilihan == "3":
            if os.path.exists("riwayat.txt"):
                try:
                    with open("riwayat.txt", "r", encoding="utf-8") as f:
                        print(f"{Color.CYAN}" + f.read() + f"{Color.END}")
                except:
                    print(f"{Color.YELLOW}Gagal membaca riwayat.{Color.END}")
            else:
                print(f"{Color.YELLOW}Belum ada riwayat.{Color.END}")
            input(f"\n{Color.CYAN}Tekan Enter...{Color.END}")
        elif pilihan == "4":
            print(f"\n{Color.GREEN}{Color.BOLD}Terima kasih! Semangat menuju kampus impian 2026!{Color.END}")
            break
        else:
            print(f"{Color.YELLOW}Pilihan tidak valid!{Color.END}")

if __name__ == "__main__":
    main()
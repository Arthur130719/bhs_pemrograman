1. Definisi

Array (dalam python) adalah struktur yang dapat menyimpan dan mengatur kumpulan data. Struktur data berbicara tentang cara menyimpan, mengatur, mengelompokkan, dan merepresentasikan data. Struktur data sangatlah penting dan harus dikuasai oleh seorang programmer. Di forum-forum pemrograman, saya sering menjumpai pertanyaan-pertanyaan yang menurut saya bisa diselesaikan jika orang tersebut memahami konsep struktur data.

Pada materi kali ini kita akan membahas tentang struktur data lanjutan yaitu himpunan dan kamus.

2. Tetapkan

Himpunan dalam bahasa pemrograman python merupakan tipe data kolektif yang digunakan untuk menyimpan beberapa nilai dalam satu variabel dengan ketentuan sebagai berikut: Iversitas

nilai anggota yang disimpan harus unik (bukan duplikat)

Nilai member yang sudah dimasukkan tidak dapat diubah lagi

⚫ set bersifat unordered alias tidak berurutan-artinya tidak bisa diakses berdasarkan indeks.

Untuk lebih memahami 3 poin di atas, langsung saja kita lakukan praktiknya.

Bentuk umum Himpunan:

# gunakan kurung kurawal

student_set = {'Huda', 'Lendis', 'Wahid', 'Basith'}

mencetak(kumpulan_siswa)

# ubah daftar menjadi kumpulan

buah_set = set(['mangga', 'Apel'])

cetak(set_buah)

# set dengan tipe data berbeda

set_mix = {'manusia', 'hewan', 5, Benar, ('A', 'B')}

print(set_mix)
D. Tambahkan/Perbarui Elemen Kumpulan

Seperti yang telah kami sebutkan di atas bahwa meskipun nilai yang ditetapkan tidak dapat diubah, namun tetap dapat ditambah dan dihapus. Kita dapat menambahkan anggota baru ke set dengan fungsi add() dan update(). Perhatikan contoh berikut:

alfabet_set = {'a', 'b', 'c'}

cetak (kumpulan abjad)

#tambahkan satu per satu

set_abjad.tambahkan('d')

set_abjad.tambahkan('e')

#tambahkan lebih dari satu anggota sekaligus

set_abjad.update({ 'f', 'g' })

# juga bisa menggunakan daftar

set_abjad.update(['h', 'i'])

cetak (kumpulan abjad)

di Undqui

...

{'a' dan 'g', 'h', 'f', 'c'}

e. Hapus/hapus Elemen Set

Untuk menghapus anggota dari suatu himpunan, ada 4 fungsi yang bisa kita gunakan:

• hapus(nilai) Untuk menghapus nilai yang dicari. Jika nilai yang dicari tidak ada maka akan terjadi error.

membuang(nilai) Untuk menghapus nilai yang dicari. Jika nilai yang dicari tidak ada maka tidak akan terjadi error.

pop() Mengambil dan menghapus nilai di sebelah kiri.

clear() Menghapus semua anggota.

Contoh:

setel {'virtual', 'berbudi luhur', 100, ('a', 'b'), salah, Benar} print(set)
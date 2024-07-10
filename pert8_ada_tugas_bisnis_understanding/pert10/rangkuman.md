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

Keluaran:

{'Wahid', 'Lendis', 'Basith', 'Huda'}

{'apel', 'mangga'}

{True, 5, ('A', 'B'), 'hewan', 'manusia'}

A. Tidak Terurut (Set)

Tipe kumpulan data tidak berurutan. Artinya, kita tidak bisa menggunakan indeks untuk mengakses nilai error: di set. Kalaupun kita memaksa, kita hanya akan mendapat

set_saya = {'a'}

cetak(set_saya[0])

Pesan eror:

Traceback (panggilan terakhir terakhir):

File "<stdin>", baris 1, di <modul>

TypeError: objek 'set' dapat disubskripkan

Kita juga bisa melihat kode program yang telah kita buat tadi:

student_set = {'Huda', 'Lendis', 'Wahid', 'Basith'} print(student_set)

Keluaran:

{'Wahid', 'Lendis', 'Basith', 'Huda'}

Dimana diatas kita definisikan 4 anggota himpunan secara berurutan: Huda, Lendis, Wahid, dan Basith. Namun setelah kami cetak, kami mendapat pesanan yang berbeda.

B. Tidak dapat diubah (Set)

Himpunan tidak dapat diubah, artinya nilai yang telah kita masukkan ke dalam himpunan tidak dapat diubah lagi. Namun, kami masih dapat menambah dan menghapus anggota ke kumpulan tersebut. Dan, karena kumpulan tidak dapat diubah, kumpulan hanya dapat menerima anggota tipe data yang juga tidak dapat diubah.

C. Tidak ada Nilai duplikat (Set)

Juga diatur dalam python tidak dapat menerima nilai duplikat. Jika kita memasukkan suatu nilai yang sudah ada pada suatu himpunan, maka nilai tersebut hanya akan muncul atau dimasukkan satu kali saja. Perhatikan contoh berikut:

kata_unik= {

'pagi', 'ini', 'adalah', 'pagi', 'yang mana',

'sangat terang'}

cetak(kata_unik)

Maka kata “pagi” hanya akan dimasukkan satu kali:

['itu', 'sangat', 'ini', 'pagi', 'cerah', 'adalah')

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

3. Kamus

Kamus merupakan tipe data pada python yang berfungsi untuk menyimpan kumpulan data/ nilai dengan pendekatan “key-value”. Kamus itu sendiri memiliki dua komponen inti: Yang pertama adalah kuncinya, yaitu nama atribut suatu item dalam kamus. Yang kedua adalah nilai, yaitu nilai yang disimpan dalam suatu atribut.

Item kamus mempunyai 3 sifat yaitu :

Tidak berurutan - tidak berurutan

• Dapat diubah dapat diubah

• Unik - alias tidak dapat menerima dua kunci yang sama

Unordered artinya tidak berurutan, jadi key/atribut yang kita definisikan terlebih dahulu, bukan berarti justru akan menjadi yang “pertama” dibandingkan dengan key yang lain. Selain itu, tidak berurutan berarti tidak dapat diakses menggunakan indeks (bilangan bulat) seperti halnya daftar.

Changeableartinya kita dapat mengubah nilai yang telah kita masukkan ke dalam kamus. Ini berbeda dengan tipe data set dan tuple, yang keduanya bersifat immutable atau tidak dapat diubah.

Dan yang terakhir Unique, kamus tidak boleh memiliki lebih dari satu kunci yang sama karena bersifat unik. Jadi jika dua kunci sama, kunci yang terakhir ditentukan akan menimpa nilai kunci yang ditentukan sebelumnya.

A. Buat Elemen Kamus

Selanjutnya cara membuat kamus dengan python. Untuk membuatnya, di sana

adalah 2 cara:

• Yang pertama dengan kurung kurawal {}.

Dan yang kedua bisa menggunakan fungsi atau konstruktor dict().

Perhatikan contoh berikut:

#Langkah pertama

buku = {

"title": "Daun Musim Gugur Tak Pernah Membenci Angin",

"Penulis": "Tere Liye"

}

# cara kedua

buku = dikte(

title="Daun Musim Gugur Tak Pernah Membenci Angin",

penulis-"Tere Liye"

)

B. Tambahkan/Perbarui Elemen Dict

Untuk menambahkan kunci dan item baru, caranya seperti mengedit item. Jadi: Jika key yang kita tentukan sudah ada, maka sistem akan mengganti item lama dengan yang baru alias mengeditnya. Namun jika kunci yang kita definisikan tidak ada, sistem akan menambahkannya sebagai item baru
murid {

'nama': 'Lendis Fabri'

'origin': 'Indonesia', }

#keluaran Tidak ada

print('Hobi:', pelajar.dapatkan('hobi'))

# tambahkan data

pelajar['hobi'] = 'Memancing'

#cetak ulang

print('Hobi {} adalah {}'.format(

siswa.dapatkan('nama'),

pelajar.mendapatkan('hobi')

))

Keluaran:

Hobi: Tidak ada

Hobi dari Lendis Fabri adalah Memancing

C. Hapus Elemen Dict

Ada dua cara untuk menghapus item:

Menggunakan pernyataan del <dict[key]>.

• Atau gunakan fungsi kamus.pop()

Perhatikan contoh berikut:

murid = {

'nama': 'Wahid Abdullah',

'usia': 18,
D. Operator Keanggotaan (Dict)

Kita dapat menggunakan operator keanggotaan untuk tipe data kamus dengan python.

Perhatikan contoh berikut:

murid {

'nama': 'Renza yang Terinspirasi'

}

08.24

print('Apakah variabel siswa mempunyai kunci nama?') print('nama' pada siswa)

print('\nApakah variabel siswa TIDAK mempunyai kunci umur?') print(catatan 'usia' pada siswa)

Keluaran:

Apakah variabel siswa memiliki key nama? True

Apakah variabel siswa TIDAK memiliki key usta?

BENAR

e. Fungsi (Kamus)

Berikut rangkuman fungsi bawaan Dict yang bisa kita gunakan: Versitas

Fungsi

semua()

Keterangan

Mengembalikan True jika semua kunci kamus adalah True (atau jika kamus kosong).

setiap()

Kembalikan Truejika salah satu kunci kamus benar. Jika kamus kosong, returnfalse.

Mengembalikan panjang (jumlah item) dalam kamus.

hanya()

cmp()

Membandingkan item dari dua kamus. (Tidak tersedia di Python 3)

diurutkan()

Mengembalikan daftar kunci baru yang diurutkan dalam kamus.
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
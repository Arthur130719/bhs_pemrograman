1. Definition

Arrays (in python) are structures that can store and organize data sets. Data structures talk about a way to store, organize, group and represent data. Data structures are very important and must be mastered by a programmer. On programming forums, I often come across questions that I think can be solved if the person understands the concept of data structures.

In this material, we will discuss advanced data structures, namely sets and dictionaries.

2. Set

A set in the python programming language is a collective data type that is used to store multiple values in a single variable with the following conditions: Iversitas

stored member values must be unique (not duplicates)

The value of the member that has been entered cannot be changed anymore

⚫ set is unordered aka unordered-which means it can't be accessed by index.

To better understand the 3 points above, we will immediately do the practice.

General form of Sets:

# use curly braces

student_set = {'Huda', 'Lendis', 'Wahid', 'Basith'}

print(student_set)

# convert list into set

fruit_set = set(['mango', 'Apple'])

print(set_fruit)

# sets with different data types

set_mix = {'man', 'animal', 5, True, ('A', 'B')}

08.24

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
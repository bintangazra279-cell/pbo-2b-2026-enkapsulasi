from book import Book
import datetime

buku1 = Book(1, "Belajar Python", "Affan", 2025)
buku2 = Book(2, "belajar java", "Budi", 2024)

print(buku1.judul)
print(buku1.get_update_terakhir())

buku1.update_judul("mulai belajar phyton bab 1 😉")

print(buku1,judul)
print(buku1.get_update_terakhir())
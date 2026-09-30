from collections import deque

# Membuat antrean
queue = deque()

# Menambahkan mahasiswa ke antrean
queue.append("Rian")
queue.append("Naufal")
queue.append("Falih Fahry")
queue.append("Raffa")

print("Antrean mahasiswa:")
print(queue)

# Melihat mahasiswa paling depan
print("\nMahasiswa paling depan:")
print(queue[0])

# Melayani mahasiswa paling depan
dilayani = queue.popleft()

print("\nMahasiswa yang dilayani:")
print(dilayani)

print("\nAntrean setelah dilayani:")
print(queue)
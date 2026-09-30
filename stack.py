# ==========================================
# STACK - FITUR UNDO
# ==========================================

# Membuat Stack
stack = []

# Menambahkan aktivitas
stack.append("Input nilai Rian")
stack.append("Input nilai Heru")
stack.append("Input nilai Aulia")

print("Aktivitas:")
print(stack)

# Undo aktivitas terakhir
undo = stack.pop()

print("\nAktivitas yang di-Undo:")
print(undo)

print("\nAktivitas setelah Undo:")
print(stack)
# Tolong buat satu array / list dari 1 sampai 100. Print semua angka ini dalam urutan terbalik, tetapi ada beberapa peraturan : 
 
# 1. Jangan print angka bilangan prima.
# 2. Ganti angka yang dapat dibagi dengan angka 3 dengan text "Foo".
# 3. Ganti angka yang dapat dibagi dengan angka 5 dengan text "Bar".
# 4. Ganti angka yang dapat dibagi dengan angka 3 dan 5 dengan text "FooBar".
# 5. Print angka menyamping tidak ke bawah.

# Membuat list dari 1 sampai 100.
arr = [i+1 for i in range(100)]

# Function untuk mengganti angka menjadi kata yang sudah ditentukan sesuai peraturan yang diberikan.
def mutate_arr(n: int) -> int|str:
    if n % 3 == 0 and n % 5 == 0:
        return "FooBar"
    elif n % 3 == 0:
        return "Foo"
    elif n % 5 == 0:
        return "Bar"
    else:
        return n
    
# Menggunakan 'map()' untuk menerapkan function pada tiap element pada list, lalu mengubah iterator ke list.
arr = [i for i in map(mutate_arr, arr)]
# Print angka menyamping tidak ke bawah dengan pemisah ','.
print(*arr, sep=", ")

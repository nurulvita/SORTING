#NAMA       : NURUL VITA AZIZAH
#NIM        : 2209116038
#KELAS      : SISTEM INFORMASI A'22

import random # library untuk menghasilkan data secara acak
import os

os.system("cls")

print(40*"-")
print(" MERGESORT ".center(40,"="))
print(40*"-")

def Merge_Sort(arr):
    if len(arr) > 1:
        # mid merupakan titik dimana elemen dalam data dibagi menjadi dua sub bar
        mid = len(arr)//2
        Left = arr[:mid] # menampilkan sub sebelah kiri
        Right = arr[mid:] # menampilkan sub sebelah kanan

        # memanggil data dalam setiap sub bar
        Merge_Sort(Left)
        Merge_Sort(Right)

        print(f"Left : {Left}")
        print(f"Right : {Right}")
        print(25*"-")

        # indeks untuk elemen kanan dan kiri
        i = 0
        j = 0
        # indeks untuk penggabungan
        k = 0

        while i < len(Left) and j < len(Right):
            # jika elemen kiri nilainya kurang dari elemen kanan maka tambahkan elemen kiri ke output
            if Left[i] < Right[j]: 
                arr[k] = Left[i]
                i += 1 # menambahkan elemen ke depan
            else:
                arr[k] = Right[j]
                j += 1
            k += 1 # memindahkan ke slot berikutnya
        
        # untuk semua elemen yang tersisa
        while i < len(Left):
            arr[k] = Left[i]
            i += 1
            k += 1

        while j < len(Right):
            arr[k] = Right[j]
            j += 1
            k += 1

# menampilkan elemen yang berada di dalam list
def inlist(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

# untuk menjalankan program
if __name__ == '__main__':
    data = []
    data = list(range(1,20)) # tipe data yang digunakan adalah list dan rentang nilai yang diambil yaitu antara 1 sampai 20
    x = random.sample(data, k=10) # untuk mendapatkan sample dari data dengan jumlah data unik yang diambil adalah 10
    print("\nSebelum disorting : ")
    print(x)
    print("")

    Merge_Sort(x) # menjalankan proses sorting

    print("")
    print("Setelah disorting : ")
    inlist(x) # hasil mergesort
    print("")

print(40*"-")
print(" QUICKSORT ".center(40,"="))
print(40*"-")

data = []
data = list(range(1, 30)) # tipe data yang digunakan adalah list dan rentang nilai yang diambil yaitu antara 1 sampai 30
acak = random.sample(data, k=10) # untuk mendapatkan sample dari data dengan jumlah data unik yang diambil adalah 10


def partition(array, begin, end):
	print("Sorting :", acak)
	print(45*"-")

	# pilih elemen paling kanan sebagai pivot
	pivot = array[end]

	# pointer untuk elemen yang lebih besar
	i = begin - 1

    # bandingkan setiap elemen dengan pivot
	for j in range(begin, end):
		if array[j] <= pivot:

            # jika elemen yang lebih kecil dari pivot ditemukan
            # tukar dengan elemen yang lebih besar yang ditunjukkan oleh i
			i = i + 1

			# menukar elemen di i dengan elemen di j
			(array[i], array[j]) = (array[j], array[i])

	# menukar elemen pivot dengan elemen yang lebih besar yang ditentukan oleh i
	(array[i + 1], array[end]) = (array[end], array[i + 1])

	# Kembalikan posisi dari mana partisi dilakukan
	return i + 1

# untuk menjalankan sorting
def quickSort(array, begin, end):
	if begin < end:

        # menemukan elemen pivot sedemikian rupa
        # elemen yang lebih kecil dari pivot ada di sebelah kiri
        # elemen yang lebih besar dari pivot ada di sebelah kanan
		pi = partition(array, begin, end)

		# memanggil elemen sebelah kiri
		quickSort(array, begin, pi - 1)

		# memanggil elemen sebelah kanan
		quickSort(array, pi + 1, end)

# menampilkan elemen yang berada di dalam list               
def dalamlist(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()

print("\nSebelum di sorting : ")
print(acak)
print("")

quickSort(acak, 0, len(acak) - 1) # menjalankan proses sorting

print("\nSetelah di sorting : ")
dalamlist(acak) # hasil quicksort
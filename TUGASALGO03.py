# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 18:48:26 2021

@author: Reza Kurniawan
"""
import math

while True:
	print("1. Jabodetabek\t(Rp. 10000)\n2. Dalam Jawa\t(Rp. 25000)\n3. Luar Jawa\t(Rp. 50000)\n(q) quit")
	
	pilihan = input('Pilih tujuan pengiriman : ')
	if pilihan == '1':
	    kota = 'Jabodetabek'
	    harga_kota = 10000
	elif pilihan == '2':
	    kota = 'Dalam jawa'
	    harga_kota =  25000
	elif pilihan == '3':
	    kota = 'Luar jawa'
	    harga_kota = 50000
	elif pilihan == 'q':
		print("\nProgram is Stopped!")
		exit(0)
	else:
		print("\nMenu tidak ditersedia, silahkan pilih ulang.")
		continue

	while True:
		print('\nBerat barang <= 20KG (Rp. 15000)\nBerat barang > 20KG tambahan (Rp. 1500) per kg\n(q) quit')
		
		berat_barang= input('Masukkan berat barang (KG) : ')
		if berat_barang == 'q':
			print("\nProgram is Stopped!")
			exit(0)
		try:
			berat_barang = float(berat_barang)
			break
		except:
			print("\nBerat Barang tidak valid, silahkan masukkan ulang.")
			continue
		
	if math.ceil(float(berat_barang)) <= 20:
	    harga_berat = 15000
	elif math.ceil(float(berat_barang)) > 20:
	    harga_berat = 15000
	    lebih = math.ceil(float(berat_barang)) - 20
	    harga_berat += lebih * 1500

	ppn = (harga_kota + harga_berat) * 0.1
	total = harga_kota + harga_berat + ppn
	
	print(f"""\n========== Rincian Biaya ==========
1. Tujuan : {kota}\t\tRp. {int(harga_kota)}
2. Berat Barang (KG) : {berat_barang}\tRp. {int(harga_berat)}
3. PPN (10 %)\t\t\tRp. {int(ppn)}
4. Total Biaya\t\t\tRp. {int(total)}
===================================\n""")

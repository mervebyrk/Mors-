#!/usr/bin/env  python
# -*- coding: utf-8 -*-

def acilis():
	global faktoriyel, permut, komb
	print ("\n")
	print ("Hoşgeldiniz\n")
	print ("(1)Faktoriyel Hesaplama\n")
	print ("(2)Permutasyon Hesaplama\n")
	print ("(3)Kombinasyon Hesaplama\n")
	print ("(4)Karekok Hesaplama\n")
	secim=(raw_input("İşlem Seçin(1-2-3-4):   "))
	print ("\n")
	if secim not in ["1","2","3","4"]:
		print ("Geçersiz Seçim. Lütfen 1 ile 4 arası bir sayi girin!")
		acilis()
	
	if secim=="1":
		e=int(input("Faktoriyel Hesapmalama için sayı girin:  "))
		fakt(e)
		print ("\n")
		print ("_ "*10,"\n")
		print (str(e)+"! = ",faktoriyel)
		print ("_ "*10)
		print ("\n")
		acilis()
	
	if secim=="2":
		f=int(raw_input("Asıl Kümenin Eleman Sayısı:   "))
		c=int(raw_input("Alt Kümelerin Eleman Sayıları:   "))
		if f>c:	
			perm(f,c)
			print ("\n")
			print ("_ "*10,"\n")
			print ("P("+str(f)+","+str(c)+") = ",permut)
			print ("_ "*10)
			print ("\n")
			acilis()
		else:
			print ("Geçersiz İşlem. Lütfen sayıları düzgün girin!")
			print ("\n")
			acilis()
			
	if secim=="3":
		a1=int(raw_input("Asıl Kümenin Eleman Sayısı: "))
		a2=int(raw_input("Alt Kümelerin Eleman Sayıları:   "))
		if a1>a2:
			komb(a1, a2)
			print ("\n")
			print ("_ "*10,"\n")
			print ("C("+str(a1)+","+str(a2)+") = ",komb)
			print ("_ "*10)
			print ("\n")
			acilis()
		
		else:
			print ("Geçersiz İşlem. Lütfen sayıları düzgün girin!")
			print ("\n")
			acilis()
	if secim=="4":
	   kk=int(raw_input("Bir sayi girin: "))
	   al=karek(kk)
	   print ("\n")
	   print ("_ "*10,"\n")
	   print (str(kk)+"! = ",al)
	   print ("_ "*10)
	   print ("\n")
	   acilis()
				
def fakt(i):
	global faktoriyel
	a=1
	k=1
	while a<i:
		k=a*k
		a=a+1
		if a==i:
			faktoriyel=a*k
	
def perm(l,n):
	global faktoriyel, permut
	lfakt=0
	nfakt=0
	fakt(l)
	lfakt=faktoriyel
	faktoriyel=1
	fakt(l-n)
	nfakt=faktoriyel
	permut=lfakt/nfakt
	
def komb(y,z):
	global permut, komb, faktoriyel
	perm(y,z)
	fakt(z)
	komb=permut/faktoriyel
	
def karek(k):
        x=1.0
        for i in range(1,1000):
           x=0.5*(x+(k/x))
        return x
        
		
print ("\n"*3)
acilis()

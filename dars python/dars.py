# Mssivlar bir olchovli












# import math

# list1 = list(range(1,12,3))
# print(list1)

# list2 = ["Abu"]*10
# print(list2)

# list3 = []
# print(list3)

# print(len(list1),len(list2),len(list3))


# sonlar = list(range(1,21))
# for i in sonlar: 
#     print(f"{i} ning ildizi {math.sqrt(i)} ga teng")

# print(sonlar[3:10])

# sonlar.append(25)
# sonlar.append("Mominov")
# print(sonlar)

# sonlar.pop()
# print(sonlar)

# sonlar.pop(0)
# print(sonlar)

# sonlar.insert(1,"Salom jonm")
# print(sonlar)

# sonlar.remove(8)
# print(sonlar)


# sonlar1 = sonlar.copy()
# sonlar.clear()
# print(sonlar)
# print(sonlar1)


# guruh1 = ["Abu","Ali","Ibn","Sino"]
# guruh2 = ["Alisher","Navoiy","Amir","Temur"]

# guruh1.extend(guruh2)
# print(guruh1[4])

# 5 ta shahar nomidan iborat bolgan royhat 
# va birinchi, uchinchi va oxirgi shaharni chiqaring

# guruh3 = ["Toshkent","Samarqand","Fargona","Andijon","Xorazim"]

# print(guruh3[0],guruh3[2],guruh3[4])

# list5 = list(range(1,51,2))
# print(list5)

# n = int(input("N:"))
# list6 = [0]*n
# print(list6)

# n = int(input("n="))
# royxat = [0]*n
# for i in range*(n):
#     royxat[i] = int(input(f"{i} - index kiriting:"))
# Faraz qilaylik, ro'yxat "sonlar" nomi bilan berilgan
# n = len(sonlar) mid = n // 2
# if n % 2 == 1: 
#     print(royxat)



# while True:
#     n = int(input("n:"))
#     if n == 0:
#         print("Dastur tugadi")
#         break



# parol = 1234
# i = 1
# while i <=5:
#     foy = int(int(input("Parolni kiriting:")))
#     if foy == parol:
#         print("Marhamat")
#         break
#     elif i == 5:
#         print("Bloklandi")
#     else:
#         print(f"Sizda{5-i} ta urinish qoldi. \nIltimos parolni qaytadan kiriting")
#         i +=1

# n = int(input("n sonini kiriting:"))
# son = 0
# for i  in range(1, n +1):
#     if n % i == 0:
#         son +=1
# if son ==2:
#     print("Tub son")
# else:
#     print("Tub son emas")

#Uyga vazifa








#1.	n ta son kiritib, ularning yig'indisi va o'rtacha qiymatini sum() ishlatmasdan toping.
# n = int(input("n ni kiriting: ")) 
# yigindi = 0 
# for i in range(n):
#     yigindi += float(input(f"{i+1}-sonni kiriting: ")) 
# ortacha = yigindi / n if n > 0 else 0 
# print("Yigindi:", yigindi) 
# print("Ortacha qiymat:", ortacha)




#2.	Ro'yxatdagi toq indeksli elementlar yig'indisini va juft indeksli elementlar yig'indisini solishtiring
# lst = [10, 20, 30, 40, 50, 60] 
# juft_sum = 0 
# toq_sum = 0
# for i in range(len(lst)): 
#     if i % 2 == 0: 
#         juft_sum += lst[i] 
#     else: toq_sum += lst[i]
# print("Juft indekslar yig'indisi:", 
#     juft_sum) 
# print("Toq indekslar yig'indisi:", toq_sum) 
# if juft_sum > toq_sum: 
#     print("Juft indeksdagilar yigindisi katta") 
# elif toq_sum > juft_sum: 
#     print("Toq indeksdagilar yigindisi katta") 
# else: 
#     print("Teng")



#3.	Ro'yxatdagi musbat elementlar ko'paytmasini toping (musbat element bo'lmasa, mos xabar chiqaring).

# lst = [-2, 5, -3, 4, 0, 3] 
# kopaytma = 1 
# bor = False
# for x in lst: 
#     if x > 0: 
#         kopaytma *= x 
#         bor = True
#     if bor: 
#         print("Musbat elementlar ko'paytmasi:", kopaytma) 
#     else: 
#         print("Musbat element bolmasa")




#4.	Haftalik xarajatlar (7 ta qiymat) kiritilsin: umumiy xarajat va kunlik o'rtacha xarajatni toping
# xarajatlar = [] 
# for i in range(1, 8):
#     xarajatlar.append(float(input(f"{i}-kunlik xarajatni kiriting:")))
# umumiy = sum(xarajatlar)
# ortacha = umumiy / 7 
# print("Umumiy xarajat:", umumiy)
# print("Kunlik ortacha xarajat:", ortacha)





#5.	Ro'yxat elementlarining o'rtacha qiymatiga eng yaqin elementni toping.
# lst = [10, 15, 20, 30, 40] 
# ortacha = sum(lst) / len(lst)
# eng_yaqin = lst[0] 
# eng_kichik_farq = abs(lst[0] - ortacha)
# for x in lst: 
#     farq = abs(x - ortacha) 
#     if farq < eng_kichik_farq: 
#         eng_kichik_farq = farq 
#         eng_yaqin = x
# print("Ortacha qiymat:", ortacha) 
# print("Eng yaqin element:", eng_yaqin)






#6.	Ro'yxatdagi eng katta va eng kichik element orasidagi farqni (diapazonni) max()/min() ishlatmasdan toping.
# lst = [15, 3, 9, 27, 4, 1] 
# katta = lst[0] 
# kichik = lst[0]
# for x in lst: 
#     if x > katta: 
#         katta = x 
#     if x < kichik: 
#         kichik = x
# farq = katta - kichik 
# print("Eng katta va eng kichik element farqi (diapazon):", farq)




#7.	Eng kichik elementning birinchi va oxirgi uchragan indeksini toping.
# lst = [5, 2, 8, 2, 9, 2, 7] 
# min_val = min(lst)
# birinchi_idx = None 
# oxirgi_idx = None
# for i in range(len(lst)): 
#     if lst[i] == min_val: 
#         if birinchi_idx is None: 
#             birinchi_idx = i 
#             xirgi_idx = i
# print("Eng kichik element:", min_val) 
# print("Birinchi uchrash indeksi:", birinchi_idx) 
# print("Oxirgi uchrash indeksi:", oxirgi_idx)





#8.Ro'yxatdagi ikkinchi eng katta elementni toping (eng katta element bir necha marta uchrashi mumkin).
# lst = [12, 45, 2, 45, 30, 25] 
# katta1 = None 
# katta2 = None
# for x in lst: 
#     if katta1 is None or x > katta1: 
#         katta2 = katta1 
#         katta1 = x 
#     elif x != katta1 and (katta2 is None or x > katta2): 
#         katta2 = x
# if katta2 is not None: 
#     print("Ikkinchi eng katta element:", katta2) 
# else: 
#     print("Ikkinchi eng katta element yo'q")




#9.Maksimal element nechta marta uchrashini bitta sikl yordamida aniqlang
# lst = [5, 9, 2, 9, 3, 9, 1] 
# maks = lst[0] 
# soni = 0
# for x in lst: 
#     if x > maks: 
#         maks = x 
#         soni = 1 
#     elif x == maks: 
#         soni += 1
# print("Maksimal element:", maks) 
# print("Uchrashlar soni:", soni)





#10.Ro'yxatdagi eng katta elementdan oldin joylashgan elementlar yig'indisini toping.
# lst = [2, 5, 3, 10, 7, 4] 
# max_idx = 0 
# for i in range(1, len(lst)): 
#     if lst[i] > lst[max_idx]: 
#         max_idx = i
# yigindi = 0 
# for i in range(max_idx): 
#     yigindi += lst[i]
# print("Eng katta elementgacha bolgan yigindi:", yigindi)




#11.Ro'yxatdagi musbat, manfiy va nol elementlar sonini bitta siklda sanang.
# lst = [-3, 0, 5, 2, -1, 0, 8] 
# musbat = 0 
# manfiy = 0 
# nol = 0
# for x in lst: 
#     if x > 0: 
#         musbat += 1 
#     elif x < 0: 
#         manfiy += 1 
#     else: 
#         nol += 1
# print("Musbatlar soni:", musbat) 
# print("Manfiylar soni:", manfiy) 
# print("Nollar soni:", nol)












# 15-Oktabr Mavzu: Bir olchovli massivlar










#13.	Ro'yxat elementlarini juft va toq sonlar ro'yxatlariga ajrating.
# sonlar = list(range(2,150,3))
# new_list = []
# for i in range(len(sonlar)):
#     if sonlar[i]>=10 and sonlar[i]<=99:
#         new_list.append(sonlar[i])

# juft_sonlar = []
# toq_sonlar = []

# for son in new_list:
#     if son % 2 == 0:
#         juft_sonlar.append(son)
#     else:
#         toq_sonlar.append(son)
# print(f"Toq sonlar:",toq_sonlar)
# print(f"Juft sonlar:",juft_sonlar)

#Ballar ro'yxatini baholarga aylantiring: 86,100, 5, 71,85, 4, 56,70,3, qolgani 2.
# royxat = [10,11,12,13,14,15]
# yangi_royxat = []
# for son in royxat:
#     yangi_royxat.append(son*2)
# print(f"Royxat",royxat)
# print(f"Yanfi royxat",yangi_royxat)


#Har bir elementni 2 ga ko'paytirib, natijalardan yangi ro'yxat hosil qiling; asl ro'yxat o'zgarmaganini ko'rsating.
# ballar = [92, 78, 65, 45, 88, 71, 56, 100, 40] 
# baholar = []
# for ball in ballar: 
#     if 86 <= ball <= 100: 
#         baholar.append(5) 
#     elif 71 <= ball <= 85: 
#         baholar.append(4) 
#     elif 56 <= ball <= 70: 
#         baholar.append(3) 
#     else: baholar.append(2)
# print("Asl ballar:", ballar) 
# print("Chiqarilgan baholar:", baholar)


# list1 = [1,2,3,4,5]
# list2 = list1*2
# print(list2)

#Chiziqli qidirish
# elementlar = ["Olma","Nok","Uzum","Bexi","Shaftoli","Uzum"]
# print(elementlar)
# qidir = "Uzum"
# for i in range(len(elementlar)):
#     if qidir == elementlar[i]:
#         print(f"{qidir} soni {i+1}-indeksda turibdi")


#Qidirish va saqlash algoritmlari
# x in a -->> True False

# a = [14, 7, 23, 7]
# qidiruv = 4
# for x in a:
#     if x == qidiruv:
#         print(f"{x} element mavjud {a} ning ichida")
#         break
#     else:
#         print(f"{x} mavjud emas")

# #enumerate(i,x) -->> i - index, x - element

# for i,x in enumerate(a):
#     print(f"{i} - indexda {x} turibdi")


# a = [14, 7, 23, 7]
# qidiruv = 7
# for i,x in enumerate(a):
#     if x == qidiruv:
#         print(f"{i}-indexda {x} element  {a} ning ichida")
# else:
#         print(f"{x} mavjud emas")



# sonlar = [1,2,3,4,5,6,7,8,9,10]
# qidir = 10
# if qidir in sonlar:
#     print(f"{qidir} mavjud")
# else:
#     print(f"{qidir} mavjud emas")


# print(f"{sonlar.index(qidir)} - indexda {qidir} turibdi")
# print(f"{sonlar.count(qidir)} - ta {qidir} bor")



# a = [-15,-14,-13,-12,-11,-10,9,8,7,6,5,4,3,2,1]
# n = len(a)
# # for i in range(n - 1):
# #     for j in range(n - 1 - i):
# #         if a[j] > a[j + 1]:
# #             a[j],a[j + 1] = a[j + 1], a[j]
# #     print(f"{i + 1} - otish: {a}")
# print(f"Sorted yordamida {sorted(a)}")   















# Ikki  olchovli massivlar


# a = "salom,alik,xayr"
# b = a.split(",")
# print(b)

# a = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     [10,11,12],
#     [13,14,15]
# ]
# print(a)
# print(a[0][0])
# print(a[0][-1])
# print(a[-1][-1])
# print(a[1])



# #Ustun ajratish
# ustun = []
# for qator in  a:
#     # ustun.append(qator[0])
#     ustun.append(qator[-1])    
# print(ustun)



# a = []
# for i in range(3):
#     qator = []
#     for j in range(3):
#         n = int(input(f"a [{i+1}] [{j+1}] = "))
#         qator.append(n)
#     a.append(qator)
# print(a)


# b = [[0]*4 for i in range(3)]
# print(b)



# a = []
# son = 1
# for i in range(3):
#     qator = []
#     for j in range(4):
#         qator.append(son)
#         son += 1
#     a.append(qator)
#     print(a [i])








# -------------------------------------------4 - Noyabr Mavzu: Stringlar--------------------------------------------------------


# ' - single quote
# " - double toute
# Bitta satr uchun ma'lumot oladi obyekt yaratadi

# text  = "salom bugun \"5\" baxo oldim"
# print(text)



# -------------------------------------------String bilan ishlash metodlari-------------------------------------------

# Python'da stringlar bilan ishlash uchun ko‘plab metodlar mavjud.



# upper() - Harflarni katta qiladi

# lower() - Harflarni kichik qiladi

# title() - Har bir so‘z boshini katta qiladi

# capitalize() - Birinchi harfni katta qiladi

# replace() - Matnni almashtiradi

# strip() - Ortiqcha bo‘sh joylarni olib tashlaydi

# find() - Belgining o‘rnini topadi



#-------------------------------------------Operatori yordamida formatlash-------------------------------------------
#Bu usulda maxsus belgilar orqali o‘zgaruvchilar matnga joylashtiriladi.



# %s - String (matn)

# %d - Butun son

# %f - Haqiqiy son

# %.2f - Verguldan keyin 2 ta raqam





#-------------------------------------------Index - Slicing-------------------------------------------

# text = "Ali kelyapti"
# print(text)
# text = text.replace("Ali","Vali")
# print(text)
# text = text.upper()
# print(text)
# text = text.lower()
# print(text)
# text = text.capitalize()
# print(text)
# text = text.title()
# print(text)





#-------------------------------------------1. Ism va familiyani birlashtirish va uzunligini chiqarish

# ism = input("Ismingizni kiriting: ")
# familiya = input("Familiyangizni kiriting: ")

# ism_familiya = ism + " " + familiya

# print("To'liq ism:", ism_familiya)
# print("Uzunligi:", len(ism_familiya))





# #-------------------------------------------2. Birinchi, o‘rtadagi va oxirgi belgilarni chiqarish

# matn = input("Matn kiriting: ")

# print("Birinchi belgi:", matn[0])
# print("O'rtadagi belgi:", matn[len(matn)//2])
# print("Oxirgi belgi:", matn[-1])


# #-------------------------------------------3. Kiritilgan satrni teskari tartibda chiqarish

# matn = input("Matn kiriting: ")

# print("Teskari matn:", matn[::-1])



# #-------------------------------------------4. Faqat juft indeksli belgilarni chiqarish

# matn = input("Matn kiriting: ")

# print("Juft indeksli belgilar:", matn[::2])


# #-------------------------------------------5. Kiritilgan so‘z palindrom ekanini aniqlash

# soz = input("So'z kiriting: ")

# if soz.lower() == soz[::-1].lower():
#     print("Palindrom")
# else:
#     print("Palindrom emas")



# #-------------------------------------------6. Birinchi va oxirgi belgilarni almashtirish

# matn = input("Matn kiriting: ")

# yangi = matn[-1] + matn[1:-1] + matn[0]

# print("Yangi satr:", yangi)



# #-------------------------------------------7. Matndagi unli harflar sonini topish

# matn = input("Matn kiriting: ")

# unlilar = "aeiou"
# sanoq = 0

# for harf in matn.lower():
#     if harf in unlilar:
#         sanoq += 1

# print("Unli harflar soni:", sanoq)



# #-------------------------------------------8. Berilgan belgi necha marta uchrashini sikl yordamida sanash

# matn = input("Matn kiriting: ")
# belgi = input("Belgi kiriting: ")

# sanoq = 0

# for harf in matn:
#     if harf == belgi:
#         sanoq += 1

# print("Belgi qatnashgan soni:", sanoq)




# #-------------------------------------------9. Harflar, raqamlar, probellar va boshqa belgilar sonini sanash

# matn = input("Matn kiriting: ")

# harf = 0
# raqam = 0
# probel = 0
# boshqa = 0

# for belgi in matn:
#     if belgi.isalpha():
#         harf += 1
#     elif belgi.isdigit():
#         raqam += 1
#     elif belgi.isspace():
#         probel += 1
#     else:
#         boshqa += 1

# print("Harflar:", harf)
# print("Raqamlar:", raqam)
# print("Probellar:", probel)
# print("Boshqa belgilar:", boshqa)




# #-------------------------------------------10. Belgining birinchi va oxirgi uchragan indekslarini topish

# matn = input("Matn kiriting: ")
# belgi = input("Belgi kiriting: ")

# birinchi = matn.find(belgi)
# oxirgi = matn.rfind(belgi)

# if birinchi != -1:
#     print("Birinchi indeks:", birinchi)
#     print("Oxirgi indeks:", oxirgi)
# else:
#     print("Belgi topilmadi")


# #-------------------------------------------11. Belgining barcha uchragan indekslarini chiqarish

# matn = input("Matn kiriting: ")
# belgi = input("Belgi kiriting: ")

# for i in range(len(matn)):
#     if matn[i] == belgi:
#         print("Indeks:", i)



# #-------------------------------------------12. Matndagi katta va kichik harflar sonini topish

# matn = input("Matn kiriting: ")

# katta = 0
# kichik = 0

# for belgi in matn:
#     if belgi.isupper():
#         katta += 1
#     elif belgi.islower():
#         kichik += 1

# print("Katta harflar:", katta)
# print("Kichik harflar:", kichik)
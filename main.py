# 1-m
summa = int(input("Xarid summasini kirit: "))

if summa > 0:
    if summa < 50000:
        print("Chegara yoq")
    elif summa < 100000:
        print("5% chegerma")
    elif summa < 200000:
        print("10% chegirma")
    else:
        print("15% chegirma")
else:
    print("Manfiy summa")


# 2-m
i = input("svitafor rangi: ")

if i == "Qizil":
    print("Toxtang")
elif i == "Sariq":
    print("Tayyorlaning")
elif i == "Yashil":
    print("Yuring")
else:
    print("Xato")



# 3-m
i = int(input("Soat kirit: "))

if 6 >= i >= 12:
    print("Ertalabki dori")
elif 12 >= i >= 18:
    print("Kunduzki dori")
elif 18 >= i >= 00:
    print("Kecki dori")
else:
    print("Xozi dori ichish kerak emas!")



# 4-m
i = int(input("Harorat kirit: "))

if i < 0:
    print("Qalin palto")
elif i < 15:
    print("Jaket kiying")
elif i <= 25:
    print("Fotbolka yetadi")
else:
    print("Yengil kiyim soyabon oling")




# 5-m
sinf = int(input("O‘quvchi sinfini kiriting (1–9): "))
ogirlik = float(input("Sumka og‘irligini kiriting (kg): "))

if 1 <= sinf <= 4 and ogirlik > 2:
    print("Og‘ir, kamaytiring!")
elif 5 <= sinf <= 9 and ogirlik > 4:
    print("Og‘ir, kamaytiring!")
else:
    print("Normal")


# 6-m
i = int(input("Yosh kirit: "))
a = input("og'ir yoki oddiy: ")

if 10 <= i <= 70:
    print("Zudlik bilan")
elif a == "Og'ir bolsa":
    print("1-soat ichida")
else:
    print("3-soat ichida")


# 7-m
kun = input("Kun turini kiriting (ish / dam olish): ").lower()
masofa = float(input("Masofani kiriting (km): "))

if kun == "dam olish":
    km_narx = 3600
else:
    km_narx = 3000

umumiy_narx = km_narx * masofa

if masofa >= 10:
    umumiy_narx *= 0.9

print("Yakuniy narx:", umumiy_narx, "so‘m")



# 8-m
harorat = float(input("Haroratni kiriting (°C): "))
yomgir = float(input("Yomg‘ir ehtimolini kiriting (%): "))

if yomgir >= 70:
    print("Uyda qoling")
elif harorat < 5:
    print("Juda sovuq, sayr qilish tavsiya etilmaydi")
else:
    print("Ajoyib kun, sayrga boring!")


# 9-m
daromad = float(input("Oylik daromadingizni kiriting: "))
xarajat = float(input("Oylik xarajatlaringizni kiriting: "))

if xarajat > daromad:
    print("Xavfli! Xarajatlarni kamaytiring")
elif xarajat == daromad:
    print("Aynan yetarli")
else:
    print("Ajoyib! Tejamkorlik qilyapsiz")


# 10-m
tur = input("Velosiped turini kiriting (shahar / sport): ").lower()
vaqt = int(input("Ijaraga olingan vaqtni kiriting (soat): "))

if tur == "shahar":
    soat_narx = 10000
else:
    soat_narx = 15000

umumiy_narx = soat_narx * vaqt

if vaqt >= 5:
    umumiy_narx *= 0.8 
elif vaqt >= 3:
    umumiy_narx *= 0.9

print("Yakuniy ijara narxi:", umumiy_narx, "so‘m")








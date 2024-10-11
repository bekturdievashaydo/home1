# 1-mashq:
# Quyidagi o'zgaruvchilarni yarating:
kocha="Bog'bon"

mahalla="Sog'bon"

tuman="Bodomzor"

viloyat="Samarqand"
#
# Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
kocha = "Bog'bon"

mahalla = "Sog'bon"

tuman = "Bodomzor"

viloyat = "Samarqand"

# Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati
print(kocha + " ko'chasi", mahalla + " mahallasi", tuman + " tumani", viloyat + " viloyati")

# 2-mashq:
# Yuqoridagi o'zgaruvchilarning (kocha, mahalla, tuman, viloyat) qiymatini foydalanuvchidan so'rang. Va avvalgi mashqni takrorlang.
kocha = input("Ko'changizni nomini kiriting:")
print(kocha + " ko'chasi")

mahalla = input("Mahallangizni nomini kiriting:")
print(mahalla + " mahallasi")

tuman = input("Tumaningni nomini kiriting:")
print(tuman + " tumani")

viloyat = input("Viloyatingizni nomini kiriting:")
print(viloyat + " viloyati")

# 3-mashq:
# Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan yozing
kocha = "Bog'bon"

mahalla = "Sog'bon"

tuman = "Bodomzor"

viloyat = "Samarqand"

print(kocha + " ko'chasi\n", mahalla + " mahallasi\n", tuman + " tumani\n", viloyat + " viloyati")


# Yuqoridagi matnni f-string yordamida, yangi, manzil deb nomlangan o'zgaruvchiga yuklang
yangi_manzil = f"{kocha} {mahalla} {tuman} {viloyat}"

# manzilga biz yuqorida o'rgangan title(), upper(), lower() , capitalize() metodlarini qo'llab ko'ring.
print(yangi_manzil.title())
print(yangi_manzil.upper())
print(yangi_manzil.lower())
print(yangi_manzil.capitalize())

# 4-mashq:
# Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur tuzing
person = input("Son kiriting:")
person1 = int(person)**2
person2 = int(person)**3
print(f"{person} ning kvadrati {person1} ga teng!")
print(f"{person} ning kubi {person2} ga teng!")

# 5-mashq:
# Foydalanuvchining yoshini so'rab, uning tug'ilgan yilini hisoblab, konsolga chiqaruvchi dastur tuzing
foydalanuvchi = input("Yoshingizni kiriting:")
yosh = 2024-int(foydalanuvchi)
print(f"Siz {yosh}-yilda tug'ilgansiz!")

# 6-mashq:
# Foydalanuvchidan ikki son kiritshni so'rab, kiritilgan sonlarning yig'indisi, ayirmasi, ko'paytmasi va bo'linmasini chiqaruvchi dastur
son1 = input("1-sonni kiriting:")
son2 = input("2-sonni kiriting:")

plus = int(son1) + int(son2)
print(f"Yig'indisi: {plus} ga teng ")
minus = int(son1) - int(son2)
print(f"Ayirmasi: {minus} ga teng")
multi = int(son1) * int(son2)
print(f"Ko'paytmasi: {multi} ga teng")
bolish = int(son1) / int(son2)
print(f"Bo'linmasi: {bolish} ga teng")

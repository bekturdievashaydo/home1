# 1.
juft = int(input("Juft son kiriting:"))
if juft % 2 == 0:
    print("Rahmat!")
else:
    print("Bu son juft emas.")

# 2
#
yosh = int(input('Yoshingiz nechida? '))
if yosh < 4 or yosh > 60:
    price = 0
elif yosh < 18:
    price = 10000
elif yosh >= 18:
    price = 20000
print(f"Sizga kirish {price} so'm")

# 3
son1 = float(input("Birinchi sonni kiriting: "))
son2 = float(input("Ikkinchi sonni kiriting: "))
if son1 > son2:
    print("Birinchi son ikkinchi sondan katta.")
elif son1 < son2:
    print("Birinchi son ikkinchi sondan kichik.")
else:
    print("Ikkita son teng.")

# 4
son = int(input("Iltimos, biror butun sonni kiriting: "))

for n in range(2, 11):
    if son % n == 0:
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi.")

# 5
oila = {
    "otam": {
        "ismi": "Bobomurod",
        "tugilgan_yili": 1983,
        "shahri": "Xorazm viloyati"
    },
    "onam": {
        "ismi": "Zuxra",
        "tugilgan_yili": 1985,
        "shahri": "Xorazm viloyati"
    },
    "opam": {
        "ismi": "Gullola",
        "tugilgan_yili": 2005,
        "shahri": "Urganch"
    },
    "ukam": {
        "ismi": "Davlatyor",
        "tugilgan_yili": 2018,
        "shahri": "Xorazm"
    }
}

for family, malumot in oila.items():
    print(
        f"{family.capitalize()}ning ismi {malumot['ismi']}, {malumot['tugilgan_yili']}-yilda, {malumot['shahri']}da tug'ilgan.")

# 6
taomlar = {
    "Otam": "osh",
    "Onam": "manti",
    "Opam": "kabob",
    "Kamola": "salat",
    "O'g'iloy": "qozon kabobi"
}

for ism, taom in taomlar.items():
    print(f"{ism}ning sevimli taomi {taom}.")

# 7
izohli_lugat = {
    "integer": "Butun son - o'nlik sonlar qismiga ega bo'lmagan son.",
    "float": "Haqiqiy son - o'nlik sonlar qismi bo'lgan son.",
    "string": "Qator - matn yoki belgilardan iborat ma'lumot turi.",
    "if": "Agar - shartli ifoda, shart to'g'ri bo'lsa bajariladi.",
    "else": "Aks holda - agar if sharti noto'g'ri bo'lsa bajariladigan kod.",
    "for": "Takrorlash - biror amallarni bir necha marta bajarish uchun ishlatiladi.",
    "while": "Davr - shart to'g'ri bo'lganda davom etadigan takrorlash.",
    "def": "Funktsiya - kodni qayta ishlatish uchun funksiyani belgilash.",
    "list": "Ro'yxat - bir nechta ma'lumotlarni saqlash uchun foydalaniladigan tuzilma.",
    "dictionary": "Lug'at - kalit-qiymat juftliklarini saqlaydigan tuzilma."
}
for lugat, tarjima in izohli_lugat.items():
    print(f"{lugat}: {tarjima}")

# 8
lugat = input("Iltimos, tarjimasini bilmoqchi bo'lgan so'zni kiriting: ")

if lugat in izohli_lugat:
    print(f"{lugat}: {izohli_lugat[lugat]}")
else:
    print("Bunda so'z mavjud emas.")

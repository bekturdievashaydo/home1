# 1-mashq
sozlar = {
    "o'zgaruvchi": "Ma'lumotni saqlash uchun joy.",
    "funksiya": "Takrorlanadigan kod bloklari.",
    "ro'yxat": "Elementlar to'plami.",
    "dasturlash": "Muammolarni yechish jarayoni.",
    "klass": "Ob'ektga yo'naltirilgan dasturlashda ma'lumotlar va funksiyalar to'plami.",
    "modul": "Boshqa fayl yoki kutubxona.",
    "tsikl": "Takrorlanadigan operatsiyalar.",
    "shart": "Qaysi bir shart bajarilganida kod bajarilishi.",
    "malumot": "Dasturda ishlatiladigan barcha ma'lumotlar.",
    "xatolik": "Kodda aniqlangan muammo."
}

for kalit in sorted(sozlar):
    print(f"{kalit}: {sozlar[kalit]}")


#
# 2-mashq
davlatlar = {
    "O'zbekiston": "Toshkent",
    "AQSH": "Vashington",
    "Rossiya": "Moskvа",
    "Fransiya": "Parij",
    "Xitoy": "Peкин",
    "Indoneziya": "Jakarta",
    "Braziliya": "Brasilia",
    "Germaniya": "Berlin",
    "Italiya": "Rim",
    "Yaponiya": "Tokio"
}

print("Davlatlar:")
for davlat in sorted(davlatlar):
    print(davlat)


print("\nPoytaxtlar:")
for poytaxt in sorted(set(davlatlar.values())):
    print(poytaxt)

#
# 3-mashq
davlatlar = {
    "O'zbekiston": "Toshkent",
    "AQSH": "Vashington",
    "Rossiya": "Moskva",
    "Fransiya": "Parij",
    "Xitoy": "Pekin",
    "Indoneziya": "Jakarta",
    "Braziliya": "Brasilia",
    "Germaniya": "Berlin",
    "Italiya": "Rim",
    "Yaponiya": "Tokio"
}

davlat = input("Iltimos, davlat nomini kiriting: ")

if davlat in davlatlar:
    print(f"{davlat} ning poytaxti: {davlatlar[davlat]}")
else:
    print("Bizda bunday ma'lumot yo'q.")


# 4-mashq
menu = {
    "Pizza": 50000,
    "Burger": 30000,
    "Sushi": 70000,
    "Pasta": 40000,
    "Salat": 25000,
    "Kofta": 45000,
    "Kebab": 60000,
    "Sho'rva": 20000,
    "Chips": 15000,
    "Desert": 30000
}


buyurtmalar = []
for i in range(3):
    taom = input(f"{i + 1}-taomni kiriting: ")
    buyurtmalar.append(taom)


for taom in buyurtmalar:
    if taom in menu:
        print(f"{taom} narhi: {menu[taom]} so'm.")
    else:
        print(f"Bizda '{taom}' taomi yo'q.")

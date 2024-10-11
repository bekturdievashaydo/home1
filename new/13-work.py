# 1-mashq
mashhur_shaxslar = [
    {
        "ism": "Abu Abdulloh Muhammad ibn Ismoil",
        "tug_yil":  810,
        "t_joy": "Buxoro",
        "umr": 60,
    },
    {
        "ism": "Abdulla Qodiriy",
        "tug_yil":  1894,
        "t_joy": "Toshkent",
        "umr": 44,
    },
    {
        "ism": "Erkin Vohidov",
        "tug_yil":  1936,
        "t_joy": "Farg'ona",
        "umr": 80,
    },
    {
        "ism": "Alisher Navoiy",
        "tug_yil":  1441,
        "t_joy": "Xirot",
        "umr": 60,
    }
]

for shaxs in mashhur_shaxslar:
    print(f"{shaxs['ism']} "
          f"{shaxs ['tug_yil']}-yilda "
          f"{shaxs['t_joy']}da tavvalud topgan "
          f"{shaxs['umr']}yil umr ko'rgan.")

# 3-mashq:
ismi = "Ali"

sevimli_kinolar = {
    "Ali": ["Terminator", "Rambo", "Titanic"]
}

print(f"{ismi}ning sevimli kinolari:")
for kino in sevimli_kinolar[ismi]:
    print(f"{kino}")
print()


ismi = "Vali"

sevimli_kinolar = {
    "Vali": ["Tenet", "Inception", "Interstellar"]
}

print(f"{ismi}ning sevimli kinolari:")
for kino in sevimli_kinolar[ismi]:
    print(f"{kino}")
print()

ismi = "Hasan"

sevimli_kinolar = {
    "Hasan": ["Abdullajon", "Bomba", "Shaytanat"]
}

print(f"{ismi}ning sevimli kinolari:")
for kino in sevimli_kinolar[ismi]:
    print(f"{kino}")
print()

ismi = "Husan"

sevimli_kinolar = {
    "Husan": ["Mahallada duv-duv gap", "John Wick"]
}

print(f"{ismi}ning sevimli kinolari:")
for kino in sevimli_kinolar[ismi]:
    print(f"{kino}")

# 4-mashq
davlatlar = {
    "O'zbekiston": {
        "poytaxt": "Toshkent",
        "aholi_soni": "34 million",
        "rasmiy_tili": "O'zbek tili",
        "valyuta": "O'zbek so'mi"
    },
    "AQSh": {
        "poytaxt": "Vashington, D.C.",
        "aholi_soni": "331 million",
        "rasmiy_tili": "Ingliz tili",
        "valyuta": "AQSh dollari"
    },
    "Rossiya": {
        "poytaxt": "Moskvа",
        "aholi_soni": "146 million",
        "rasmiy_tili": "Rus tili",
        "valyuta": "Rubl"
    },
    "Xitoy": {
        "poytaxt": "Pekin",
        "aholi_soni": "1.4 milliard",
        "rasmiy_tili": "Xitoycha",
        "valyuta": "Yuan"
    }
}

for davlat, malumot in davlatlar.items():
    print(f"{davlat}:")
    for kalit, qiymat in malumot.items():
        print(f"  {kalit}: {qiymat}")
    print()

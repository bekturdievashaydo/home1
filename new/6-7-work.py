#  1-mashq:
# ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
# Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring
ismlar = ['Shaxnoza', 'Shaydo', 'Shabnam']
print(f"Assalomu aleykum " + (ismlar[0]) + " yaxshimisiz!")
print(f"Assalomu aleykum " + (ismlar[1]) + " yaxshimisiz!")
print(f"Assalomu aleykum " + (ismlar[2]) + " yaxshimisiz!")
# 2-mashq:
# sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik).
# Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring.
sonlar = [+10,-29,18,36.2]
print((sonlar[0]) + (sonlar[3]))
print((sonlar[2]) - (sonlar[1]))
print((sonlar[0]) * (sonlar[3]))
print((sonlar[1]) / (sonlar[0]))
print(sonlar[2] + 25)
print(sonlar[0] - 4)
sonlar[3] = 46.24
print(sonlar[3])
sonlar[2] = 59
print(sonlar[2])
#
# 3-mashq:
# t_shaxslarva z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting.
# Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib oling (pop())

t_shaxslar = ['Abdulla Oripov', 'Zulfiya', 'Davinchi']
z_shaxslar = ['Den Broun', "Billie Eilish", 'Xcho']
name = t_shaxslar.pop(2)
name1 = z_shaxslar.pop(1)

# 4-mashq:friendsnomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.
#
# Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang.
#
# Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing
friends = []
friends.append("Shodiya")
friends.append("Oygul")
friends.append("Shahnoza")
friends.append("Kamola")
friends.append("Shaydo")
print(friends)

friends.remove("Kamola")
friends.remove("Oygul")
print(friends)

friends.insert(0, "Elif")
friends.insert(3, "Shabnam")
print(friends)

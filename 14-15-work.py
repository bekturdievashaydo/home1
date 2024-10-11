# # 1-mashq
print('sevimli kitobllaringiz')
savol = 'sevimli kitobingizni kiriting'
savol+="(dasturni toxtatish uchun 'stop' deb yozing)"
qiymat=""
while qiymat !='stop':
    qiymat = input(savol)
    print(qiymat)

# # 2-mashq
while True:
    yosh = input("Iltimos, yoshingizni kiriting (yoki 'exit' / 'quit' deb yozing): ")

    if yosh.lower() in ['exit', 'quit']:
        print("Dastur to'xtatildi.")
        break

    try:
        yosh = int(yosh)

        if yosh < 7:
            chipta_narhi = 2000
        elif 7 <= yosh < 18:
            chipta_narhi = 3000
        elif 18 <= yosh < 65:
            chipta_narhi = 10000
        else:
            chipta_narhi = 0

        print(f"Sizning chipta narhingiz: {chipta_narhi} so'm")

    except ValueError:
        print("Iltimos, to'g'ri yosh kiriting.")
# 3-mashq
buyurtma = []

while True:
    mahsulot = input("Iltimos, mahsulot nomini kiriting (yoki 'stop' deb yozing): ")

    if mahsulot.lower() == 'stop':
        break

    buyurtma.append(mahsulot)
    print(f"'{mahsulot}' mahsuloti buyurtma ro'yxatiga qo'shildi.")

print("\nBuyurtma ro'yxati:")
for i in buyurtma:
    print(f"- {i}")
# 4-mashq
mahsulotlar = {}

while True:
    mahsulot = input("Mahsulot nomini kiriting (tugash uchun 'stop' deb yozing): ")

    if mahsulot.lower() == 'stop':
        break

    narh = input(f"{mahsulot} ning narhini kiriting: ")

    mahsulotlar[mahsulot] = narh

print("\nSiz kiritgan mahsulotlar va narhlari:")
for mahsulot, narh in mahsulotlar.items():
    print(f"{mahsulot}: {narh}")

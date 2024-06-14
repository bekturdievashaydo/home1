print('buyurtma qabul qiluvchi dastur.')
savol='iltimos,buyurtma bering'
savol+="(dasturni yoxtatish uchun 'end' deb yozin): "
buyurtma=''
while buyurtma !='end':
    buyurtma=input(savol)
    if buyurtma !='end':
        print(buyurtma)


print('e-bozor uchun mahsulotlar va ularnig narxlarini saqlaymiz.')
mahsulotlar={}
ishora=True
while ishora:
    mahsulot=input("mahsulot nomini kiriting:")
    narx=input(f"{mahsulot.title()}ning narxini kiriting:")
    mahsulotlar[mahsulot]=int(narx)

    javob=input("yana nimadir qoshasizmi?(ha/yoq")
    if javob =="yo":
        ishora=False

for mahsulot,narx in mahsulotlar.items():
    print(f"{mahsulot.title()}{narx} som")



buyurtmalar = ['pomidor','gilos', 'banan']
mahsulotlar = {'pomidor':80000,
                       'gilos': 25000,
                       'banan': 18000}
while buyurtmalar:
            buyurtma = buyurtmalar.pop()
            if buyurtma in mahsulotlar.keys():
                narh = mahsulotlar[buyurtma]
                print(f"{buyurtma.title()} - {narh} so'm")
            else:
                print(f"Bizda {buyurtma} yo'q")





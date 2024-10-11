# # # #
# # # #
# # # #
# # # # print('sevimli kitobllaringiz')
# # # # savol = 'sevimli kitobingizni kiriting'
# # # # savol+="(dasturni toxtatish uchun 'stop' deb yozing)"
# # # # qiymat=""
# # # # while qiymat !='stop':
# # # #     qiymat = input(savol)
# # # #     print(qiymat)
# # # #
# # # #
# # # #
# # # # while True:
# # # #     yosh = input("Iltimos, yoshingizni kiriting (yoki 'exit' / 'quit' deb yozing): ")
# # # #
# # # #     if yosh.lower() in ['exit', 'quit']:
# # # #         print("Dastur to'xtatildi.")
# # # #         break
# # # #
# # # #     try:
# # # #         yosh = int(yosh)
# # # #
# # # #         if yosh < 7:
# # # #             chipta_narhi = 2000
# # # #         elif 7 <= yosh < 18:
# # # #             chipta_narhi = 3000
# # # #         elif 18 <= yosh < 65:
# # # #             chipta_narhi = 10000
# # # #         else:
# # # #             chipta_narhi = 0
# # # #
# # # #         print(f"Sizning chipta narhingiz: {chipta_narhi} so'm")
# # # #
# # # #     except ValueError:
# # # #         print("Iltimos, to'g'ri yosh kiriting.")
# # # #
# # # #
# # # #
# # # # buyurtma = []
# # # #
# # # # while True:
# # # #     mahsulot = input("mahsulot kiriting (toxtatiw uchun 'stop' deb yozing): ")
# # # #
# # # #     if mahsulot.lower() == 'stop':
# # # #         break
# # # #
# # # #     buyurtma.append(mahsulot)
# # # #     print(f"'{mahsulot}' mahsuloti buyurtma ro'yxatiga qo'shildi.")
# # # #
# # # # print("\nBuyurtma ro'yxati:")
# # # # for i in buyurtma:
# # # #     print(f"- {i}")
# # # #
# # # #
# # # #
# # # #
# # # #
# # # # mahsulotlar = {}
# # # #
# # # # while True:
# # # #     mahsulot = input("Mahsulot nomini kiriting (toxtatiw uchun 'stop' deb yozing): ")
# # # #
# # # #     if mahsulot.lower() == 'stop':
# # # #         break
# # # #
# # # #     narh = input(f"{mahsulot} narhini kiriting: ")
# # # #
# # # #     mahsulotlar[mahsulot] = narh
# # # #
# # # # print("\nSiz kiritgan mahsulotlar va narhlari:")
# # # # for mahsulot, narh in mahsulotlar.items():
# # # #     print(f"{mahsulot}: {narh}")
# # # #
# # #
# # # def salom_ber(ism):
# # #     print(f"'sssalomu aleykum, hurmatli {ism.title()}")
# # # salom_ber('hasan')
# # # print(salom_ber.__doc__)
# #
# #
# #
# # def toliq_ism(ism,familia):
# #     print(f"foydalanuvchi ismi{ism.title()}\n"
# #           f"foydalanuvci familiasi: {familia.title()}")
# # toliq_ism('bilolbek',"karimov")
# #
# #
# #
# #
# def yosh_hisobla(tugilganyil,joriyyil=2024):
#     print(f"siz {joriyyil-tugilganyil}yoshdasiz")
#
# yosh_hisobla(2009)


def toliqismyasa(ism,familia,otaism=''):
    if otaism:
        toliqism = f"{ism} {otaism} {familia}"
    else:
        toliqism = f"{ism} {familia}"

    # toliqism = f"{ism} {familia}"

    return toliqism.title()

talaba1 = toliqismyasa('olim','mpmom')

talaba2 = toliqismyasa('shado','bekturdieva')
print(f"darsga klemagan talaba{talaba1} va {talaba2}")
# print(toliqismyasa('shaydo','uralov'))
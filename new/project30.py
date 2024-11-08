# #case1
# son = int(input("1 dan 7 gacha son kiriting: "))
#
# match son:
#     case 1:
#         print("Dushanba")
#     case 2:
#         print("Seshanba")
#     case 3:
#         print("Chorshanba")
#     case 4:
#         print("Payshanba")
#     case 5:
#         print("Juma")
#     case 6:
#         print("Shanba")
#     case 7:
#         print("Yakshanba")
#     case _:
#         print("Xato: 1 dan 7 gacha son kiriting")
#
#
#
# #case2
# son = int(input("1 dan 5 gacha baho kiriting: "))
#
# match son:
#     case 1:
#         print("Yomon")
#     case 2:
#         print("Qoniqarsiz")
#     case 3:
#         print("Qoniqarli")
#     case 4:
#         print("Yaxshi")
#     case 5:
#         print("A'lo")
#     case _:
#         print("Xato: 1 dan 5 gacha baho kiriting")
#
#
#
#
# #case3
# oy = int(input("Oy raqamini kiriting: "))
#
# match oy:
#     case 12 | 1 | 2:
#         print("Qish")
#     case 3 | 4 | 5:
#         print("Bahor")
#     case 6 | 7 | 8:
#         print("Yoz")
#     case 9 | 10 | 11:
#         print("Kuz")
#     case _:
#         print("1 dan 12 gacha oy raqami kiriting")
#

# #case4
# oy = int(input("Oy raqamini kiriting: "))
#
# match oy:
#     case 1 | 3 | 5 | 7 | 8 | 10 | 12:
#         print("31 kun bor")
#     case 4 | 6 | 9 | 11:
#         print("30 kun bor")
#     case 2:
#         print("28 yoki 29 kun bor")
#     case _:
#         print("1 dan 12 gacha oy raqami kiriting")
#
#
#
# #case5
# A = float(input("A sonini kiriting: "))
# B = float(input("B sonini kiriting: "))
# amal = int(input("Amalni tanlang (1- Qo'shish, 2- Ayirish, 3- Bo'lish, 4- Ko'paytirish): "))
#
# match amal:
#     case 1:
#         print("Natija:", A + B)
#     case 2:
#         print("Natija:", A - B)
#     case 3:
#         if B != 0:
#             print("Natija:", A / B)
#         else:
#             print("Xato: Nolga bo'lib bo'lmaydi")
#     case 4:
#         print("Natija:", A * B)
#     case _:
#         print("1 dan 4 gacha amal tanlang")
#
#
#
# #case6
# birlik = int(input("Uzunlik birligini tanlang (1-desimetr, 2-kilometr, 3-metr, 4-millimetr, 5-santimetr): "))
# qiymat = float(input("Uzunlikni kiriting: "))
#
# match birlik:
#     case 1:
#         print("Metrlarda:", qiymat * 0.1)
#     case 2:
#         print("Metrlarda:", qiymat * 1000)
#     case 3:
#         print("Metrlarda:", qiymat)
#     case 4:
#         print("Metrlarda:", qiymat * 0.001)
#     case 5:
#         print("Metrlarda:", qiymat * 0.01)
#     case _:
#         print("Xato: 1 dan 5 gacha birlik tanlang")
#
#
# #case7
# birlik = int(input("Og'irlik birligini tanlang (1-kilogramm, 2-milligramm, 3-gramm, 4-tonna, 5-sentner): "))
# qiymat = float(input("Og'irlikni kiriting: "))
#
# match birlik:
#     case 1:
#         print("Kilogrammlarda:", qiymat)
#     case 2:
#         print("Kilogrammlarda:", qiymat * 0.000001)
#     case 3:
#         print("Kilogrammlarda:", qiymat * 0.001)
#     case 4:
#         print("Kilogrammlarda:", qiymat * 1000)
#     case 5:
#         print("Kilogrammlarda:", qiymat * 100)
#     case _:
#         print("Xato: 1 dan 5 gacha birlik tanlang")
#
#
# #case8
# yil = int(input("Yilni kiriting: "))
# oy = int(input("Oy raqamini kiriting: "))
# kun = int(input("Kun raqamini kiriting : "))
#
# # Kabisa yilini aniqlash
# kabisa = (yil % 4 == 0 and yil % 100 != 0) or (yil % 400 == 0)
#
# match oy:
#     case 1:
#         kun_raqami = kun
#     case 2:
#         kun_raqami = 31 + kun
#     case 3:
#         kun_raqami = 59 + kun if not kabisa else 60 + kun
#     case 4:
#         kun_raqami = 90 + kun if not kabisa else 91 + kun
#     case 5:
#         kun_raqami = 120 + kun if not kabisa else 121 + kun
#     case 6:
#         kun_raqami = 151 + kun if not kabisa else 152 + kun
#     case 7:
#         kun_raqami = 181 + kun if not kabisa else 182 + kun
#     case 8:
#         kun_raqami = 212 + kun if not kabisa else 213 + kun
#     case 9:
#         kun_raqami = 243 + kun if not kabisa else 244 + kun
#     case 10:
#         kun_raqami = 273 + kun if not kabisa else 274 + kun
#     case 11:
#         kun_raqami = 304 + kun if not kabisa else 305 + kun
#     case 12:
#         kun_raqami = 334 + kun if not kabisa else 335 + kun
#
# print(f"Yil boshidan boshlab {kun_raqami}-kun")
#
#
#
# #case9
# oy = int(input("Oy raqamini kiriting: "))
# kun = int(input("Kun raqamini kiriting: "))
# kabisa = int(input("Kabisa yilmi? (1-Ha, 0-Yo'q): "))
#
# kunlar = {1: 31, 2: (29 if kabisa else 28), 3: 31, 4: 30, 5: 31, 6: 30,
#           7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
#
# if kun < kunlar.get(oy, 0):
#     kun += 1
# else:
#     kun = 1
#     oy += 1
#     if oy > 12:
#         oy = 1
#
# #case12
#import math
#
#
# #case14
# def teng_tomonli_uchburchak_elementlarini_topish(element_turi, qiymat):
#     match element_turi:
#         case 1:  # Tomon berilgan
#             a = qiymat
#             R1 = a * math.sqrt(3) / 6  # Ichki radius
#             R2 = a * math.sqrt(3) / 3  # Tashqi radius
#             S = (a**2 * math.sqrt(3)) / 4  # Yuza
#         case 2:  # Ichki radius berilgan
#             R1 = qiymat
#             a = R1 * 6 / math.sqrt(3)
#             R2 = a * math.sqrt(3) / 3
#             S = (a**2 * math.sqrt(3)) / 4
#         case 3:  # Tashqi radius berilgan
#             R2 = qiymat
#             a = R2 * 3 / math.sqrt(3)
#             R1 = a * math.sqrt(3) / 6
#             S = (a**2 * math.sqrt(3)) / 4
#         case 4:  # Yuza berilgan
#             S = qiymat
#             a = math.sqrt((S * 4) / math.sqrt(3))
#             R1 = a * math.sqrt(3) / 6
#             R2 = a * math.sqrt(3) / 3
#
#     return {"Tomon (a)": a, "Ichki radius (R1)": R1, "Tashqi radius (R2)": R2, "Yuza (S)": S}
#
#
# element_turi = int(input("Qaysi element berilganligini tanlang (1-tomon, 2-ichki radius, 3-tashqi radius, 4-yuza): "))
# qiymat = float(input("Berilgan qiymatni kiriting: "))
#
#
# natija = teng_tomonli_uchburchak_elementlarini_topish(element_turi, qiymat)
# print("Teng tomonli uchburchak elementlari:", natija)
#
#
#
# #case15
# qiymat = int(input("Karta qiymatini kiriting (6-14): "))
# tur = int(input("Karta turini kiriting (1-4): "))
#
#
#
# match qiymat:
#     case 11:
#         qiymat_nom = "Valet"
#     case 12:
#         qiymat_nom = "Dama"
#     case 13:
#         qiymat_nom = "Qiroq"
#     case 14:
#         qiymat_nom = "Tuz"
#     case _ if 6 <= qiymat <= 10:
#         qiymat_nom = str(qiymat)
#     case _:
#         qiymat_nom = None
#
#
# match tur:
#     case 1:
#         tur_nom = "Ishq"
#     case 2:
#         tur_nom = "Olma"
#     case 3:
#         tur_nom = "Chillak"
#     case 4:
#         tur_nom = "Qarg’a"
#     case _:
#         tur_nom = None
#
#
#
# if qiymat_nom and tur_nom:
#     print(f"{qiymat_nom} {tur_nom}")
# else:
#     print("Noto'g'ri qiymat yoki tur kiritildi")
#
#
# #case16
#
# yosh = int(input("Yoshingizni kiriting (20-69): "))
#
#
# match yosh:
#     case 20:
#         yosh_nom = "Yigirma yosh"
#     case 30:
#         yosh_nom = "O‘ttiz yosh"
#     case 40:
#         yosh_nom = "Qirq yosh"
#     case 50:
#         yosh_nom = "Ellik yosh"
#     case 60:
#         yosh_nom = "Oltmish yosh"
#     case _ if 20 < yosh < 30:
#         yosh_nom = f"Yigirma {yosh % 10} yosh"
#     case _ if 30 < yosh < 40:
#         yosh_nom = f"O‘ttiz {yosh % 10} yosh"
#     case _ if 40 < yosh < 50:
#         yosh_nom = f"Qirq {yosh % 10} yosh"
#     case _ if 50 < yosh < 60:
#         yosh_nom = f"Ellik {yosh % 10} yosh"
#     case _ if 60 < yosh < 70:
#         yosh_nom = f"Oltmish {yosh % 10} yosh"
#     case _:
#         yosh_nom = None  # Agar noto'g'ri yosh kiritilsa, None bo'ladi
#
#
# if yosh_nom:
#     print(yosh_nom)
# else:
#     print("Noto'g'ri yosh kiritildi")
#
#
#
#
#
#
#
# #case18
#
# son = int(input("Uch xonali sonni kiriting (100-999): "))
#
#
# birliklar = {
#     1: "bir", 2: "ikki", 3: "uch", 4: "to'rt", 5: "besh",
#     6: "olti", 7: "yetti", 8: "sakkiz", 9: "to'qqiz"
# }
# onliklar = {
#     1: "o'n", 2: "yigirma", 3: "o'ttiz", 4: "qirq", 5: "ellik",
#     6: "oltmis", 7: "yetmis", 8: "sakson", 9: "to'qson"
# }
# yuzliklar = {
#     1: "bir yuz", 2: "ikki yuz", 3: "uch yuz", 4: "to'rt yuz", 5: "besh yuz",
#     6: "olti yuz", 7: "yetti yuz", 8: "sakkiz yuz", 9: "to'qqiz yuz"
# }
#
#
# yuzlik = son // 100
# onlik = (son // 10) % 10
# birlik = son % 10
#
#
# yuzlik_soz = yuzliklar.get(yuzlik, "")
# onlik_soz = onliklar.get(onlik, "")
# birlik_soz = birliklar.get(birlik, "")
#
#
# natija = f"{yuzlik_soz} {onlik_soz} {birlik_soz}"
# print(natija)
#
#

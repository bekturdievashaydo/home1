# son=1
# while son<=5:
#     print(son,end='')
# #     son=son+1
# print('kiritilgan sonning kvadratini aniqlab beruvchi dastur')
# savol='istalgan sonni kiriting'
# savol+="(dasturni toxtatish ucun 'exit'deb yozing):"
# qiymat=''
# while qiymat !='exit':
#     qiymat=(input(savol))
#     if qiymat !='exit':
#         print(float(qiymat)**2
# # print('kiritilgan sonning kvadratini aniqlab beruvchi dastur')
# # savol='istalgan sonni kiriting'
# # savol+="(dasturni toxtatish ucun 'exit'deb yozing):"
# # ishora=True
# #
# #
# #
#
# sonlar=list(range(1,11))
# # for son in sonlar:
# #     if son ==6:
# #         break
# #     print(f"{son}ning kvatrati {son**2}ga teng")
# #
# #
# #
# # print('yaqiin dostlaringiz ismini kiriting,')
# # n=1
# # savol=f"{n}-dostingiz issmini kiriting:"
# # ism=input(savol)
# # ismlar.append(ism)
# # javob=input(('yana ism qoshasizmi?  (ha/yoq'))
# # if javob =='ha':
# #     n+=1
# #     continue
# # else:
# #     break
#
#

print('dosttlaringiz yoshini saqlaymiz.')
dostla={}
ishora=True
while ishora:
    ism=input('dostingizni ismini kiriting:')
    yosh=input(f"{ism.title()}ning yoshini kiriting:")
    dostla[ism]=int(yosh)
    javob=input('yana malumat kiritasizmi?  (ha/no)')
    if javob == "no":
        ishora=False

for ism,yosh in dostla.items():
    print(f"{ism.title()} {yosh} yoshda")

# #
# # cars=['lacetti','nexia','malibu','nexia','nexia','matiz']
# # while 'nexia' in cars:
# #     cars.remove('nexia')
# # print(cars)
#
# talabalar=['jonibek','husan']
# baholangan_talabalar={}
# while talabalar:
#     talaba=talabalar.pop()
#     baho=input(f"{talaba.title()}ning bahosini kiriting")
#     print(f"{talaba.title()}baholandi")
#     baholangan_talabalar[talaba]=baho
#     print(baholangan_talabalar)
#






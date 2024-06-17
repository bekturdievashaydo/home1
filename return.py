ef user_malumot(ism,familiya,t_yil,t_joy,t_raqam):
    malumot={ism:'ism',
             familiya:'familiya',
             t_joy:'t_joy',
             t_yil:'t_yil',
             t_raqam:'t_raqam'}
    return malumot



    malumot1=user_malumot('shaydo','bekturdieva','2008','urganch shahri',897654567)
    malumotlar=[malumot1]
    print('foydalanuvchining haqida malumot')
    for malumot in malumotlar:
        print(f"{malumot['ism']}{mmalumot['familiya']}{malumot['t_yil']}{malumot['t_joy']}{malumot[t_raqam]}")





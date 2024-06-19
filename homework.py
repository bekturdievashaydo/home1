

def summa(*sonlar):
    kopaytma = 1
    for son in sonlar:
      kopaytma *= son
    return kopaytma
print(summa(5,7,45,46,89,90))


def malumot ( ism,familiya,**malumotlar):
        malumotlar['ism']=ism
        malumotlar['familiya']=familiya
        return malumotlar

malumot1 = malumot("shaydo", "bekturdieva", t_yil='2008', t_joy='urrganch shahri')
print(malumot1)






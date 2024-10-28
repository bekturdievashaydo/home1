class Shaxs:
    def __init__(self, ism, familiya, passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passpport = passport
        self.tyil = tyil

    def get_info(self):
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport: {self.passpport}, {self.tyil}-yilda tugilgan"
        return info
    def get_age(self,yil):
        return yil-self.tyil

# inson = Shaxs("Egambergebnov","Otabek","AB456456",2001)
#
# print(f"{inson.get_info()}. {inson.get_age(2024)} yoshda")

class Talaba(Shaxs):
    def __init__(self,ism,familiya,passport,tyil,idraqam, manzil):
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil
    def get_id(self):
        return self.idraqam

    def get_bosqich(self):
        return self.bosqich

    def get_info(self):
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqam,{self.idraqam}-yilda tugilgan"
        return info

class Manzil:
    def __init__(self, uy, kocha, tuman, viloyat):
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat

    def get_manzil(self):
        manzil = f"{self.viloyat} viloyati, {self.tuman} shahar. "
        manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
        return manzil

talaba_manzili = Manzil("208a","Partov", "Urganch", "Xorazm")
talaba = Talaba("bekturdiyeva","shaydo","AB654649687",2001, "000065", talaba_manzili)
print(f"{talaba.get_info()}, Bosqich: {talaba.get_bosqich()}, Id raqami:{talaba.get_id()}. {talaba.get_age(2024)}-yoshda\n"
      f"{talaba_manzili.get_manzil()}")

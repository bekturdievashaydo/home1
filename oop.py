class user:
    def __init__(self,ism,user_ism,email):
        self.ism= ism
        self.user_ism = user_ism
        self.email = email


#     def tanishtirish(self):
#         print(f"ismim {self.ism} user nikim {self.user_ism} emailim {self.email}")
# user1= user('shaydo','B_shaydo','@shaydobekturdieva')
# print(user1.ism,user1.user_ism,user1.email)#
#
# user1= user('shaydo','B_shaydo','@shaydobekturdieva')
# user1.tanishtirish()



    def get_ism(self):
       return self.ism

    def get_username(self):
       return self.user_ism

    def get_email(self):
        return self.email



    def tanishtirish(self):
      print(f"ismim {self.ism} user nikim {self.user_ism} emailim {self.email}")
user1= user('shaydo','B_shaydo','@shaydobekturdieva')
print(user1)

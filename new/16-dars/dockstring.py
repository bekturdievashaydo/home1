
def tugilgan_yil_hisobla(h_yil=2024):
    ismi = input("Ismingizni kiriting: ")
    yosh = int(input("Yoshingizni kiriting: "))
    print(f"{ismi}, siz {h_yil-yosh}- yilda tug'ilgansiz")

tugilgan_yil_hisobla()


def sonni_hisobla():
    son = int(input("Sonni kiriting: "))

    kvadrat = son ** 2
    kub = son ** 3

    print(f"{son} ning kvadrati: {kvadrat}")
    print(f"{son} ning kubi: {kub}")

sonni_hisobla()


def j_yoki_t():
    son = int(input("Sonni kiriting: "))

    if son % 2 == 0:
        print(f"{son} soni juft son.")
    else:
        print(f"{son} soni toq son.")

j_yoki_t()



def kattason():
    son1 = int(input("Birinchi sonni kiriting: "))
    son2 = int(input("Ikkinchi sonni kiriting: "))

    if son1 > son2:
        print(f"Katta son: {son1}")
    elif son1 < son2:
        print(f"Katta son: {son2}")
    else:
        print("Sonlar teng.")

kattason()

print("""
ATM MAKİNESİNE HOŞGELDİNİZ.
İŞLEM YAPMAK İSTEDİĞİNİZ ALANI KONTROL EDİNİZ.
1. BAKİYE SORGULAMA
2. PARA YATIRMA
3. PARA ÇEKME
İSLEM YAPMAK İSTEMİYORSANIZ "q"" YA BASINIZ.
""")

bakiye = 0

while True:
    işlem = input("işlemi seçiniz: ")

    if (işlem == "q"):
        print("Lütfen kartınızı alınız.İşleminiz sonlandırılmıştır")
        break
    elif (işlem == "1"):
        print("Bakiyeniz {} TL'dir".format(bakiye))

    elif (işlem == "2"):

        while True:
            miktar = int(input("Lütfen yatırmak istediğiniz tutarı giriniz: "))
            if (miktar == 0):
                print("Lütfen geçerli miktarı giriniz")
            else:
                break

        bakiye = bakiye + miktar

    elif (işlem == "3"):
        while True:
            miktar = int(input("Lütfen çekmek istediğiniz tutarı giriniz: "))

            if (bakiye - miktar < 0 ):
                print("Hesabınızda yeterli bakiye bulunmamaktadır. Lütfen geçerli miktarı giriniz")
                continue
            else:
                break
        bakiye = bakiye - miktar

    else:
        print("GEÇERSİZ İŞLEM !!")



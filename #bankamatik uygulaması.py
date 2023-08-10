#bankamatik uygulaması

Cerenhesap = {
    "ad": "Ceren Yılmaz",
    "hesapNumarası": "254578",
    "bakiye": 4000,
    "ekhesap": 5000
}

Kemalhesap = {
    "ad": "Kemal Demir",
    "hesapNumarası": "987456",
    "bakiye": 7000,
    "ekhesap": 4000
}

def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye']>= miktar):
        hesap['bakiye'] -= miktar
        print("paranızı alabilirsiniz.")
        bakiyeSorgula(hesap)

    else:
        toplam= hesap['bakiye']+ hesap['ekhesap'] 

        if(toplam >= miktar):
            ekHesapKullanimi= input("ek hesabı kullanmak istiyor musunuz?(e/h)")

            if ekHesapKullanimi== "e":
                ekhesapkullanilacakmiktar= miktar - hesap['bakiye']
                hesap['bakiye']= 0
                hesap['ekhesap']-= ekhesapkullanilacakmiktar
                print("paranızı alanilirsiniz")
                bakiyeSorgula(hesap)

            else:
                print(f"{hesap['hesapNumarası']} nolu hesabınızda{hesap['bakiye']}bulunmaktadır")    
        else:
            print(("bakiye yetersiz"))
            bakiyeSorgula(hesap)

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNumarası']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekhesap']} TL bulunmaktadır.")

paraCek(Cerenhesap, 2000)
bakiyeSorgula(Cerenhesap)
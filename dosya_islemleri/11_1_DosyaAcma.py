def oku(dosyaAdi):
    try:
        file=open(dosyaAdi,"r",encoding="utf-8")
       # for i in file:
       #     print(i)
        veriler=file.read()
        file.close()
        print(str(veriler))
    except Exception as err:
        print(err)

def yaz(dosyaAdi,icerik):
    try:
        file=open(dosyaAdi,"w",encoding='utf-8')
        file.write(icerik+"\n")
        file.close()
        print("Kayıt yapıldı.")
    except Exception as err:
        print(err)


def icerikGirme(gelen):
    while True:
        if gelen=="q":
            break
        else:
            try:
                file=open(dosyaAdi,"w",encoding='utf-8')
                file.write(gelen+"\n")
                file.close()   
                print("İçerik kaydedildi.")
            except Exception as err:
                print(err)



def uzerineYaz(dosyaAdi,icerik):
    try:
        file=open(dosyaAdi,"a",encoding='utf-8')
        file.write(icerik+"\n")
        file.close()
        print("Ekleme yapıldı.")
    except Exception as err:
        print(err)



dosyaAdi=input("Dosya adı:  ")
dosyaAdi="C:\\Users\\Zeynep\\Desktop\\111\\"+dosyaAdi
icerik1=input("İçerik: ")
icerik2=input("Ekleme: ")
yaz(dosyaAdi,icerik1)
uzerineYaz(dosyaAdi,icerik2)
oku(dosyaAdi)


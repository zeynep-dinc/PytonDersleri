
liste=["1","2","3","5a","10b","abc",3,4,5,-8]
for x in liste:
    try:
        result=int(x)
        print(result)
    except ValueError:
        continue

while True:
    gelen=input("Değer: ")
    if gelen=="q":
        break
    try:
        result=float(gelen)
    except ValueError:
        print("Geçersiz değer")

turkce=['ş','ç','İ','ğ','ü','ö','ı']

def kontrol(sifre):
    for i in sifre:
        if i in turkce:
            raise("Türkçe karakter girdiniz.")
        else:
            pass
    print("Şifre geçerli.")
try:
    sifre=input("Şifreniz: ")
    kontrol(sifre)
except TypeError:
    print("Geçersiz karakter")

def faktoriyel(x):
    x=int(x)
    if x<0:
       raise ValueError('Negatif')
    result=1
    for i in range(1,x+1):
        result*=i
    return result
    

for x in liste:
    try:
        y=faktoriyel(x)
    except ValueError as err:
        print(err)
        continue
    print(y)

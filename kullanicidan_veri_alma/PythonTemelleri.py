# diyez, hastag ile yorumlar yapılıyor.
"""eğer uzuuuuuuuuuuun satırlar boyu yorumlar yapmak
istiyorsanız bu şekil 3 tırnak gerek
ctrl+k+shift ile silme yapabilirsin
"""
#değişken tanımlama ve veri tipleri
x= 1
y=5.3
name='mat'
isStudent=False
print('x ->',x)
print('y ->',y)
print('lesson name ->',name)
print('isStudent ->',isStudent)

#genel olarak tür dönüşümleri bu şekilde
#değişken ismi= istenen tip(değiştirilmek istenen değişken ismi)
'''int to float'''
x=float(x)
print(x)
topla=x+y
print('x+y->',topla)

isStudent=str(isStudent)
print('isStudent* ->',isStudent)
print(type(isStudent))


#Kullanıcıdan veri alma
name=input("Adınız Nedir: ")
isStudent=input("Öğrenci misin: 0 evet/1 hayır")
x=int(input("Yaşın: "))
y=float(input(" Aylık Gelirin: "))
if(isStudent=="0"):
    isStudent=str('öğrenci')
else:
    isStudent=str('çalışan')
print("Hoşgeldiniz, saygı değer, ",name,
x," yaşında aylık ",y," gelirine sahip bir ",
isStudent," bireysiniz.")


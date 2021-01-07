#Bir liste oluşturalım ve ismi yiyecekler olsun
#liste asağıdaki gibi tanımlanır
yiyecekler=["makarna","kebap","pizza","börek","kek","hamburger","kurabiye","börek"]
#(yazar burada diyette olduğunu ve hasret kaldığı bazı şeylere özlemini dile getirmek istemiştir :) )
#bir başka yöntemi ise
icecekler="kola;gazoz;fanta;şekerli çay;rakı;bira;şarap".split(';')
#Eğer isterseniz ";" yerine başka bir ayıraçta kullanabilirsiniz. Hiçbir şey kullanmazsanız
# boşlukları otomatik olarak ayıracaktır split fonksiyonu

#Gelelim işlemlere
#index komutu 
'''
listeAdi.index(element,start,end)
element: aranan eleman
start(başlangıç): (opsiyonel) bu index'i aramak için nereden başlanılacağını gösteriyor
end(son): yine opsiyonel bu index'i aramak için nereye kadar gidebileceğimizi gösteriyor
Dikkat edilmesi gereken noktalar;
 + arama yaparken listelere 0'dan başladığımızı unutmamak gerekiyor
 + listenin son elemanı n-1 oluyor 
 + fonksiyon başlangıçtan son-1 değerine kadar bakar
 + eğer aralık verilmediyse listede ilk bulduğu elemanın indexini verir
 + bir sınır belirtilmediyse 0'dan sona tüm listeye bakılır
'''
# Hamburger kaçıncı sırada diye arayalım 0'dan başladıkları için beklenen sonuç 5
# aralık belirtmezsek
hamburgerSiraNo=yiyecekler.index('hamburger')
print(hamburgerSiraNo) #5

#sadece başlangıç belirtirsek, başlangıca en yakın noktadakini seçecek 
borekSiraNo=yiyecekler.index('börek',4)
print(borekSiraNo) #7

#tam aralık belirtme
borekSiraNo=yiyecekler.index('börek',0,4)
print(borekSiraNo) #3

"""
borekSiraNo=yiyecekler.index('börek',4,5)
print(borekSiraNo) #ValueError: 'börek' is not in list hatası döner
çünkü liste[4] değere yani bizler için 5. değer "kek"e bakıyor sadece
"""

"""
append listenin sonuna yeni değer eklememizi sağlar.
Aşağıdaki göreceğimiz insertten farkı budur.
Konum listenin sonudur.
liste.append(element) şeklinde çalışır
element: değişken, değer,liste,vs herhangi bir şey olabilir.
Örnek için ben float sayı eklemeyi göstereceğim.

yiyecekler.append(3.14)
print(yiyecekler)
"""

yiyecekler.append("poğaça")
print(yiyecekler)

"""
append den sonra sıra çok benzeri olan insert'e gelsin o zaman.
istediğimiz konuma ekleyebiliriz. sonra gelen elemenaların konumu 1 adım ötelenir.
liste.insert(index,element)
element:eklemek istediğimiz değer
index: eklemek istediğimiz yer. integer türünde olmak zorundadır

 + Eğer bir nokta belirtmezseniz hata verir ikiside zorunludur.
 + Eğer aralığın dışında bir yeri işaret edersek örneğin listemiz 
 7 indexli ama biz 35. index dersek 8.indexe kayıt yapılır.35.index'i yazdırmaya kalktığınızda IndexError hatasını döndürür.
"""
#yiyecekler.insert(35,"adana")
#print(yiyecekler) #Hata almak icin deneyebilirsiniz

#normal deneme
yiyecekler.insert(3,"dolma")
print(yiyecekler) #3.indise değer atandı 4. indis börek oldu

#Negatif indis girersek
yiyecekler.insert(-2,"adana")
print(yiyecekler) #Hata bekleyebilirsiniz ama vermedi. Sondan 0,1,2. indise değeri atadı.

"""
Tek seferde bir kaç veriyi eklemek için 
extend kullanılıyor.append'den farkı append'de bir veriseti ekleyeceğiniz zaman o verisetini tek bir indiz olarak alıyor.
extend o seriyi dağıtıyor. karşılaştırmalı olarak aşağıya ekleyeceğim.
extend edilince listenin boyu 2 listenin toplamı kadar olurken
append edildiğinde eski liste boyutu+1 olamaktadır.
"""
icecekler.extend(yiyecekler)
yiyecekler.append(icecekler)
print(yiyecekler)
print("++++++++++++++++++")
print("Extend: ",icecekler)
print("Append: ",yiyecekler)
print("++++++++++++++++++")


"""
list.remove(element)
içine atadığınız elementi listeden siler.
eğer 1 taneden fazla varsa ilk değişkeni siler. indis vs almaz
extend edilen özelliği değil ama append edilen özellikleri toplu olarak kaldırma yeteneği vardır.
"""
icecekler.remove('börek')
print("remove: ",icecekler)

"""
list.count(element)
listedeki element değişkenin,n sayısını verir. eğer element değeri belirtilmezse listenin indis sayısını verir.
"""
count1=yiyecekler.count("börek")
print("yiyecekler count börek: ",count1)

count2=icecekler.count("börek")
print("icecekler count börek: ",count2)

"""
list.pop(index) 
belirttiğimiz index numarasındaki değişkeni siler
index numarasını bilmiyorsanız indexof ile değişkene gidebilirsiniz.
"""
yiyecekler.pop(5)
print("yiyecekler 5. indis pop: ",yiyecekler)

icecekler.pop(icecekler.index("fanta"))
print("içecekler pop değeri fanta olan index: ",icecekler)

"""
arama yapmanın basit hali;
değer in list 
değer varsa true yoksa false döndürüyor.
"""
a="kebap" in yiyecekler
print("in sonucu: ",a) #true
b="votka" in icecekler
print("in sonucu: ",b) #false

yiyecekler.remove(icecekler)
print("remove icecekler: ",yiyecekler)
"""
list.reverse()
tüm listeyi tersten yazar. n. indis 0, 0. indis n olur.
"""
icecekler.reverse()
print("reverse: ",icecekler)

"""
list.sort(key=...,reverse=....) sorted alternatifidir.
sıralama işlemini yapar eğer hiçbir şey belirtilmezse küçükten büyüğe sıralama yapar. 
koşul belirtilmesi durumunda koşula göre sıralama yapılır.
"""
icecekler.sort(key=len)
print("Key= takenSecond :",icecekler)
"""
list.copy(): listeyi kopyalamayı sağlar. 
böylelikle yedekli listelerle işlemler yapılabilir.

"""
marketListesi=icecekler.copy()
print("kopya liste: ",marketListesi)


"""
list.clear()
Tüm listeyi temizleminize olanak sağlar.
içine değer almaz.
"""
yiyecekler.clear()
print("Clear: ",yiyecekler)

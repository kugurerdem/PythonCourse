# PythonCourse
Öğrencilerime verdiğim Python kursu ders içeriği.

# İzlence

* [Ön hazırlık](#ön-hazırlık)
* [Merhaba Dünya!](#merhaba-dünya) 
* [1 - Veri tipleri (Data Types): primitif veri tiplerine (Primitive Data Types) giriş.](#1-veri-tipleri-data-types-primitif-veri-tiplerine-primitive-data-types-giriş)
* [2 - Koşullar (Conditions)](#2---koşullar-conditions)
* [3 - Döngüler (Loops)](#3---döngüler-loops)
* 4 - Fonksiyonlar (Functions) 
* 5 - Etki alanı - kapsam (Scoping) 
  * Global değişkenler (Global Variables) 
* 6 - Modüller (Modules), dosyalar (Files) 
* 7 - Referans Veri Tipi (Reference Data Type): Değiştirilebilir (mutable) data tipleri 
  * Diziler (Arrays) ve Çok Boyutlu Diziler (Multi-Dimensional Arrays) 
  * Listeler (Lists) 
  * Sözlükler (Dictionaries) 
* 8 - Yüksek derece fonksiyonlar (Higher-Order Functions) 
* 9 - Sınıflar (Classes) ve Obje Tabanlı Programlama (Object-Oriented Programming) 
* 10 - Numpy, matplotlib, pandas kütüphanelerine giriş 

# Ön hazırlık

### .1 Programlama nedir? 

En yalın haliyle programlamayı, bilgisayar programı geliştirme şeklinde tanımlayabiliriz. Peki program nedir? Program, bilgisayara belirli bir işlemi ya da işlemleri gerçekleştiren şeydir. Şuanda bu yazığı okurken kullandığınız browser bir programdır, oynadığınız oyunlar, tüm bu şeylerin çalıştığı işletim sistemi vs. de bir programdır. Kısacası programı, bilgisayara bir şeyler yaptıran şey şeklinde düşünebiliriz.

### .2 Programlama dili nedir?

Programlama dili, program ve programcı arasındaki arayüz, etkileşim aracı, ya da dil şeklinde düşünülebilir. Programlama dili dediğimiz şey, esasında yine bir makine tarafından anlaşılacak ve başka bir programın yapılmasında kullanılabilecek belirli gramatik kurallar bütününden fazlası değildir. 

Özünde bir programlama dili kendi başına bir programın çalışmasını sağlamaz, bir programın çalışmasını sağlayan şey o programlama dilini anlayan ve bunu makine diline (veya yine anlaşılabilen daha düşük seviyedeki programlama dillerine) çevirebilen başka programların varlığıdır. Bu yüzden her programlama dili için o dili anlayabilecek ayrı programlamlar olan derleyici (Compiler) ve yorumlayıcı (Interpreter) denilen programlara ihtiyaç duyarız.

### .3 Programlama dilleri hiyerarşisi
* <b> Derleyici ve yorumlayıcı farkı </b> <br/>
  
  Derleyici ve yorumlayıcının, belirli programlama dilinde yazılan kodların ve ilgili kodların tekabül ettiği programa çevirilmesinde rol oynayan ayrı programlar olduğundan bahsetmiştik. Peki bu iki program, yani derleyici ve yorumlayıcı arasındaki fark nedir?
  
  bkz: https://www.youtube.com/watch?v=_C5AHaS1mOA
  
* <b> Yüksek ve düşük seviye programlama dilleri </b> <br/>
  
  Derleyiciler ve yorumlayıcılar kendi başlarına bir programdır, dolayısıyla bunlar da uygun olan herhangi bir programlama dilinde yazılabilirler. Bir programlama dilini iyi/kötü kılan çeşitli faktörler vardır. Okunabilirlik, yazılabilirlik, verimlilik (performans), güvenlik vs. akla gelen ilk faktörlerdir. Zaman geçtikçe insanların daha rahat öğrenebileceği, daha rahat yazabileceği ve daha okunabilir programlama dilleri yazılmıştır. Genel olarak bu şekilde, insan diline daha yakın olan programlama dilleri yüksek seviye programlama dili olarak anılır. Makine diline daha yakın olan programlama dillerine ise düşük seviyeli programlama dili denir.
  
  Örnek verilmesi gerekirse Assembly makine diline oldukça yakın bir programlama dili olduğu için düşük seviyeli bir dil olarak görülebilir. C'nin compiler'ı vs. assembly'de yazıldığı ve C insan diline Assembly'e nazaran daha yakın bir dil olduğu için C assembly'e göre daha yüksek seviyede bir dildir ancak yine de Java, C# vs. gibi Object Oriented (Obje Tabanlı) dillere kıyasla daha düşük-temel seviyede bir programlama dilidir. Python genel programlama dilleri arasında değerlendirilecek olursa yüksek seviyedeki programlama dilleri arasında yer alır.
  
### .4 Python
Python yorumlanan (interpreted), yüksek seviye bir scripting dilidir. 

### .5 Kurulum

Başlangıç için kurulumla uğraşmadan doğrudan repl.it üzerinden yazılabilir. <br/>
Çoğu kütüphaneyi birlikte getirdiği ve güzel IDE'lere vs. sahip olduğu için Anaconda paketi ile birlikte indirilebilir (tavsiyem budur). <br/>
Manüel olarak kurmak isteyenler Python'ın kendi sitesinden yükleyebilir. <br/>

# Merhaba Dünya

<b> Konsola! </b>

```python
print( "Merhaba Dünya!")
```

Yukarıdaki kodu çalıştırırsanız konsolda "Merhaba Dünya!" yazdığını görürsünüz. print esasında Python'ın bizim için sağladığı metotlardan birisidir ve parantez içine yazdığımız verileri konsola iletir, bu sayede verilerimizi kontrol edebilir, eğer uygulama konsolda çalışıyor ise kullanıcı ile etkileşime geçebiliriz.
 
 Yukarıda print fonksiyonu içerisine doğrudan Merhaba Dünya yazmadığımızı fark etmişsinizdir. Bunun nedeni python'ın yazdığınız Merhaba ve Dünya kelimelerinin bir değişkene mi hitap ettiğini yoksa yazılması gereken bir şey mi olduğunu ayırt edememesi. Bunu ayırt etmek amacı ile kelime, yazı işlevi gören bilgi string adı verilen bir veri tipinde tutulur. Stringler ise " " veya ' ' işaretleri arasında tanımlanırlar. Örneğin a bir string değilken 'a' a yazısını gösteren bir stringdir. Önemli veri tiplerini ve temel ifadeleri ileriki bölümde inceleyeceğiz.
 
 ```python
print(merhaba) # yanlış
print("merhaba") # konsola merhaba yazdırır
```

<b> Yorumlar (Comments) </b> <br/>
Yukarıdaki kodda print ifadelerinin hemen sonrasında # ile başlayan belli ifadeler var. Bu ifadeler ne anlama geliyor? Bu ifadeler bilgisayar açısından hiçbir anlama gelmiyor. Bilgisayar otomatik olarak satır içerisinde # sonrasında gelen ifadeleri görmezden geliyor. Peki bilgisayar bu ifadeleri görmezden geliyorsa niye böyle bir şey var? Kodumuzu insanlar için daha anlaşılır kılmak için. Başlangıçta anlamsız gözükse de projeleriniz ve kodlarınız karmaşıklaştıkça yorumlar, koddaki niyetlerinizin ve mantığınızın anlaşılmasını çok büyük oranda kolaylaştırır. 

Satırları ard arda olacak şekilde yorumlamak istiyorsanız, # kullanmak yerine """ da kullanabilirsiniz.

 ```python
# bu bir single-line comment

"""
bu ise multi-line comment
bu tirnak isaretleri arasında oldugu sürece istedigimiz kadar yorum yapabiliriz
"""
```
 
# 1-Veri tipleri (Data Types): primitif veri tiplerine (Primitive Data Types) giriş.

Hem hayatımızda hem de programlamada bir sürü faklı türde bilgi mevcuttur. Bu farklı türdeki bilgileri, yapısı bakımından karakterize etmemiz iletişimde kolaylık sağlar. Örneğin gazete okurken sayfalar içerdikleri verinin yani bilginin türüne göre sınıflandırılır, bazı bilgiler finansal bilgi olarak sayılırken bazıları magazin bilgisi şeklinde tanımlanabilir. Benzer bir ayrım programlamada da vardır ve uğraştığımız bilginin türüne göre farklı veri tiplerini kullanırız. Örneğin yazı bilgisi içeren verileri ifade etmeye çalışırken string denilen bir veri tipini kullanırız, sayısal verileri ifade etmek için integer, veya float denilen veri tiplerini kullanırız. Uzun lafın kısası, farklı veri tiplerinin varlığı uğraştığımız verinin doğasına göre bize kolaylık sağlar.

Python'da veri tiplerini basitçe iki ayrı sınıfa ayırabiliriz: Değiştirilebilir (Mutable) ve Değiştirilemez (Immutable) veriler. Temel olarak, immutable verileri, üzerinde değişiklik yapamayacağımız kendi başına temel-primitif değerler olan veri tipleri şeklinde düşünebiliriz, mutable verileri ise üstünde değişiklik yapabildiğimiz, kendi değerini değiştirebildiğimiz veriler olarak düşünebiliriz.

Bu şimdilik bir şey ifade etmeyebilir, ancak mutable objeleri gördüğümüzde her şey daha açık bir hale gelecek.

Şimdilik immutable data tipinde olan, temel verileri inceleyelim. 

#### String
Bu veri tipi yazı türünden bilgileri ifade etmede kullanılır. İki tırnak işareti " arasında yazılarak ifade edilir. Python'da "merhaba" yazdığınızda Python'ın bu ifadeyi merhaba yazısı şeklinde algılıyor gibi düşünebiliriz. Öte yandan merhaba yazacak olsaydık Python bu isimde bir değişken arayıp (bunun ne olduğunu açıklayacağız) eğer tanımlanmamışsa hata verirdi.

#### Number
Bu veri tipi sayıları ifade etmek için kullanılıyor. Ondalıklı sayıları 2.3434 şeklinde ifade edebileceğimiz gibi tam sayıları da 5, -4 vs. şeklinde ifade edebiliriz.

#### Boolean
Bu veri tipi yalnızca iki değerden oluşuyor: True ve False. Özünde bu veri tipi lisede mantık dersinde gördüğünüz önermesel mantıktaki 0 ve 1, doğru ve yanlış ifadelerine denktir. Boolean verilerinin amacı belirli koşulları kontrol etmemizi sağlaması, koşullu işlemlerde kolaylık sağlamasıdır.

## Veriler ile yapabileceğimiz işlemler
Nasıl ki sayılarda işlem yapabiliyorsak (ki bunu da işleyeceğiz), yukarıda saydığım (ve saymadığım) veri tiplerinin de kendilerine ait işlemleri vardır. Number veri tipindeki verilerdeki işlemler esasında bildiğimiz aritmetik işlemlere tekabül ettiğinden bunlar anlaşılması en kolay olan işlemlerdir ancak String ve Boolean veri tiplerinin de kendilerine has işlemleri vardır. 

 ```python
# arithmetic expressions
print( 3 + 5) # 8
print( 3 - 2) # 1
print( 5 * 2) # 10
print( 5 ** 2) # 5^2 -> 25
print( 10 % 3) # 5 mod 3 -> 2
print( 5 / 2 ) # 5 / 2 -> 2.5
print( 5 // 2) # 5 // 2 = 2

# string expressions
print( "asd") # asd
print("asd" + "dsa") # "asddsa"
print("asd" * 5) # "asdasdasdasdasd"

# boolean expression
print( True) # True
print( False) # False

```
Sayıların aritmetiği olduğu gibi, boolean'ların da kendine has bir aritmetiği, operatörleri vardır (ve, veya, ya da, eşittir operatörleri gibi) boolean arithmetiği denilen bu aritmetiği ileride göreceğiz.

## Değişkenler

Normalde çoğu işi yaparken bir çeşit hafızaya ihtiyaç duyarız. Örneğin içinde olduğumuz yılı sorduğunuzda hafızama dayanır, 2020 (şuan bunu yazdığım tarih) verisine ulaşır ve bunu size yanıt olarak söylerim. Benzer bir hafıza sistemine programlamada da ihtiyaç duyarız, değişken dediğimiz şey de tam olarak bu işe yarar.

Değişkenler bir nevi bilgilerimizi içine koyabildiğimiz kutular gibi işler. Bu kutunun içine istediğiniz veriyi koyabilir, istediğiniz zaman kutunun içindeki içeriği çıkarıp yerine başka şeyler koyabilir ya da kutunun içindeki verinin türüne göre (eğer mutable ise) verinin kendisini değiştirebilirsiniz. 

 ```python
a = 5 # a diye bir değişken tanımladık ve değişkenin (kutunun) içine 5 verisi koyduk
print( a) # a yazdığımızda kutunun içindeki veriyi çekiyoruz, print fonksiyonun içine a'nın içindeki değeri 5'i koymuş olduk
a = 7 # a kutusunun icindeki verinin yani 5'in yerine 7 değerini koyduk.
print( a) # 7
```

<b> Önemli not </b>

Değişken tanımlarken kullandığımız = ifadesi, fark ettiğiniz üzere matematikte kullandığımız = ifadesinden farklı bir şekilde işliyor. Yukarıda önce a = 5 deyip hemen ardından a = 7 dedik, burada kafası karışan okuyucu "5 = 7 değil ki?" türünden bir tepki verebilir ancak Python'da (ve neredeyse diğer tüm programlama dillerinde) = ifadesi bir şeyin eşit olduğunu söylemekten ziyade bir şeyin değerini (soldaki değişkenin) güncellemek için kullanılır. Bu sayede yukarıdaki gibi ifadeler kurabiliyoruz. Hatta ifadenin değerini kendisine bağlı olacak şekilde de güncelleyebiliriz. Bu, özellikle bir şeyleri saymamız gerektiğinde çok işe yarayacak.

 ```python
yas = 16 
print( yas) 
yas = yas + 1
print( yas)
```

Değişkenlerin bir diğer artısı ise kendisini çok fazla tekrar eden, ya da bir sürü yerde kullanılan verileri değiştirmemiz gerektiğinde bu değiştirme işlemini inanılmaz ölçüde kolaylaştırabilmesidir. 

Diyelim ki bir işlem yapıyorsunuz ve yaptığınız işlemde PI sayısını 3 olarak kabul ederek bir sürü farklı hesap yapıyorsunuz.

 ```python
# yaricapi 4 olan cember icin cevre ve alan hesapları
print( 2 * 3 * 4) # cevre
print( 3 * 4 * 4) # alan

# yaricapi 7 olan cember icin cevre ve alan hesapları
print( 2 * 3 * 7) # cevre
print( 3 * 7 * 7) # alan
```

şimdi de diyelim ki PI'yi 3 almaktan memnun değilsiniz ve daha net bir cevap istiyorsunuz, bu nedenden dolayı da pi'yi 3.14 olacak şekilde değiştirmek istiyorsunuz. Bu durumda yukarıdaki her 3 sayısını teker teker 3.14 ile değiştirmeniz gerekirdi. Başta bu kısa ve kolay gözükse de kodunuz uzadıkça ve işlem sayınız arttıkça 3'leri takip etmek gittikçe zorlaşacaktır. Bunun yerine en başından PI'yi belirtecek bir değişken oluştursak ve 3 yerine PI değişkenini kullansak kodda değişiklik yapmamız çok daha kolay olurdu.

 ```python
PI = 3
# yaricapi 4 olan cember icin cevre ve alan hesapları
print( 2 * PI * 4) # cevre
print( PI * 4 * 4) # alan

# yaricapi 7 olan cember icin cevre ve alan hesapları
print( 2 * PI * 7) # cevre
print( PI * 7 * 7) # alan
```

kod yazarken sabit değerler kullanmaktan olabildiğince kaçınmak, modülarite ve kodun esnekliği (güzelliği) açısından oldukça önemlidir. Yukarıdaki kodda PI değerini değiştirmek istediğimizde rahatlıkla değişkenin kendisini değiştirip kodun diğer kısmı ile uğraşmaktan kurtulabilirdik.

# 2 - Koşullar (Conditions)

Hayatta çoğu zaman koşullara göre hareket ederiz, belli durumlarda belli kararlar alır ve onları uygularız. Benzer bir şeye programlamada da ihtiyaç duyarız. En basitinden basit bir siteye giriş sırasında dahi yaşımıza göre siteye girip giremeyeceğimiz belirlenebilir. 

Bilgisayar biliminde bu işi gören ifadelere koşullu (conditional) ifadeler diyoruz. Koşulların kendisi ise birçok şeye bağlı olabilir, esasında her bir koşul, önermelerde olduğu gibi "doğru" veya "yanlış" değerine sahiptir. Örneğin siteye "18 yaşından büyüğüm" ya da başka bir değişle "benim yaşım > 18" ifadesi doğru ise girerim. Burada "benim yaşım > 18" ifadesinin değeri doğrudur, yani aslında "benim yaşım > 18" ifadesi bir boolean değerine sahiptir ve o değer de Doğru'dur. Benzer bir şekilde bazen koşulumuzun kendisi birden fazla koşula bağlı olabilir, bazen bu koşulların birbirine göreli olarak doğru veya yanlış olmasına göre hareket etmek isteyebiliriz, işte bu tür durumların altından kalkmamızı sağlayan şeye boole aritmetiği denir. 

## Boole Aritmetiği

Boole aritmetiği esasında lisede öğrendiğimiz mantıksal operatörler ile yaptığımız işlemlerden oluşur. Bunlar "ve, veya, ancak ve ancak, ya da" gibi operatörler ile yapılan işlemlerdir.

 ```python
print( True) # True
print( False) # False

# boolean expression
print( True) # True
print( False) # False

print("OR LOGIC TABLE")
print( True or False) # True
print( False or True) # True
print( True or True) # True
print( False or False) # False

print("AND LOGIC TABLE")
print( True and True) # True
print( False and True) # False
print( True and False) # False
print( False and False) # False

print("NOT LOGIC TABLE")
print( not True) # False
print( not False) # True
```

## Karşılaştırma operatörleri

Yukarıda Boolean'lar arasında kullanabileceğimiz ve boolean return'leyen operatörleri görmüştük. Ancak bunlar tek başına programlama yapabilmemiz için yeterli değildir, programlama yaparken çoğu zaman belirli değerleri birbirleri ile kıyaslayıp bu kıyaslamanın doğru değer verip vermediği ile ilgileniriz. Bu nedenle farklı objeler arasındaki ilişkileri incelememizi sağlayan karşılaştırma operatörlerine (comparison operators) ihtiyaç duyarız. Sayılar bazında düşünecek olursak bunlar "küçüktür, eşittir, küçükeşittir vs." gibi operatörlerdir. Ancak herhangi iki obje arasında belirli türden karşılaştırma yapmamızı sağlayan herhangi bir operatör veya fonksiyon da karşılaştırma operatörü olarak değerlendirilebilir. 

 ```python
# comparison operators
print("3 == 5", 3 == 5) # False
print("3 < 5", 3 < 5) # True
print("3 >= 5", 3 >= 5) # False
print("3 != 5", 3 != 5) # True
print("not 3 == 5", not 3 == 5) # True (yukarıdaki ile aynı)
```

Örneğin aşağıdaki kodda == ifadesini "asda" stringleri için kullanabiliyoruz. < ifadesini iki string arasında kullanabiliyoruz, < ifadesi stringler arasında kullanıldığında sayılar arasında kullanıldığından farklı olarak hangi ifadenin alfabetik olarak daha önde olduğunu kıyaslıyor. "ab" < "bb" yazdığımızda esasında " "ab" alfabetik olarak "bb" den daha öncedir" ifadesinin doğruluk değeri neyse onun değerini, yani True'yu alıyoruz.


 ```python
# comparison operators
print("\"asda\" == \"asda\": ", ("asda" == "asda") ) # True
print("\"ab\" < \"bb\":", ("ab" < "bb")) # True
```

## Escape character ve özel karakterler 

Python'da stringlerin " " işaretleri arasında tanımlandığını belirtmiştik. Burada aklınıza şu soru takılabilir, eğer " işaretleri ile string tanımlıyorsak, " işaretinin kendisini içeren bir stringi nasıl yazabiliriz? String içerisinde yazdığımız " nın string açma işareti yerine string içerisindeki bir karakter olduğunu belirtmek için \ işareti kullanılır. \ işareti yalnızca " için değil, özel karakterlerin önünde de kullanılır ve genel olarak escape character olarak anılır. Örneğin stringizin içinde " olmasını istiyorsanız aşağıdaki gibi yapabilirsiniz.

 ```python
print(" \" \" ") # konsolda " " yazar.
```

\ işaretinin kendisini konsola yazdırmak isterseniz \\ yazabilirsiniz.
 ```python
print(" \\ ") # konsolda \ yazar.
```

Onun haricinde en çok kullanılan özel karakterlerden birisi "\n"dir ve bu string'de satır atlandığı anlamına gelir.
 ```python
print("a \n b \n c ") 
# konsolda aşağıdaki çıktı elde edilir
# a
# b
# c
```

## Input alma

Program yazarken kullanıcı ile etkileşime geçmek için kullanıcının girdilerini takip etmemiz gerekir. Bunu konsol üzerinden yapmamızın yollarından birisi de input almaktır. Bunu input() metodu ile yapabiliriz, bu metod kullanıcının konsola bir şey yazmasını bekler ve yazdıktan sonra (Enter'a bastıktan sonra) yazılan şeyi string olarak geri döner. Eğer girilen değer sayı ise input()'tan alınan değerin özellikle integer'a veya float'a çevirilmesi gerekir. Bunu casting fonksiyonlarını kullanarak yapabilirsiniz.

 ```python
PI = 3.14
print(" yaricapi giriniz")
r = int( input() )
print("cevre:", 2 * PI * r) # cevre
print( "alan:", PI * r * r) # alan
```

## if

 ```python
if koşul:
    ifadeler
```
koşulun doğru olduğu durumda if tarafından kapsanan ifadeleri çalıştırır. 

## if else

 ```python
if koşul:
    ifadeler
else:
    ifadeler
```
koşulun doğru olduğu durumda if tarafından kapsanan ifadeleri çalıştırır. Yanlış olduğu durumda else tarafından kapsanan ifadeleri çalıştırır.

## if elif else

koşulun doğru olmadığı durumda ayrı bir koşulu (koşul2) kontrol etmek için kullanılır. 

 ```python
if koşul:
    ifadeler
elif koşul2:
    ifadeler
else:
    ifadeler
```

Eğer koşul doğru değilse ve koşul2 doğru ise elif koşul2 tarafından kapsanan ifadeler çalıştırılır. Eğer koşul2 de yanlışsa else tarafından kapsanan ifadeler çalıştırılır. 

# 3 - Döngüler (Loops)

Programlama yaparken çoğu zaman kendini belirli bir düzene göre tekrarlayan bir takım işleri yapmamız gerekir. Örneğin 10 kere aynı değeri printlemek istersek 10 kere print ifadesini tekrarlayabiliriz, 1'den 10'a kadar olan değerleri konsola çıkartmak istersek teker teker print(1), print(2) vs. şeklinde tüm bu değerleri printleyebiliriz. Ancak fark edileceği yapılması gereken tekrar sayısı arttıkça bu işi manüel olarak yapmamız da bir o kadar zorlaşacak. Ayrıca bir noktadan sonra kendini tekrar eden bu kodlar kodumuzun çirkin gözükmesine neden olacak. İşte tam olarak bu noktada döngü dediğimiz şey devreye giriyor.

Şimdilik döngü yapmamızı sağlayacak iki sentaks var. Bunlardan ilki while loop ikincisi ise for loop olarak geçer.

## while-loop sentaksı

 ```python
while boolean_değeri:
    ifade1
    ifade2
    ...
    ifade_n
```

yukarıdaki ifadede boolean_değeri'nin değeri True olduğu müddetçe while loop'u tarafından kapsanan ifadeler tekrar tekrar çalışmaya devam eder.

## for-loop sentaksı

 ```python
 
 for i in range(iterasyon_sayisi):
     ifade1
     ifade2
     ...
     ifade_n
```

yukarıdaki ifadede i değeri iterasyon_sayisi'na ulaşak şekilde her bir iterasyon sonunda değerini 1 arttırır ve değeri iterasyon_sayisi kısmındaki değere ulaştığında iterasyon durur. 

## Örnek

Aşağıda 1'den 10'a kadar sayan, tam olarak aynı işi yapan while ve for döngülerini görüyoruz. Çoğu durumda while ve for döngüleri dönüşümlü olarak kullanılabilir.

 ```python
count = 0;
limit = 10;
while count < limit:
  print("iteration number: " + str(count) )
  count = count + 1

for i in range(10):
  print(i)
 ```
# 4 - Fonksiyonlar (Functions)

Matematikte fonksiyonlar tanımlı girdilere has çıktı veren objelerdir. Her ne kadar bu işi programlamada yapan şeyler de "fonksiyon" olarak geçse de fonksiyon kavramı genelde daha geniş bir anlamda kullanılır. Matematikte fonksiyonun çıktı veren objeler olduğunu söylemiştik, programlamada çıktı vermeyen ancak yine belli işleri yapan kod parçalarına da fonksiyon denir. Python'da fonksiyonları iki özelliğe göre, 4 farklı şekilde kategorize edebiliriz.

1. Çıktısı olan ve olmayan fonksiyonlar 
2. Girdisi olan ve olmayan fonksiyonlar 

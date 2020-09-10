# PythonCourse
Öğrencilerime verdiğim Python kursu ders içeriği.

# İzlence

* [Ön hazırlık](#ön-hazırlık)
* [Merhaba Dünya!](#merhaba-dünya) 
* 1 - Veri tipleri (Data Types): primitif veri tiplerine (Primitive Data Types) giriş.
* 2 - Koşullar (Conditions)
* 3 - Döngüler (Loops)
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
 
# 1-Veri tipleri (Data Types): primitif veri tiplerine (Primitive Data Types) giriş.



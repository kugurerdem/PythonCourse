# Merhaba Dünya!
print("Merhaba Dunya!")
print('Merhaba Dunya!') 

'''
Coklu yorum yapıyoruz.
Birden fazla satır yorum yazabiliriz.
'''

# 1-Veri tipleri (Data Types): primitif veri tiplerine (Primitive Data Types) giriş.


# Immutable (değiştirilemez) veri tipleri

# Numbers

# arithmetic expressions
print( 3 + 5) # 8
print( 3 - 2) # 1
print( 5 * 2) # 10
print( 5 ** 2) # 5^2 -> 25
print( 10 % 3) # 10 mod 3 -> 1
print( 5 / 2 ) # 5 / 2 -> 2.5
print( 5 // 2) # 5 // 2 = 2 INTEGER DIVISION

# Strings

# string expressions
print( "asd") # asd
print("asd" + "dsa") # "asddsa"
print("asd" + str(3) )  
print("asd" * 5) # "asdasdasdasdasd"

# Booleans

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

# comparison operators
print("3 == 5", 3 == 5) # False
print("3 < 5", 3 < 5) # True
print("3 >= 5", 3 >= 5) # False
print("3 != 5", 3 != 5) # True
print("not 3 == 5", not 3 == 5) # True (yukarıdaki ile aynı)

print("\"asda\" == \"asda\": ", ("asda" == "asda") )
print("\"ab\" < \"bb\":", ("ab" < "bb"))

# Değişkenler
yas = 18
merhaba = "Merhaba dostum, hosgeldin"
buyuk = yas > 18

# yaricapi 4 olan cember icin cevre ve alan hesapları
print( 2 * 3 * 4) # cevre 2*pi*r
print( 3 * 4 * 4) # alan pi * r^2

# yaricapi 7 olan cember icin cevre ve alan hesapları
print( 2 * 3 * 7) # cevre
print( 3 * 7 * 7) # alan

# --------

PI = 3.14
# yaricapi 4 olan cember icin cevre ve alan hesapları
r = 4
print( 2 * PI * r) # cevre
print( PI * r * r) # alan

# yaricapi 7 olan cember icin cevre ve alan hesapları
r = 7
print( 2 * PI * r) # cevre
print( PI * r * r) # alan

# ='in sağında da değişken kullanabiliriz
x = 1
x = x + 1
x = x + 1
print( x) # 3

# question01
print( "question01")
a = 1
b = a
a = a + 1
print( b) 

#question02
print("question02")
a = 1
b = 5
print("a,b: " + str(a) + "," + str(b) ) # 1,5
# bir şey yap ve a,b'nin değerleri değişsin
c = a
a = b
b = c
# a, b's value should swap
print("a,b: " + str(a) + "," + str(b) ) 

#question03: FUN QUESTION
print("question03 HW01")
a = 3
b = 5
print("a,b: " + str(a) + "," + str(b) )

# a, b's value should swap, 3. bir değişken kullanma
a = a + b
b = a - b
a = a - b

print("a,b: " + str(a) + "," + str(b) )
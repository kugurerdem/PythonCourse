# 02 - CONDITIONS

# getting input from console
'''
print(" Enter some input: ")
print( "The user entered " + input() ) 

print("İsminizi girin: ")
name = input()
print("İsminiz: " + name)
'''

print("Yasınızı girin: ")
age = int(input())
print("Yasınız: " + str(age))


'''
if koşul:
  ifadeler

---
if koşul: 
  ifadeler
else:
  ifadeler

---
if koşul:
  ifadeler
elif koşul2:
  ifadeler
else:
  ifadeler
'''

'''
if age > 18: 
  print("Siteye girebilirsiniz")
if age <= 18:
  print("Siteye giremezsiniz")

if age >= 18: 
  print("Siteye girebilirsiniz")
else:
  print("Siteye giremezsiniz")

if age >= 18: 
  print("Siteye girebilirsiniz")
else:
  if age == 17:
    print("Bir sene sonra girebilirsiniz")
  else:
    print("Siteye giremezsiniz")
'''

if age >= 18:
  print("Siteye girebilirsiniz")
elif age == 17:
  print("Bir sene sonra girebilirsiniz")
else:
  print("Siteye giremezsiniz")

# question01
# sayinin 1-10, 10-20, 20-30, 30-40, 40-50 araliklarindan hangisinde olduğunu bulan program
print("Bir sayı girin: ")
num = 13 # int( input())
if 1 <= num < 10:
  print("Sayı [1,10) arasında")
elif 10 <= num < 20:
  print("Sayı [10,20) arasında")
elif 20 <= num < 30:
  print("Sayı [20,30) arasında")
elif 30 <= num < 40:
  print("Sayı [30,40) arasında")
elif 40 <= num <= 50:
  print("Sayı [40,50] arasında")
else:
  print("Sayı verilen değer aralığında değil")

# question02
# Konsoldan 3 tane sayı al, bu sayıların en büyüğünü printle
a = 3
b = 3
c = 3

# a'nın en büyük olduğu durum
if a >= b and a >= c:
  print("En büyük değer", a)
# b'nin en büyük olduğu durum
elif b >= a and b >= c:
  print("En büyük değer", b)
# c'nin en büyük olduğu durum 
else:
  print("En büyük değer", c)
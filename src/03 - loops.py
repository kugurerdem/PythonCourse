# 03 - LOOPS

# while loop
'''
while boolean_değeri:
   ifade1
   ifade2
   ...
   ifade_n
'''

# 0'dan küçük bir sayı girilene kadar girilen sayıyı 2 ile çarpan program
condition = False # Çalışması için True yazın
while condition:
  print("Sayi girin (çıkmak için 0'dan küçük sayı gir)")
  num = int(input())
  if( num < 0):
    condition = False
  else:
    print("2 * girdiğiniz sayı:", 2 * num)

print("While loop")
counter = 0
iteration_number = 10
while counter < iteration_number:
  print("Iteration count", counter + 1, "/", iteration_number)
  counter += 1
  
# for loop

'''
for degisken_ismi in range(iterasyon_sayisi):
  ifade1
  ifade2
  ...
  ifade_n
'''

print("For loop")
iteration_no = 10
# 0,1,2,3,4...,9
for i in range(iteration_no):
  print("Iteration count", i + 1, "/", iteration_number)

print("---")
# 5,6,7,....,9
for i in range(5, 10):
  print(i)

print("---")
for i in range(10, 5, -2):
  print(i)

# question01
# Kullanıcı pozitif olmayan sayı girene kadar input alıp 2'yle çarpan program yaz
print("question01")
num = 50 # int( input("Enter a positive number :"))
while num > 0:
  print(num * 2)
  num = int( input("Enter a positive number"))

print("You entered non-positive number")

# question02
# birden 100'e kadar 5'in katı olan ama 3'ün katı olmayan tüm sayıları yazdır
# eğer sayı hem 5'in hem 3'ün katıysa "WOO" yazdır

for i in range(1,101):
  if i % 5 == 0 and i % 3 != 0:
    print(i)
  elif i % 15 == 0:
    print("WOO")

# question03: Verilen sayıyı bölen sayıları printleyen kod yaz
number = 5 # int( input("Enter a number"))
for i in range(1, number + 1):
  if number % i == 0:
    print( i)
  
# n'den 1'e doğru yazdır
n = 10
for i in range(n):
  print(n - i)
  
# question04: verilen n ve m değerleri için n x m şeklinde bir dikdörtgen çizdir
# örnek: n = 3, m = 4 için:
#
#    XXXX
#    XXXX
#    XXXX

# YOL 1
n = 3
m = 4
for i in range(n):
    for j in range(m):
        print("X", end='')
    print("\n")

# YOL 2 (Python'a has)
line = 'X' * m
for i in range(n):
    print( line)
    
# YOL 3 (Python'a has)
line = ('X' * m) + '\n'
rectangle = line * n # = (('X' * m) + '\n') * n de diyebilirdik
print( rectangle)

# gauss calculation
sum = 0
for i in range(1,11):
  sum = sum + i
print("the sum is: " + str(sum))

# factorial calculation
product = 1
for i in range(2, 11):
  product = product * i
print("the product is: " + str(product))
    
# question05: question04'deki gibi bir dikdörtgen çizdir
# ancak x ve y'nin eşit olduğunu noktalarda X yerine 0 yazsın.
# örnek n = 3, m = 4 için
#    0XXX
#    X0XX
#    XX0X

n = 3
m = 4
for i in range(n):
    for j in range(m):
        if( n == m):
            print("0", end='')
        else:
            print("X", end='')
    print("\n")

# question06: Aldığın bir n sayısı için, n basamaklı aşağıdaki gibi bir ağaç oluştur
'''
x
xx
xxx
xxxx
....
xxxxxx...xxxx (n-tane)
'''

n = int(input("Enter the triangle's height"))
# YOL 1
for i in range(n):
    line = ""
    for j in range(i+1):
        line = line + 'x'
    print( line)
    
# YOL 2
line = ""
for i in range(n)
    line = line + 'x'
    print( line)

# YOL 3 (Python'a has)
for i in range(1, n + 1):
  print(i * "x")
  
  
  
# question07: DNA eşleme
# verilen bir DNA kodunun eşleniğini veren kod
# A ile T, C ile G eşleşmeli.
print("--Q7--")
# YOL 1
DNA = 'ACTAGAAGACTG'
DNA_es = ''

for i in range( len(DNA)):
  char = DNA[i]
  if( char == 'A'):
    DNA_es = DNA_es + 'T'
  elif( char == 'T'):
    DNA_es = DNA_es + 'A'
  elif( char == 'C'):
    DNA_es = DNA_es + 'G'
  elif( char == 'G'):
    DNA_es = DNA_es + 'C'

print("DNA\n", DNA)
print("DNA_es\n", DNA_es)

# YOL 2 (Python'a has)
print("---")
DNA = 'ACTAGAAGACTG'
DNA_es = ''

for char in DNA:
  if( char == 'A'):
    DNA_es = DNA_es + 'T'
  elif( char == 'T'):
    DNA_es = DNA_es + 'A'
  elif( char == 'C'):
    DNA_es = DNA_es + 'G'
  elif( char == 'G'):
    DNA_es = DNA_es + 'C'

print("DNA\n", DNA)
print("DNA_es\n", DNA_es)

# question08: Aşağıdaki ağacı veren kodu yaz
print("--Q8--")
'''
   * - > 1. satır: 3 boşluk 1 yıldız
  *** - > 2. satır: 2 boşluk 3 yıldız
 ***** - > 3. satır: 1 boşluk 5 yıldız
******* - > 4. satır: 0 boşluk 7 yıldız

i. satırdayken: n - i boşluk
              : (i - 1) * 2 + 1
                
'''

# YOL 1
n = 4
for i in range(n):
  # satır yazdırmamız lazım
  for j in range(n - i - 1):
    print(" ", end="")
  for j in range(2 * i + 1):
    print("*", end="")
  print()

# YOL 2 (Berkay'ın kodu) (Python'a has yöntem)
space = n - 1
star = 1
for i in range(n):
  print( " " * space + "*" * star)
  space = space - 1
  star = star + 2
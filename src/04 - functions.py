# Girdisi ve çıktısı da olmayan fonksiyonlar
def print_calculations():
  print("Sayi girin")
  a = int( input())
  print("Sayi girin")
  b = int( input())
  print("a * b", a * b)
  print("a - b", a - b)
  print("a + b", a + b)
  print("a / b", a / b)
    
print_calculations()
print_calculations()

# Girdisi olmayan ve çıktısı olan fonksiyonlar
PI = 3.14
r = 5
def area():
  return PI * r * r
  
area() # konsola bir şey yazdırmaz
print( area() ) # konsola alani yazdirir


# Girdisi olan ve çıktısı olmayan fonksiyonlar
def welcome(name, surname, age):
  print("Hi", name, surname)
  
  if( age >= 18):
    print("Welcome!")
  else:
    print("You cannot enter.")

welcome("berkay","özgün", 21)
welcome("belinay","özgün", 9)

# Girdisi olan ve çıktısı olan fonksiyon
def area(r):
  return PI * r * r

print( area(5) ) 
print( area(10)) 
print( area(15))

# Q01: Stringi ters çeviren fonksiyon
def reverse_string(string):
  reverse_string = ""
  for i in range(len(string)):
    reverse_string = string[i] + reverse_string
  
  return reverse_string

# Q02: Bir stringin palindrom olup olmadığını kontrol eden fonksiyon
def isPalindrome(string):
  return reverse_string( string) == string

print( reverse_string("aba")) 
print( reverse_string(" merhaba")) 

print( isPalindrome("aba")) 
print( isPalindrome(" merhaba")) 

# Q03: Bir sayının bölenlerini yazdıran (printleyen) fonksiyon

# Q04: Bir sayının asal sayı olup olmadığını veren fonksiyon

# Q05: Verilen bir stringin substring'ini veren fonksiyon

# Default parameters

# Function overloading
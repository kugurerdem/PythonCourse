# 02 Pratik

# Menu programi

# 1. Hesap makinesi
# 2. Kelime işleyicisi
# 3. Boolean aritmetiği
# 0. Çıkış

'''
n = int(input("Bir sayı girin: (durdurmak için 0 girin)"))
while n != 0:
  n = int(input("Bir sayı girin: (durdurmak için 0 girin)"))
'''

# Komutların kullanıcıya iletilmesi
print("Bir komut seçin: ")
print("1. Hesap makinesi")
print("2. Kelime işleyicisi")
print("3. Boolean aritmetiği")
print("0. Çıkış")

command = int( input("> "))
while command != 0:
  # Komutu işleyebiliriz
  if( command == 1):
     # ARİTMETİK İŞLEMLER
    n_1 = int(input("İlk tam sayıyı girin: "))
    n_2 = int(input("İkinci tam sayıyı girin: "))

    print("Hangi işlemi yapmak istiyorsunuz?")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    
    sub_command = int(input("> "))
    if sub_command == 1:
      # TOPLAMA
      print(n_1 + n_2)
    elif sub_command == 2:
      # ÇIKARMA
      print(n_1 - n_2)
    elif sub_command == 3:
      # ÇARPMA
      print(n_1 * n_2)
    elif sub_command == 4:
      # BÖLME
      if n_2 != 0:
        print(n_1 / n_2)
      else:
        print("Sayıyı sıfıra bölemezsiniz.")
    else:
      print("Uygun komut girmediniz, ana menüye yönlendiriliyorsunuz")
      
  elif( command == 2):
    # KELİME İŞLEME
    print("Hangi işlemi yapmak istiyorsunuz?")
    print("1. Kelime ters çevirme")
    print("2. Palindrom kontrolü")
    print("3. Ağaç çizdirme")

    sub_command = int(input("> "))

    if( sub_command == 1):
      # Ters çevirme
      string = input("Stringi giriniz: ")

      reversed_string = ""
      for i in range( len(string)):
        reversed_string = string[i] + reversed_string
      
      print( reversed_string )
    elif(sub_command == 2):
      # Palindrom kontrol
      string = input("Stringi giriniz: ")

      reversed_string = ""
      for i in range( len(string)):
        reversed_string = string[i] + reversed_string

      if( reversed_string == string):
        print("Kelime palindrom.")
      else:
        print("Kelime palindrom değil.")

    elif(sub_command == 3):
      # Ağaç çizdirme
      print("Ağacınız kaç satır olsun?")
      line_number = int( input(":"))
      for i in range( line_number):
        print( (line_number - i) * " " + (2 * i + 1) * "*" )  
    else:
      print("Uygun komut girmediniz, ana menüye yönlendiriliyorsunuz")

  elif( command == 3):
    # BOOLEAN ARİTMETİĞİ
    print("Hangi operatörü kullanmak istiyorsunuz?")
    print("1. NOT (Değil)")
    print("2. AND (Ve)")
    print("3. OR (Veya)")
    print("4. XOR (Ya da)")
    print("5. XNOR (Ancak ve Ancak)")

    sub_command = int( input("> "))
    if sub_command != 1 and sub_command != 2 and sub_command != 3 and sub_command != 4 and sub_command != 5:
      print("Uygun komut girmediniz, ana menüye yönlendiriliyorsunuz")
    else:
      print("Boolean değeri girin: ", end="")
      bool_1 = input().lower() == "true"
      if sub_command == 1:
        # NOT OPERATÖRÜ
        print(not bool_1)
      else:
        # 2. değer alan operatörler
        print("Boolean değeri girin: ", end="")
        bool_2 = input().lower() == "true"
        
        if sub_command == 2:
          # AND OPERATÖRÜ
          print(bool_1 and bool_2)

        elif sub_command == 3:
          # OR OPERATÖRÜ
          print(bool_1 or bool_2)
          
        elif sub_command == 4:
          # XOR OPERATÖRÜ
          print( (bool_1 and not bool_2) or (bool_2 and not bool_1))
          
        elif sub_command == 5:
          # XNOR (ancak ve ancak) OPERATÖRÜ
          print(bool_1 == bool_2)
  
  else: 
    print("Komut anlaşılmadı.")
  
  # Komutların kullanıcıya iletilmesi
  print("Bir komut seçin: ")
  print("1. Hesap makinesi")
  print("2. Kelime işleyicisi")
  print("3. Boolean aritmetiği")
  print("0. Çıkış")
  command = int(input("> "))
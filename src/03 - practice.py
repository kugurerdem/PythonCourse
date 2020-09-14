# 02 Pratik

# Menu programi

# 1. Hesap makinesi
# 2. Kelime işleyicisi
# 3. Boolean aritmetiği
# 0. Çıkış

# Komutların kullanıcıya iletilmesi
print("Bir komut seçin: ")
print("1. Hesap makinesi")
print("2. Kelime işleyicisi")
print("3. Boolean aritmetiği")
print("0. Çıkış")

# Kullanıcıdan komutun alınması
command = int( input())

# Kullanıcı çıkışa basmadıkça döngüyü devam ettir
while( command != 0):
    if( command == 1):
      # Hesap makinesi işlemleri
      print("İlk tam sayıyı girin")
      first_number = int( input())
      print("İkinci tam sayıyı girin")
      second_number = int( input())

      print("Hangi işlemi yapmak istiyorsunuz?")
      print("1. Toplama")
      print("2. Çıkarma")
      print("3. Çarpma")
      print("4. Bölme")

      command_2 = int(input())
      if( command_2 == 1):
        print(first_number + second_number)
      elif( command_2 == 2):
        print(first_number - second_number)
      elif( command_2 == 3):
        print(first_number * second_number)
      elif( command_2 == 4):
        print(first_number / second_number)
      else:
        print("Uygun komut girmediniz!")

    elif( command == 2):
      # String işlemleri
      print("a")
    
    elif( command == 3):
      # Boolean aritmetiği işlemleri
      print("b")

    else:
      # Bilinmeyen bir kod girilmiş.
      print("Bu komut tanımlı değil. Lütfen aşağıdaki komutlardan birisini çalıştırın.")
        
    # Her şeyi yaptıktan sonra tekrar komut alıyoruz.
    # Komutların kullanıcıya iletilmesi
    print("Bir komut seçin: ")
    print("1. Hesap makinesi")
    print("2. Kelime işleyicisi")
    print("3. Boolean aritmetiği")
    print("0. Çıkış")

    # Kullanıcıdan komutun alınması
    command = int( input())
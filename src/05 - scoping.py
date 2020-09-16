a = 3 # global variable

def foo():
    a = 4 # local variable
   
foo()
print(a) # 3

# ----

b = 5

def foo2():
    global b
    b = 4

foo2()
print( b) # -> 4

# ----

# Python'da scoping dynamic bir şekilde işler, static bir şekilde değil.
a = 3

def foo4():
    print(a)

def foo3():
    a = 5
    foo4()
    
foo3()
    
# ----

for i in range(3):
    c = 3
    print(a)
    print(i)

print(i) # -> 3
# print(c) this causes an error

# Aynı durum herhangi bir scoping (kapsama/etki alanı) için geçerli. IF, WHİLE vs. de buna dahil

# ----
# Fonksiyonlar içinde fonksiyon da tanımlayabiliriz. İçeride tanımlanan fonksiyon dışarıda kullanamaz.

def func_1():
    def func_2():
        print("hi")
    
    func_2()

func_1() # "hi"
# func_2() # -> hata verir
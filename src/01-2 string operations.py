# length
name = "ugur"
print("İsim uzunluğu ", len( name)) # -> 4

# character-at
print("1. karakter ", name[0]) # -> u
print("Son karakter ", name[len(name) - 1]) # -> r

# splicing

kelime = "merhaba"
# string[start : end]
print( kelime[3 : 6] ) # -> "hab"

# string[start : end : inc]
print( kelime[0: len(kelime): 2]) # mraa
print( kelime[::2]) # mraa

print( kelime[::-1])  # abahrem

# LOWER & UPPER
print( "ASDAD".lower() ) # asdad
print( "asdad".upper() ) # ASDAD
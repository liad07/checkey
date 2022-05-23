from random import choice

digits='0123456789'
chars='abcdefghijklmn' \
      'opqrstuvwxyz'
up=chars.upper()
speical='!@#$%^&*_'
all=digits+chars+up+speical

f = open("license.txt", "a")
for i in range (0,250):
    password = ''.join(choice(all) for j in range(16))
    f.write(password+"\n")

f.close()


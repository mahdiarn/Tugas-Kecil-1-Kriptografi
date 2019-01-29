f = open("a.png", "rb")
plain = f.read()
print(type(plain))
cipher = bytearray(plain)
cipher[0] = 255
print(cipher[0])
print(len(cipher))
print(type(cipher))
if (type(cipher) is bytearray) :
    print("yo")
else :
    print("ya")

print(plain)
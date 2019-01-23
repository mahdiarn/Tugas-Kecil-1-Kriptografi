def stdVigenere(plain,key):
    cipher = ""
    for idx,val in enumerate(plain):
        if (val.istitle()):
            cipher = cipher + chr((((ord(plain[idx])-65) + (ord(key[idx].upper())-65)) % 26) + 65)
        elif (val.isdigit()):
            cipher = cipher + val
        elif (val == " "):
            cipher = cipher + val
        else:
            cipher = cipher + chr((((ord(plain[idx])-97) + (ord(key[idx])-97)) % 26) + 97)
    return cipher

if __name__=="__main__":
    print("Masukkan jenis input:")
    print("1. Dari Keyboard")
    print("2. Dari File")
    choice = int(input())

    if (choice == 1) :
        plain = input("Masukkan plainteks: ")        
        print("Plainteks:",plain)
    else :
        filename = input("Masukkan nama file:")
        f = open(filename, "rb")
        plain = f.read()
        for a in plain:            
            print(format(a, '02x'))
        # print(plain)

    print("Masukkan jenis enkripsi:")
    print("1. Vigenere Cipher Standar")
    choice = int(input())
    if (choice == 1):
        rawKey = input("Masukkan kata kunci: ")
        usableKey = ""
        if (len(rawKey) == len(plain)):
            usableKey = rawKey        
        elif (len(rawKey) < len(plain)):
            counter = 0
            while (len(usableKey) != len(plain)):
                usableKey += rawKey[counter]
                counter = (counter + 1) % len(rawKey)
        else :
            usableKey = rawKey[:len(plain)]
        print("Hasil enkripsi:",stdVigenere(plain,usableKey))
    else :
        print("Bye!")

import os

def stdVigenere(inputan,key,mode):
    if(mode == 1):
        cipher = ""
        for idx,val in enumerate(inputan):
            if (val.istitle()):
                cipher = cipher + chr((((ord(inputan[idx])-65) + (ord(key[idx].upper())-65)) % 26) + 65)
            elif (val.isdigit()):
                cipher = cipher + val
            elif (val == " "):
                cipher = cipher + val
            else:
                cipher = cipher + chr((((ord(inputan[idx])-97) + (ord(key[idx])-97)) % 26) + 97)
        return cipher
    elif(mode == 2):
        plain = ""
        for idx,val in enumerate(inputan):
            if (val.istitle()):
                plain = plain + chr((((ord(inputan[idx])-65) - (ord(key[idx].upper())-65)) % 26) + 65)
            elif (val.isdigit()):
                plain = plain + val
            elif (val == " "):
                plain = plain + val
            else:
                plain = plain + chr((((ord(inputan[idx])-97) - (ord(key[idx])-97)) % 26) + 97)
        return plain
    else:
        return 0

def stdVigenereBytes(inputan,key,mode):
    if(mode==1):
        cipher = inputan
        for i in range(len(cipher)):
            if (cipher[i] <= 90 and cipher[i] >= 65):
                cipher[i] = (((cipher[i]-65) + (ord(key[i].upper())-65)) % 26) + 65
            elif (cipher[i] <= 122 and cipher[i] >= 97):
                cipher[i] = (((cipher[i]-97) + (ord(key[i])-97)) % 26) + 97
        return cipher
    elif(mode==2):
        plain = inputan
        for i in range(len(plain)):
            if (plain[i] <= 90 and plain[i] >= 65):
                plain[i] = (((plain[i]-65) - (ord(key[i].upper())-65)) % 26) + 65
            elif (plain[i] <= 122 and plain[i] >= 97):
                plain[i] = (((plain[i]-97) - (ord(key[i])-97)) % 26) + 97
        return plain
    else:
        return 0
    

if __name__=="__main__":
    print("Tentukan mode:")
    print("1. Enkripsi")
    print("2. Dekripsi")
    mode = int(input())
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
        filebyte = f.read()
        plain = bytearray(filebyte)
        
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
        if(mode==1):
            print("Hasil enkripsi:")
        else:
            print("Hasil dekripsi:")
        if (type(plain) is bytearray) :
            if(mode==1):
                with open(filename + ".enc", 'wb') as fo:
                    fo.write(stdVigenereBytes(plain,usableKey,mode))
                os.remove(filename)
            elif(mode==2):
                with open(filename[:-4], 'wb') as fo:
                    fo.write(stdVigenereBytes(plain,usableKey,mode))
                os.remove(filename)
        else:
            print(stdVigenere(plain,usableKey,mode))
    else :
        print("Bye!")

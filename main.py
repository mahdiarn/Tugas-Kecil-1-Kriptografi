import os
import random

def saveTable(table):
    f = open("tabel","w")
    for i in table:
        for j in i:
            f.write(str(j)+"\n")

def generateRepeatedKey(input,plainLen):
    if (len(input) == plainLen):
        return input        
    elif (len(input) < plainLen):
        output = ""
        counter = 0
        while (len(output) != plainLen):
            output += input[counter]
            counter = (counter + 1) % len(input)
        return output
    else :
        return input[:plainLen]

def generateFullKeyTable():
    table = []
    for i in range(26):
        listPerKey = []
        for j in range(26):
            listPerKey.append(chr(j + 97))
        swappedIndex = []
        while (len(swappedIndex) != len(listPerKey)):
            swapFirst = random.randint(0,25)
            swapSecond = random.randint(0,25)
            while ((swapFirst in swappedIndex) or (swapSecond in swappedIndex)):
                swapFirst = random.randint(0,25)
                swapSecond = random.randint(0,25)
            swappedIndex.append(swapFirst)
            if (swapFirst != swapSecond):
                swappedIndex.append(swapSecond)
            temp = listPerKey[swapFirst]
            listPerKey[swapFirst] = listPerKey[swapSecond]
            listPerKey[swapSecond] = temp
        table.append(listPerKey)
    return table

def generateAutoKey(input,key):
    if (len(key) == len(input)):
        return key
    elif (len(key) > len(input)):
        output = ""
        idx = 0
        while (len(output) != len(input)):
            output = output + key[idx]
            idx += 1
        return output
    else:
        output = key
        idx = 0
        while (len(output) != len(input)):
            output = output + input[idx]
            idx += 1
        return output

def generateRunningKey(input,filename):
    file = open(filename,"r")
    fileString = file.read()
    output = ""
    idx = 0
    while (len(output) != len(input)):
        output = output + fileString[idx]
        idx += 1
    return output

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
                cipher = cipher + chr((((ord(inputan[idx])-97) + (ord(key[idx].lower())-97)) % 26) + 97)
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
                plain = plain + chr((((ord(inputan[idx])-97) - (ord(key[idx].lower())-97)) % 26) + 97)
        return plain
    else:
        return 0

def vigenereAscii(inputan,key,mode):
    if(mode == 1):
        cipher = ""
        for idx,val in enumerate(inputan):
                cipher = cipher + chr(((ord(inputan[idx])) + (ord(key[idx]))) % 256)
        return cipher
    elif(mode == 2):
        plain = ""
        for idx,val in enumerate(inputan):
                plain = plain + chr(((ord(inputan[idx])) - (ord(key[idx]))) % 256)
        return plain
    else:
        return 0

def fullVigenere(inputan,key,mode):    
    if(mode == 1):
        table = generateFullKeyTable()
        cipher = ""
        for idx,val in enumerate(inputan):
            if (val.istitle()):
                cipher = cipher + table[(ord(key[idx].upper())-65)][(ord(inputan[idx])-65)]
            elif (val.isdigit()):
                cipher = cipher + val
            elif (val == " "):
                cipher = cipher + val
            else:
                cipher = cipher + table[(ord(key[idx].lower())-97)][(ord(inputan[idx])-97)]
        saveTable(table)
        return cipher
    elif(mode == 2):
        fileTableName = input('Masukkan nama file tabel pergeseran hurufnya : ')
        fileTable = open(fileTableName,"r")
        for fileTableLength,fileTableContent in enumerate(fileTable):
            pass
        fileTableLength += 1
        if (fileTableLength != 676):
            print("Tabel tidak berukuran 676 baris, tetapi berukuran ", fileTableLength)
        else:
            fileTable = open(fileTableName,"r")
            table = []
            for i in range(26):
                elementTable = []
                for j in range(26):
                    if (i==25 and j==25):
                        elementTable.append(fileTable.readline())
                    else:
                        a = fileTable.readline()[:-1]
                        elementTable.append(a)
                table.append(elementTable)
        plain = ""
        for idx,val in enumerate(inputan):
            if (val.istitle()):
                plain = plain + table[(ord(key[idx].upper())-65)][(ord(inputan[idx])-65)]
            elif (val.isdigit()):
                plain = plain + val
            elif (val == " "):
                plain = plain + val
            else:
                plain = plain + table[(ord(key[idx].lower())-97)][(ord(inputan[idx])-97)]
        return plain
    else:
        return 0

def vigenereAsciiForBytes(inputan,key,mode):
    if(mode==1):
        cipher = inputan
        for i in range(len(cipher)):
            cipher[i] = ((cipher[i] + ord(key[i])) % 256)
        return cipher
    elif(mode==2):
        plain = inputan
        for i in range(len(plain)):
            plain[i] = ((plain[i] - ord(key[i])) % 256)
        return plain
    else:
        return 0

def tanpaSpasi(masukan):
    output = ""
    idx = 0
    while (idx != len(masukan)):
        if(masukan[idx] != " "):
            output = output + masukan[idx]
        idx += 1    
    return output

def perLimaHuruf(masukan):
    raw = ""
    idx = 0
    while (idx != len(masukan)):
        if(masukan[idx] != " "):
            raw = raw + masukan[idx]
        idx += 1
    output = ""
    idx = 0
    count = 0
    while (idx != len(raw)):
        if(raw[idx] != " "):
            output = output + raw[idx]
        idx += 1
        if(count == 4):
            output += " "
        count += 1
        count = count % 5
    return output


def penyajianOutput(masukan,mode):
    print("Pilih metode penampilan :")
    print("1. Apa adanya")
    print("2. Tanpa spasi")
    print("3. Per 5 Huruf")
    pilihanMetode = int(input())
    hasil = masukan
    if (pilihanMetode == 1):
        hasil = masukan
    elif (pilihanMetode == 2):
        hasil = tanpaSpasi(masukan)
    elif (pilihanMetode == 3):
        hasil = perLimaHuruf(masukan)
    if(mode == 1):
        print("Hasil enkripsi: ")    
    else:
        print("Hasil dekripsi: ")    
    print(hasil)
    if(mode == 1):
        print("Simpan file cipherteks?")
        print("1. Ya")
        print("2. Tidak")
        isSaveCipher = int(input())
        if (isSaveCipher == 1):
            filename = input("Masukkan nama file")
            file = open(filename,"w")
            file.write(masukan)
            file.close()
    return 0

if __name__=="__main__":
    print("Tentukan mode:")
    print("1. Enkripsi")
    print("2. Dekripsi")
    mode = int(input())
    print("Masukkan jenis algoritma enkripsi:")
    print("1. Standard Vigenere (26 karakter)")
    print("2. Full Vigenere (26 karakter)")
    print("3. Standard Vigenere variasi auto key (26 karakter)")
    print("4. Standard Vigenere varuasi running key (26 karakter)")
    print("5. Vigenere 256 bit")
    print("6. Playfair Cipher")
    algorithm = int(input())
    print("Masukkan jenis input:")
    print("1. Dari Keyboard")
    print("2. Dari File")
    choice = int(input())

    if (choice == 1) :
        if (mode == 1):
            masukan = input("Masukkan plainteks: ")        
            print("Plainteks:",masukan)
        elif(mode == 2):
            masukan = input("Masukkan cipherteks: ")        
            print("Cipherteks:",masukan)
    else :
        if (algorithm == 5):
            filename = input("Masukkan nama file:")
            f = open(filename, "rb")
            filebyte = f.read()
            masukan = bytearray(filebyte)
        else:
            filename = input("Masukkan nama file:")
            f = open(filename, "r")
            masukan = f.read()            

    if (algorithm == 1):
        rawKey = input("Masukkan kata kunci: ")
        usableKey = generateRepeatedKey(rawKey,len(masukan))        
        penyajianOutput(stdVigenere(masukan,usableKey,mode),mode)        
    elif (algorithm == 2):
        rawKey = input("Masukkan kata kunci: ")
        usableKey = generateRepeatedKey(rawKey,len(masukan))        
        penyajianOutput(fullVigenere(masukan,usableKey,mode),mode)      
    elif (algorithm == 3):
        rawKey = input("Masukkan kata kunci: ")
        usableKey = generateAutoKey(masukan,rawKey)
        print("Kunci setelah digenerate: ", usableKey)
        penyajianOutput(stdVigenere(masukan,usableKey,mode),mode)  
    elif (algorithm == 4):
        fileKeyName = input("Masukkan nama file key: ")
        usableKey = generateRunningKey(masukan,fileKeyName)
        print("Kunci setelah digenerate: ", usableKey)
        penyajianOutput(stdVigenere(masukan,usableKey,mode),mode)  
    elif (algorithm == 5):
        rawKey = input("Masukkan kata kunci: ")
        usableKey = generateRepeatedKey(rawKey,len(masukan))        
        if (type(masukan) is bytearray) :
            if(mode==1):
                with open(filename + ".enc", 'wb') as fo:
                    fo.write(vigenereAsciiForBytes(masukan,usableKey,mode))
                os.remove(filename)
                print("File berhasil dienkripsi")
            elif(mode==2):
                with open(filename[:-4], 'wb') as fo:
                    fo.write(vigenereAsciiForBytes(masukan,usableKey,mode))
                os.remove(filename)
                print("File berhasil didekripsi")
        else:
            penyajianOutput(vigenereAscii(masukan,usableKey,mode),mode)  
    else :
        print("Bye!")

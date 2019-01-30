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
        print(listPerKey)
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

def stdVigenereForBytes(inputan,key,mode):
    if(mode==1):
        cipher = inputan
        for i in range(len(cipher)):
            cipher[i] = ((cipher[i] + ord(key[i])) % 256)
    elif(mode==2):
        plain = inputan
        for i in range(len(plain)):
            plain[i] = ((plain[i] - ord(key[i])) % 256)
        return plain
    else:
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
    print("4. Standard Vigenere varuasu running key (26 karakter)")
    algorithm = int(input())
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

    if (algorithm == 1):
        rawKey = input("Masukkan kata kunci: ")
        usableKey = generateRepeatedKey(rawKey,len(plain))        
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
    elif (algorithm == 2):
        rawKey = input("Masukkan kata kunci: ")
        usableKey = generateRepeatedKey(rawKey,len(plain))        
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
            print(fullVigenere(plain,usableKey,mode))
    else :
        print("Bye!")

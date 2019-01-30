import random

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
    
    
penyajianOutput("Mahdiar Naufal")
# 4 işlem hesap makşinesi

sayi1 = float(input("1. sayıyı: "))
islem = input("Toplama için (+) Çıkarma için (-) Çarpım(*) Bölme(/) girin:  ")
sayi2 = float(input("2. sayıyı: "))

if islem == "+" or islem == "-" or islem == "*" or islem == "/":
    if islem == "+":
        sonuc = sayi1 + sayi2
        print("Toplamı:",sonuc)
    elif islem == "-":
        sonuc = sayi1 - sayi2
        print("Farkı:",sonuc)
    elif islem == "*":
        sonuc = sayi1 * sayi2
        print("Çarpım",sonuc)
    elif islem == "/":
        sonuc = sayi1 / sayi2
        print("Bölüm",sonuc)
    sonuc= round(sonuc,2)
    print(sayi1 , islem , sayi2 ,"=", sonuc)
else:
    print("Hatalı işlem")




#Vize-final-Ortalama hesabı

vize = float(input("Vize notunuzu giriniz: "))
final = float(input("Final notunuzu giriniz: "))
ortalama = round((vize * 0.4) + (final * 0.6),2)
if(ortalama >=80):
    print("Harf Notu: AA")
elif(ortalama>=70):
    print("Harf Notu: BB")
elif(ortalama>=60):
    print("Harf Notu: CC")
elif(ortalama>=50):
    print("Harf Notu: DD")
elif(ortalama<=49):
    print("Harf Notu: FF")
x = f"Ortalama : {ortalama}"
print(x)


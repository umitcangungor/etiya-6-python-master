#Fibonacci Foksiyonu

def Fibo():
    list = [] 
    a = 1
    b = 0
    c = 0
    while len(list)<20: 
        c = a+b
        a = b
        b = c
        list.append(b) 
    print(list)

Fibo();

#Mükemmel Sayı fonksiyonu

def perfect():
    sayi = int(input("Bir Sayı Giriniz:"))
    toplam=0
    for i in range(1,sayi): 
        if(sayi%i == 0): 
            toplam +=i 
            
    if(sayi == toplam): 
        print(sayi,"-> Mükemmel Sayıdır.") 
    else:
        print(sayi,"-> Mükemmel Sayı Degildir")

perfect();


#En büyük fonksiyonu
def Enbüyük():
    nums = []
    for i in range(10):
        num = int(input("Sayı girin:"))
        nums.append(num)
    enBuyuk = max(nums)
    x = f"En büyük değer: {enBuyuk}"
    print(x)

Enbüyük();

#Alt-Üst limit belirleme

def AltUst():
    a = int(input("Alt limit giriniz?"))
    u = int(input("Üst limit giriniz?"))
    S = []
    for cıftSayi in range(a, u):
        if cıftSayi > 0 and cıftSayi%2 == 0:
            S.append(cıftSayi)
        
    print(S)  

AltUst();


 
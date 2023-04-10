def sayıAl():
    x = int(input("1.sayıyı girin"))
    y = int(input("2.sayıyı girin"))
    return x,y
def toplama(x,y):
    return x + y
def cıkarma(x,y):
    return x - y
def carpma(x,y):
    return x * y
def bolme(x,y):
    return x / y 
def mod(x,y):
    return x % y  

def hesapMak():  
    while True:

        secim = input("+ - / * % ,işlemlerinden birini girin, çıkış için q'ya basın ")
        if secim == "q":
            print("Çıkış yapıyoruz...")
            break
        elif secim == "+":
            sayi1,sayi2 = sayıAl()
            print(sayi1,"+",sayi2,"=", toplama(sayi1,sayi2))
        elif secim == "-":
            sayi1,sayi2 = sayıAl()
            print(sayi1,"-",sayi2,"=", cıkarma(sayi1,sayi2))
        elif secim == "*":
            sayi1,sayi2 = sayıAl()
            print(sayi1,"*",sayi2,"=", carpma(sayi1,sayi2))
        elif secim == "/":
            sayi1,sayi2 = sayıAl()
            print(sayi1,"/",sayi2,"=", bolme(sayi1,sayi2))
        elif secim == "%":
            sayi1,sayi2 = sayıAl()
            print(sayi1,"%",sayi2,"=", mod(sayi1,sayi2))  
        else:
            print("Başka işlem girin") 

hesapMak()
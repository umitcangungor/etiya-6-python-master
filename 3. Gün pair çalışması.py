# İlk iki elemanı 1'e eşit olan, en az 20 elemanlı bir fibonacci serisini liste halinde oluşturun. Örnek: [ 1, 1, 2, 3, 5, 8, 13, 21, 34..... ]
# Fibonacci Serisi : Serideki her bir sayı kendisinden önceki iki sayının toplamına eşittir.


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



#  Bir sayının kendi hariç tüm bölenlerinin toplamı eğer kendisine eşitse bu Mükemmel Sayıdır. Örnek: 1 + 2 + 3 = 6
# Kullanıcıdan aldığı sayıyının mükemmel olup olmadığını söyleyen bir program yazın. 

sayi = int(input("Bir Sayı Giriniz:"))
toplam=0
for i in range(1,sayi): 
    if(sayi%i == 0): 
        toplam +=i 
        
if(sayi == toplam): 
    print(sayi,"-> Mükemmel Sayıdır.") 
else:
    print(sayi,"-> Mükemmel Sayı Degildir")
 


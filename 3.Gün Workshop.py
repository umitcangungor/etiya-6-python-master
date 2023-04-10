
# Kullanıcıdan 10 adet sayı alalım ve bu sayılar arasından en büyük olanı kullanıcıya gösterelim.

nums = []
for i in range(10):
    num = int(input("Sayı girin:"))
    nums.append(num)
enBuyuk = max(nums)
x = f"En büyük değer: {enBuyuk}"
print(x)

# Kullanıcının vereceği üst limit ile 0'dan bu üst limite kadar olan tüm 'çift' sayıları ekrana yazdıralım.
ustLimit = int(input("Üst limit giriniz:"))

list = []

for ciftSayi in range(0 , ustLimit):
    if ciftSayi %2 == 0:
        list.append(ciftSayi)

print(list)

# 2. geliştirdiğimiz programa kullanıcının alt limiti belirlemesi için gerekli desteği ekleyelim.
a = int(input("Alt limit giriniz?"))
u = int(input("Üst limit giriniz?"))
S = []
for cıftSayi in range(a+1, u):
  if cıftSayi > 0 and cıftSayi%2 == 0:
    S.append(cıftSayi)
    
print(S)    
class Human:
    def talk(self):
        #class içerisinde fonksiyon kullanıyorsak bir parametre kullanmalıyız.(genellikle bu self olur.)
        print("Human is talking..")
    def walk(self):
        print("Human is walking..")

human1=Human()
human1.talk()
human1.walk()

class Human:

    name = "Ümit"
    def __init__(self, name):
        self.name = name
        print("Bir human instance'i üretildi.")

    def __str__(self):
        return f"str fonk. dönen değer: {self.name}"

    def talk(self,sentence):
        print(f"{self.name}: {sentence}")
    def walk(self):
        print(f"{self.name} is walking..")



human2 = Human("Alİ")  
#human2.name="Veli"     
#human2.talk()
human2.walk()
human2.talk("Merhaba")
print(human2)

human3 =Human("Ayşe")
#human3.name = "Fatma"
human3.talk("Merhaba")
human3.walk()
print(human3)
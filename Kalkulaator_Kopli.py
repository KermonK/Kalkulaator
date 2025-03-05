import math #Imporditakse kõik funktsioonid mis seonudvad matemaatikaga.


class Cal: #Templiit millegi tegevuseks nagu näiteks "objekt" kalkulaator.
    def __init__(self, num1, num2): # def kasutatakse funktsiooni määramiseks ning __init__ on eriline meetodi nimi mis on automaatselt lisatud kui luuakse uus objekt. Self viitab objektile.
        self.num1 = num1 #
        self.num2 = num2

    def liitmine(self):
        return self.num1 + self.num2 #see lõpetab funktsiooni töö ja viib väärtuse välja, mis saab olema funktsiooni tulemus.
    def lahutamine(self):
        return self.num1 - self.num2
    def korrutamine(self):
        return self.num1 * self.num2
    def jagamine(self):
        return self.num1 / self.num2
    def jaak(self):
        return self.num1 % self.num2
    def ruutjuur(self):
        return self.num1 ** self.num2
    def siinus(self): #Siinus funktsioon, mis arvutab a-sisendi siinusväärtuse
        return math.sin(math.radians(self.num1))
    def koosinus(self): #Koosinus funktsioon, mis arvutab a-sisendi koosinusväärtuse
        return math.cos(math.radians(self.num1))
num1 = int(input("Sisesta esimene number: ")) # antud käsku kasutatakse selleks, et saada kasutajalt sisend ja muuta see täis arvuks.
num2 = int(input("Sisesta teine number: ")) # antud käsku kasutatakse selleks, et saada kasutajalt sisend ja muuta see täis arvuks.

kalk = Cal(num1,num2)
while True: #tähendab lõpmatut tsüklit. While käivitub siis kui tingimus on tõene ning True kui on alati tõene. Niikaua loopib kuni katkestatakse käsuga break
    def menu():
        x = '1. Liitmine \n2. lahutamine\n3. korrutamine\n4. jagamine\n5. Jäägi leidmine\n6. Ruutjuure leidmine\n7. Siinuse leidmine\n8. Koosinuse leidmine '
        print(x)
    menu()
    valik = int(input('Sisesta üks valikutest: '))
    if valik == 1:
        print("Vastus: ",kalk.liitmine())
        break
    elif valik == 2:
        print("Vastus: ",kalk.lahutamine())
        break
    elif valik == 3:
        print("Vastus: ",kalk.korrutamine())
        break
    elif valik == 4:
        print("Vastus: ",kalk.jagamine())
        break
    elif valik == 5:
        print("Vastus: ",kalk.jaak())
        break
    elif valik == 6:
        print("Vastus: ",kalk.ruutjuur())
        break
    elif valik == 7:
        print("Vastus: ",kalk.siinus()) # Siinuse valiku kuvamine
        break
    elif valik == 8:
        print("Vastus: ",kalk.koosinus()) #Koosinuse valiku kuvamine
        break
    else:
        print('Sisestatud number ei ole kasutusel. Palun proovige uuesti.')

#10.25: today
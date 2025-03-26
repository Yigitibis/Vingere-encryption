alfabe = 'abcdefghijklmnopqrstuvwxyz'

class MesajCevaplayici:
    def __init__(self, anahtar):
        self._anahtar = anahtar

harften_indekse= dict(zip(alfabe, range(len(alfabe))))
indeksten_harfe= dict(zip(range(len(alfabe)), alfabe))

def sifrele(mesaj, anahtar) :
    sifrelendi = ''
    
    bolunmus_mesaj = [mesaj[i:i + len(anahtar)]for i in range(0, len(mesaj), len(anahtar))]
    
    for her_bolme in bolunmus_mesaj:
        i =0
        for harf in her_bolme:
            sayı = (harften_indekse[harf] + harften_indekse[anahtar[i]]) % len(alfabe) #mod 26
            sifrelendi += indeksten_harfe [sayı]
            i+=1
    
    return sifrelendi

def desifrele(sifre, anahtar) :
    desifrelendi = ''

    bolunmus_sifre = [sifre[i:i + len(anahtar)]for i in range(0, len(sifre), len(anahtar))] 
    
    for her_bolme in bolunmus_sifre:
        i =0
        for harf in her_bolme:
            sayı = (harften_indekse[harf] - harften_indekse[anahtar[i]]) % len(alfabe) #mod 26
            desifrelendi += indeksten_harfe [sayı]
            i+=1
    
    return desifrelendi



def main():
    anahtar = input("Anahtar giriniz: ")
    mesaj = input("Şifrelenecek mesajı giriniz: ")
    sifrelenmis_mesaj = sifrele(mesaj, anahtar)
    desifrelenmis_mesaj = desifrele(sifrelenmis_mesaj, anahtar)

    print('Mesaj: ' + mesaj)
    print('Sifrelenmis Mesaj: ' + sifrelenmis_mesaj)
    print('Desifrelenmis Mesaj: ' + desifrelenmis_mesaj)
    
    
    pass

main()
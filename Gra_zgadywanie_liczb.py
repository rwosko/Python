import random
sekret = random.randint(0,100)
propozycja = 0
proba = 0
print "Mam dla Ciebie zagadk�!"
print "Jest ni� tajemna liczba od 0 do 100. Na jej odgadni�cie masz 6 pr�b."
while propozycja != sekret and proba < 6:
    propozycja = input("Jaka to liczba? ")
    if propozycja < sekret:
        print "Za ma�a"
    elif propozycja > sekret:
        print "Za du�a"

    proba = proba + 1

if propozycja == sekret:
    print "Uda�o Ci si�! Odgad�e� tajemn� liczb�!"
else:
    print "Wykorzysta�e� wszystkie pr�by. Powodzenia nast�pnym razem"
    print "Tajemna liczba to: ", sekret

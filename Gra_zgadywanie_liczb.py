import random
sekret = random.randint(0,100)
propozycja = 0
proba = 0
print "Mam dla Ciebie zagadkê!"
print "Jest ni¹ tajemna liczba od 0 do 100. Na jej odgadniêcie masz 6 prób."
while propozycja != sekret and proba < 6:
    propozycja = input("Jaka to liczba? ")
    if propozycja < sekret:
        print "Za ma³a"
    elif propozycja > sekret:
        print "Za du¿a"

    proba = proba + 1

if propozycja == sekret:
    print "Uda³o Ci siê! Odgad³eœ tajemn¹ liczbê!"
else:
    print "Wykorzysta³eœ wszystkie próby. Powodzenia nastêpnym razem"
    print "Tajemna liczba to: ", sekret

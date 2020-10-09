print('Tato aplikace neni blbu-vzdorna takze se snazte doplnit ')
print('Zdravim, toto je tvuj pribeh a bude se jmenovat:')
nazev = input()
print('\n')
print('Zadej jmeno sveho hrdiny:')
jmeno = input()
print('\n')
print('Zadej jmeno sveho nepritele:')
nepritel = input()
print('\n')

i=0
for i in range(3):
    if i==0:
        print('Za sedmero horami')
    elif i==1:
        print('Za sedmero řekami')
    else:
        print('Za devatero ropnými skvrnami')
        i+=1

print('Zil jeden statecny rytir '+ jmeno + ' ktery se vydal na vypravu proti zlemu ' + nepritel + 'ovi')
print('Hej! davas pozor? Vypravec zapomnel jak dlouho trvala tva vyprava, porad mu (cislo): ')
delka = input()
print('\n')
print(jmeno + ' stravil na ceste ' + delka + ' dni ale pres tu dlouhou cestu se dostal ke zlemu '+ nepritel + 'ovi')
print('Nadesel cas souboje! Jakou zbra si '+ jmeno + ' zvolil? ')
zbran1 = input()
print('\n')
print(jmeno + ' si zvolil ' + zbran1 + ' ktery nebyl ucinny a '+ nepritel + ' ho zranil!')
print(jmeno + ' ma posledni sanci na vytezstvi, co puzije? ')
zbran2 = input()
print('\n')
print(jmeno + ' pouzil ' + zbran2 + ' a utok byl super ucinny!')
print(nepritel + ' zemrel a ' + jmeno + ' vyhal, GRATULUJU!')

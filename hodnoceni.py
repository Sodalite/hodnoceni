


class Criteria:
    def __init__(self):

        self.kriteria={'1a13':'Požadovaná charakteristika textu je dodržena.',
                       '1a12':'Požadovaná charakteristika textu je většinou dodržena.',
                       '1a11':'Požadovaná charakteristika textu není většinou dodržena.',
                       '1a10':'Požadovaná charakteristika není dodržena.',
                       '1a23':'Všechny body zadání jsou jasně a srozumitelně zmíněny.',
                       '1a22':'Většina bodů zadání je jasně a srozumitelně zmíněna.',
                       '1a21':'Většina bodů zadání není zmíněna.',
                       '1a20':'Body zadání nejsou zmíněny.',
                       '1a33':'Délka textu odpovídá požadovanému rozsahu.',
                       '1a32':'Délka textu ne zcela odpovídá rozsahu. Text je o jeden interval kratší.',
                       '1a31':'Délka textu ve větší míře neodpovídá rozsahu. Text je o dva intervaly kratší.',
                       '1a30':'Délka textu neodpovídá požadovanému rozsahu nebo není dostatek srozumitelného textu pro hodnocení.',
                       '1b13':'Body zadání jsou rozpracovány vhodně a v odpovídající míře podrobnosti.',
                       '1b12':'Body zadání jsou většinou rozpracovány vhodně a v odpovídající míře podrobnosti.',
                       '1b11':'Body zadání jsou jen ojediněle rozpracovány vhodně a v odpovídající míře podrobnosti.',
                       '1b10':'Body zadání nejsou rozpracovány.',
                       '1b23':'V textu je jasně vysvětlena podstata myšlenky nebo problému.',
                       '1b22':'V textu je většinou jasně vysvětlena podstata myšlenky nebo problému.',
                       '1b21':'V textu není ve větší míře vysvětlena podstata myšlenky nebo problému.',
                       '1b20':'V textu není vůbec vysvětlena podstata myšlenky nebo problému.',
                       '1b33':'Text neobsahuje irelevantní informace a myšlenky.',
                       '1b32':'Text ojediněle obsahuje irelevantní informace a myšlenky.',
                       '1b31':'Text ve větší míře obsahuje irelevantní informace a myšlenky.',
                       '1b30':'Text neobsahuje téměř žádné relevantní informace a myšlenky.',
                       '2a13':'Text je souvislý s lineárním sledem myšlenek.',
                       '2a12':'Text je většinou souvislý s lineárním sledem myšlenek.',
                       '2a11':'Text není ve větší míře souvislý s lineárním sledem myšlenek.',
                       '2a10':'Text není souvislý a neobsahuje lineární sled myšlenek.',
                       '2a23':'Text je vhodně organizovaný.',
                       '2a22':'Text je většinou vhodně organizovaný.',
                       '2a21':'Text není ve větší míře vhodně organizovaný.',
                       '2a20':'Text není vhodně organizovaný.',
                       '2b13':'Chyby v PTN nebrání porozumění textu.',
                       '2b12':'Chyby v PTN jen v malé míře brání porozumění textu.',
                       '2b11':'Chyby v PTN ve větší míře brání porozumění textu.',
                       '2b10':'PTN jsou použity nevhodně nebo v nedostatečném rozsahu.',
                       '2b23':'Rozsah PTN je široký.',
                       '2b22':'Rozsah PTN je většinou široký.',
                       '2b21':'Rozsah PTN je ve větší míře omezený.',
                       '2b20':'V textu téměř úplně chybí PTN.',
                       '2b33':'PTN jsou použity správně a vhodně.',
                       '2b32':'PTN jsou většinou použity správně a vhodně.',
                       '2b31':'PTN nejsou ve větší míře použity správně a vhodně.',
                       '2b30':'PTN nejsou téměř nikdy použity správně.',
                       '3a13':'Chyby ve slovní zásobě a pravopise nebrání porozumění textu.',
                       '3a12':'Chyby ve slovní zásobě a pravopise většinou nebrání porozumění textu.',
                       '3a11':'Chyby ve slovní zásobě a pravopise ve větší míře brání porozumění textu.',
                       '3a10':'Chyby ve slovní zásobě a pravopise brání porozumění textu.',
                       '3a23':'Slovní zásoba a pravopis jsou téměř vždy použity správně (0-5 chyb).',
                       '3a22':'Slovní zásoba a pravopis jsou většinou použity správně (6-11 chyb).',
                       '3a21':'Slovní zásoba a pravopis nejsou ve větší míře použity správně (12-17 chyb).',
                       '3a20':'Slovní zásoba a pravopis jsou použity nesprávně (více než 18 chyb).',
                       '3a33':'Text je dostatečně dlouhý.',
                       '3a32':'Text je o jeden interval kratší.',
                       '3a31':'Text je o dva intervaly kratší.',
                       '3a30':'Text je příliš krátký.',
                       '3b13':'Slovní zásoba je široká (vzhled k míře rozpracování bodů zadání).',
                       '3b12':'Slovní zásoba je většinou široká (vzhled k míře rozpracování bodů zadání).',
                       '3b11':'Slovní zásoba je ve větší míře omezená (vzhled k míře rozpracování bodů zadání).',
                       '3b10':'Slovní zásoba je omezená a v nedostačném rozsahu (vzhled k míře rozpracování bodů zadání).',
                       '4a13':'Chyby v mluvnických prostředcích nebrání porozumění textu.',
                       '4a12':'Chyby v mluvnických prostředcích většinou nebrání porozumění textu.',
                       '4a11':'Chyby v mluvnických prostředcích ve větší míře brání porozumění textu.',
                       '4a10':'Chyby v mluvnických prostředcích brání porozumění textu.',
                       '4a23':'Mluvnické prostředky jsou téměř vždy použity správně (0-5 chyb).',
                       '4a22':'Mluvnické prostředky jsou většinou použity správně (6-11 chyb).',
                       '4a21':'Mluvnické prostředky nejsou ve větší míře použity správně (12-17 chyb).',
                       '4a20':'Mluvnické prostředky jsou ve většině textu použity nesprávně (více než 18 chyb).',
                       '4a33':'Text je dostatečně dlouhý.',
                       '4a32':'Text je o jeden interval kratší.',
                       '4a31':'Text je o dva intervaly kratší.',
                       '4a30':'Text je příliš krátký.',
                       '4b13':'Rozsah mluvnických prostředků je široký (vzhled k míře rozpracování bodů zadání).',
                       '4b12':'Rozsah mluvnických prostředků je většinou široký (vzhled k míře rozpracování bodů zadání).',
                       '4b11':'Rozsah mluvnických prostředků je ve větší míře omezený (vzhled k míře rozpracování bodů zadání).',
                       '4b10':'Rozsah mluvnických prostředků je omezený  (vzhled k míře rozpracování bodů zadání).'}



    def provideLine(self,which):
        line = self.kriteria[which]
        return(line)



class Evaluation:
    def __init__(self):
        self.celkemBody = 0
        self.oneABody = 0
        self.oneBBody = 0
        self.twoABody = 0
        self.twoBBody = 0
        self.threeABody = 0
        self.threeBBody = 0
        self.fourABody = 0
        self.fourBBody = 0
        self.report = []

    def calculate(self,seznam):
        delka = len(seznam)

        soucet = 0
        for i in seznam:
            soucet = soucet + i

        body = int(round(soucet/delka,0))
        return(body)

    def keepScore(self,where,score):
        if where == 'a1':
            self.oneABody = score
        elif where == 'b1':
            self.oneBBody = score
        elif where == 'a2':
            self.twoABody = score
        elif where == 'b2':
            self.twoBBody = score
        elif where == 'a3':
            self.threeABody = score
        elif where == 'b3':
            self.threeBBody = score
        elif where == 'a4':
            self.fourABody = score
        elif where == 'b4':
            self.fourBBody = score


    def provideScore(self):
        points = self.oneABody+self.oneBBody+self.twoABody+self.twoBBody+self.threeABody+self.threeBBody+self.fourABody+self.fourBBody
        total = 24
        percentage = int(round((points/total)*100,0))
        return(points,percentage)

    def provideGraph(self):
        lines = ['']
        lines.append('   1 | 2 | 3 | 4 |')
        lines.append('_______________________')
        lines.append(('A  '+str(self.oneABody)+' | '+str(self.twoABody)+' | '+str(self.threeABody)+' | '+str(self.fourABody)+' | '))
        lines.append('_______________________')
        lines.append(('B  '+str(self.oneBBody)+' | '+str(self.twoBBody)+' | '+str(self.threeBBody)+' | '+str(self.fourBBody)+' | '))
        return(lines)



lines = Criteria()
evaluace = Evaluation()
hodnoceni = []


name = input('Jméno a příjmení hodnoceného: ')

# Sběr bodů za IA
print('Část IA - deskriptor 1')
print(' ')
print('3 body - ',lines.kriteria['1a13'])
print('2 body - ',lines.kriteria['1a12'])
print('1 bod - ',lines.kriteria['1a11'])
print('0 body - ',lines.kriteria['1a10'])
a = int(input('Kolik bodů zvolíte pro tento deskriptor?: '))

if a==3:
    volba = '1a13'
elif a==2:
    volba = '1a12'
elif a==1:
    volba = '1a11'
else:
    volba = '1a10'

volba = lines.provideLine(volba)    
hodnoceni.append(volba)

print('----------------------------------------------------')

print('Část IA - deskriptor 2')
print(' ')
print('3 body - ',lines.kriteria['1a23'])
print('2 body - ',lines.kriteria['1a22'])
print('1 bod - ',lines.kriteria['1a21'])
print('0 body - ',lines.kriteria['1a20'])
b = int(input('Kolik bodů zvolíte pro tento deskriptor?: '))
print('----------------------------------------------------')

if b==3:
    volba = '1a23'
elif b==2:
    volba = '1a22'
elif b==1:
    volba = '1a21'
else:
    volba = '1a20'
volba = lines.provideLine(volba)
hodnoceni.append(volba)

print('Část IA - deskriptor 3')
print(' ')
print('3 body - ',lines.kriteria['1a33'])
print('2 body - ',lines.kriteria['1a32'])
print('1 bod - ',lines.kriteria['1a31'])
print('0 body - ',lines.kriteria['1a30'])
c = int(input('Kolik bodů zvolíte pro tento deskriptor?: '))
print('----------------------------------------------------')

if c==3:
    volba = '1a33'
elif c==2:
    volba = '1a32'
elif c==1:
    volba = '1a31'
else:
    volba = '1a30'
volba = lines.provideLine(volba)
hodnoceni.append(volba)

body = [a,b,c]
scr = evaluace.calculate(body)
evaluace.keepScore('a1',scr)

#Sběr bodů za IB

print('Část IB - deskriptor 1')
print(' ')
print('3 body - ',lines.kriteria['1b13'])
print('2 body - ',lines.kriteria['1b12'])
print('1 bod - ',lines.kriteria['1b11'])
print('0 body - ',lines.kriteria['1b10'])
a = int(input('Kolik bodů zvolíte pro tento deskriptor?: '))
print('----------------------------------------------------')

if a==3:
    volba = '1b13'
elif a==2:
    volba = '1b12'
elif a==1:
    volba = '1b11'
else:
    volba = '1b10'
volba = lines.provideLine(volba)
hodnoceni.append(volba)

print('Část IB - deskriptor 2')
print(' ')
print('3 body - ',lines.kriteria['1b23'])
print('2 body - ',lines.kriteria['1b22'])
print('1 bod - ',lines.kriteria['1b21'])
print('0 body - ',lines.kriteria['1b20'])
b = int(input('Kolik bodů zvolíte pro tento deskriptor?: '))
print('----------------------------------------------------')

if b==3:
    volba = '1b23'
elif b==2:
    volba = '1b22'
elif b==1:
    volba = '1b21'
else:
    volba = '1b20'
volba = lines.provideLine(volba)
hodnoceni.append(volba)

print('Část IB - deskriptor 3')
print(' ')
print('3 body - ',lines.kriteria['1b33'])
print('2 body - ',lines.kriteria['1b32'])
print('1 bod - ',lines.kriteria['1b31'])
print('0 body - ',lines.kriteria['1b30'])
c = int(input('Kolik bodů zvolíte pro tento deskriptor?: '))
print('----------------------------------------------------')

if c==3:
    volba = '1b33'
elif c==2:
    volba = '1b32'
elif c==1:
    volba = '1b31'
else:
    volba = '1b30'
volba = lines.provideLine(volba)
hodnoceni.append(volba)

body = [a,b,c]
scr = evaluace.calculate(body)
evaluace.keepScore('b1',scr)
hodnoceni.append('\n\n')

#Sběr bodů za IIA

print('Část IIA - deskriptor 1')
print(' ')
print('3 body - ',lines.kriteria['2a13'])
print('2 body - ',lines.kriteria['2a12'])
print('1 bod - ',lines.kriteria['2a11'])
print('0 body - ',lines.kriteria['2a10'])
a = int(input('Kolik bodů zvolíte pro tento deskriptor?: '))
print('----------------------------------------------------')

if a==3:
    volba = '2a13'
elif a==2:
    volba = '2a12'
elif a==1:
    volba = '2a11'
else:
    volba = '2a10'
volba = lines.provideLine(volba)
hodnoceni.append(volba)

print('Část IIA - deskriptor 2')
print(' ')
print('3 body - ',lines.kriteria['2a23'])
print('2 body - ',lines.kriteria['2a22'])
print('1 bod - ',lines.kriteria['2a21'])
print('0 body - ',lines.kriteria['2a20'])
b = int(input('Kolik bodů zvolíte pro tento deskriptor?: '))
print('----------------------------------------------------')

if b==3:
    volba = '2a23'
elif b==2:
    volba = '2a22'
elif b==1:
    volba = '2a21'
else:
    volba = '2a20'
volba = lines.provideLine(volba)
hodnoceni.append(volba)

body = [a,b]
scr = evaluace.calculate(body)
evaluace.keepScore('a2',scr)

#Sběr bodů za IIB

print('Část IIB - deskriptor 1')
print(' ')
print('3 body - ',lines.kriteria['2b13'])
print('2 body - ',lines.kriteria['2b12'])
print('1 bod - ',lines.kriteria['2b11'])
print('0 body - ',lines.kriteria['2b10'])
a = int(input('Kolik bodů zvolíte pro tento deskriptor?: '))
print('----------------------------------------------------')

if a==3:
    volba = '2b13'
elif a==2:
    volba = '2b12'
elif a==1:
    volba = '2b11'
else:
    volba = '2b10'
volba = lines.provideLine(volba)
hodnoceni.append(volba)

print('Část IIB - deskriptor 2')
print(' ')
print('3 body - ',lines.kriteria['2b23'])
print('2 body - ',lines.kriteria['2b22'])
print('1 bod - ',lines.kriteria['2b21'])
print('0 body - ',lines.kriteria['2b20'])
b = int(input('Kolik bodů zvolíte pro tento deskriptor?: '))
print('----------------------------------------------------')

if b==3:
    volba = '2b23'
elif b==2:
    volba = '2b22'
elif b==1:
    volba = '2b21'
else:
    volba = '2b20'
volba = lines.provideLine(volba)
hodnoceni.append(volba)

print('Část IIB - deskriptor 3')
print(' ')
print('3 body - ',lines.kriteria['2b33'])
print('2 body - ',lines.kriteria['2b32'])
print('1 bod - ',lines.kriteria['2b31'])
print('0 body - ',lines.kriteria['2b30'])
c = int(input('Kolik bodů zvolíte pro tento deskriptor?: '))
print('----------------------------------------------------')

if c==3:
    volba = '2b33'
elif c==2:
    volba = '2b32'
elif c==1:
    volba = '2b31'
else:
    volba = '2b30'
volba = lines.provideLine(volba)
hodnoceni.append(volba)
hodnoceni.append('\n')

body = [a,b,c]
scr = evaluace.calculate(body)
evaluace.keepScore('b2',scr)


#Sběr bodů za IIIA

print('Část IIIA - deskriptor 1')
print(' ')
print('3 body - ',lines.kriteria['3a13'])
print('2 body - ',lines.kriteria['3a12'])
print('1 bod - ',lines.kriteria['3a11'])
print('0 body - ',lines.kriteria['3a10'])
a = int(input('Kolik bodů zvolíte pro tento deskriptor?: '))
print('----------------------------------------------------')

if a==3:
    volba = '3a13'
elif a==2:
    volba = '3a12'
elif a==1:
    volba = '3a11'
else:
    volba = '3a10'
volba = lines.provideLine(volba)
hodnoceni.append(volba)

print('Část IIIA - deskriptor 2')
print(' ')
print('3 body - ',lines.kriteria['3a23'])
print('2 body - ',lines.kriteria['3a22'])
print('1 bod - ',lines.kriteria['3a21'])
print('0 body - ',lines.kriteria['3a20'])
b = int(input('Kolik bodů zvolíte pro tento deskriptor?: '))
print('----------------------------------------------------')

if b==3:
    volba = '3a23'
elif b==2:
    volba = '3a22'
elif b==1:
    volba = '3a21'
else:
    volba = '3a20'
volba = lines.provideLine(volba)
hodnoceni.append(volba)

print('Část IIIA - deskriptor 3')
print(' ')
print('3 body - ',lines.kriteria['3a33'])
print('2 body - ',lines.kriteria['3a32'])
print('1 bod - ',lines.kriteria['3a31'])
print('0 body - ',lines.kriteria['3a30'])
c = int(input('Kolik bodů zvolíte pro tento deskriptor?: '))
print('----------------------------------------------------')

if c==3:
    volba = '3a33'
elif c==2:
    volba = '3a32'
elif c==1:
    volba = '3a31'
else:
    volba = '3a30'
volba = lines.provideLine(volba)
hodnoceni.append(volba)

body = [a,b,c]
scr = evaluace.calculate(body)
evaluace.keepScore('a3',scr)

#Sběr bodů za IIIB

print('Část IIIB - deskriptor 1')
print(' ')
print('3 body - ',lines.kriteria['3b13'])
print('2 body - ',lines.kriteria['3b12'])
print('1 bod - ',lines.kriteria['3b11'])
print('0 body - ',lines.kriteria['3b10'])
a = int(input('Kolik bodů zvolíte pro tento deskriptor?: '))
print('----------------------------------------------------')

if a==3:
    volba = '3b13'
elif a==2:
    volba = '3b12'
elif a==1:
    volba = '3b11'
else:
    volba = '3b10'
volba = lines.provideLine(volba)
hodnoceni.append(volba)
hodnoceni.append('\n')


body = [a]
scr = evaluace.calculate(body)
evaluace.keepScore('b3',scr)
        
#Sběr bodů za IVA

print('Část IVA - deskriptor 1')
print(' ')
print('3 body - ',lines.kriteria['4a13'])
print('2 body - ',lines.kriteria['4a12'])
print('1 bod - ',lines.kriteria['4a11'])
print('0 body - ',lines.kriteria['4a10'])
a = int(input('Kolik bodů zvolíte pro tento deskriptor?: '))
print('----------------------------------------------------')

if a==3:
    volba = '4a13'
elif a==2:
    volba = '4a12'
elif a==1:
    volba = '4a11'
else:
    volba = '4a10'
volba = lines.provideLine(volba)
hodnoceni.append(volba)

print('Část IVA - deskriptor 2')
print(' ')
print('3 body - ',lines.kriteria['4a23'])
print('2 body - ',lines.kriteria['4a22'])
print('1 bod - ',lines.kriteria['4a21'])
print('0 body - ',lines.kriteria['4a20'])
b = int(input('Kolik bodů zvolíte pro tento deskriptor?: '))
print('----------------------------------------------------')

if b==3:
    volba = '4a23'
elif b==2:
    volba = '4a22'
elif b==1:
    volba = '4a21'
else:
    volba = '4a20'
volba = lines.provideLine(volba)
hodnoceni.append(volba)

print('Část IVA - deskriptor 3')
print(' ')
print('3 body - ',lines.kriteria['4a33'])
print('2 body - ',lines.kriteria['4a32'])
print('1 bod - ',lines.kriteria['4a31'])
print('0 body - ',lines.kriteria['4a30'])
c = int(input('Kolik bodů zvolíte pro tento deskriptor?: '))
print('----------------------------------------------------')

if c==3:
    volba = '4a33'
elif c==2:
    volba = '4a32'
elif c==1:
    volba = '4a31'
else:
    volba = '4a30'
volba = lines.provideLine(volba)
hodnoceni.append(volba)

body = [a,b,c]
scr = evaluace.calculate(body)
evaluace.keepScore('a4',scr)

#Sběr bodů za IVB

print('Část IIIB - deskriptor 1')
print(' ')
print('3 body - ',lines.kriteria['4b13'])
print('2 body - ',lines.kriteria['4b12'])
print('1 bod - ',lines.kriteria['4b11'])
print('0 body - ',lines.kriteria['4b10'])
a = int(input('Kolik bodů zvolíte pro tento deskriptor?: '))
print('----------------------------------------------------')

if a==3:
    volba = '4b13'
elif a==2:
    volba = '4b12'
elif a==1:
    volba = '4b11'
else:
    volba = '4b10'
volba = lines.provideLine(volba)
hodnoceni.append(volba)


body = [a]
scr = evaluace.calculate(body)
evaluace.keepScore('b4',scr)

print('---------------------------------------------------------------')
print('Hodnocení písemné práce: ',name)
print('')
celkem = evaluace.provideScore()
print('Celkový počet dosažených bodů je: ',celkem[0],'. To je ',celkem[1],' procent.')
#print('To je ',celkem[1],' procent.')
print('---------------------------------------------------------------')

lines = evaluace.provideGraph()
for line in lines:
    print(line)

print('--------------------------------------------------------------')

print('Hodnocení\n')

for hod in hodnoceni:
    print(hod)


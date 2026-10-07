import random
import time
import sys

def slowPrint(string, speed=0.075):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    time.sleep(0.2)

def clear():
    print("\033[H\033[J", end="")

# ░ ▒ ▓ ▐ ▌

dark = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
grey = [13, 14, 15, 16, 17, 18, 23, 24, 25, 26, 27, 28]

def printGraphic(liv, drak_liv):
    print(f"""
Spelare_liv:{liv} Drake_liv:{drak_liv}

                ,.
 o   o         /,,;';;.  ,;;;..  ,,;.    '
/|\ /|\      .',''   `::;:' ``;;;;'  `..'
/ \ / \      `      ,,/'     ,,//         
""")

def printGraphic_utan_drake(liv, drak_liv):
    print(f"""
Spelare_liv:{liv} Drake_liv:{drak_liv}

                
 o   o        
/|\ /|\      
/ \ / \              
""")

def drake_skada(liv, drak_liv):
    for x in range (1, 6):
        printGraphic(liv, drak_liv)
        time.sleep(0.5)
        clear()
        printGraphic_utan_drake(liv, drak_liv)
        time.sleep(0.5)
        clear()

def spelare_skada(liv, drak_liv):
    for x in range (1, 6):
        print(f"""
Spelare_liv:{liv} Drake_liv:{drak_liv}

                ,.
 o   o         /,,;';;.  ,;;;..  ,,;.    '
/|\ /|\      .',''   `::;:' ``;;;;'  `..'
/ \ / \      `      ,,/'     ,,//         
""")
        time.sleep(0.5)
        clear()
        print(f"""
Spelare_liv:{liv} Drake_liv:{drak_liv}

                ,.
               /,,;';;.  ,;;;..  ,,;.    '
             .',''   `::;:' ``;;;;'  `..'
             `      ,,/'     ,,//         
""")
        time.sleep(0.5)
        clear()

def intro():
    slowPrint("Du lever i en konstig värld där monster och andra varelser finns... ")
    time.sleep(1)
    slowPrint("Du blev nyss jagad av några monster pirater men du blev omringad utanför ingången till en grotta... ")
    time.sleep(1)
    slowPrint("Du valde att springa in i grottan och använda ditt sista skott i din hand kanon för att spränga taket på ingången. ")
    time.sleep(1)
    slowPrint("Taket föll ner så nu kan piraterna inte nå dig men när du tänder din lykta och vänder dig om ser du två tunnlar. ")
    time.sleep(1)
    slowPrint("Du hör ett ekande skrik genom tunnlarna men du vet inte vilken ljudet kom ifrån... Du måste hitta en väg ut.")

def deathcase():
    val = input("Du dog. Vill du fortsätta spela från tidigare frågan eller avsluta?(börja om/avsluta): ")
    return val

def drakdöd():
    slowPrint("Du ställer dig upp och går försiktigt fram till draken. Den sover fortfarande. Du fortsätter gå runt draken men när du nästan är vid dörren så trampar du på en pinne... ")
    time.sleep(1)
    slowPrint("Draken öppnar sina ögon och får direkt ögonkontakt med dig och innan du vet vad så är allt svart... ")
    time.sleep(2)
    clear()

def vilken_tunnel():
    val = input("Väljer du tunneln till höger eller den till vänster?(höger/vänster): ")
    clear()
    return val

def höger_tunnel():
    if höger_start == 1:
        slowPrint("Du går försiktigt ner genom den mörka tunneln... ")
        time.sleep(1)
        slowPrint("Efter du gått en stund så ser du lite ljus och slutet av tunneln. När du väl kommer närmare så ser du en stor sovande drake på golvet. ")
        time.sleep(1)
        slowPrint("Du faller bakom en gammal trä låda fylld av skräck men du vet att draken varken sett eller hört dig. ")
        time.sleep(1)
        slowPrint("När du väl vågar kolla över lådan så ser du en förspikad dörr bakom draken. ")
        time.sleep(1)
        slowPrint("Kan det här vara den enda utgången?..")
        time.sleep(2)
        clear()
    else:
        if höger_start == 2:
            slowPrint("Draken är fortfarande kvar, sovandes... ")
            time.sleep(1)
            slowPrint("Du går tillbaka till början...")
            clear()
        else:
            slowPrint("Draken ligger på golvet, sovandes... ")
        slowPrint("")

def vänster_tunnel():
    if vänster_start == 2:
        slowPrint("Du har redan varit i vänster tunnel.")
    else:
        slowPrint("Du går ner den långa och mörka tunneln. Det ligger både människor och monster skelett utspritt längst med väggarna. ")
        slowPrint("När du går längst med väggen så börjar du fundera på vad det var som dödade alla de här varelserna. ")
        while True:
            slowPrint("En av skeletten har en påse guld i sin hand. Kommer du ta det?(ja/nej): ")
            val = input("")
            if val.lower() == "ja":
                slowPrint("Du har påsen med guld från skelettet... ")
                guld = 1
                break
            elif val.lower() == "nej":
                slowPrint("Du lämnar skelettet i fred. Kanske bättre att respektera de döda... ")
                guld = 0
                break
            else:
                print("fel inmatning.")
        time.sleep(1)
        clear()
        slowPrint("Du börjar se ljuset i slutet av tunneln... ")
        slowPrint("När du kommit fram så står du i ett rum som ser försvånadsvärt rent ut. ")
        slowPrint("Det finns ett bord i mitten av rummet, vapen hänger längst med väggen och det finns en eldstad som brinner med en gryta som kokar... ")
        slowPrint("Du hör ett fotsteg bakom dig, du vänder dig om raskt men du hinner inte se vem eller vad det är som slår dig i huvudet...")
        time.sleep(2)
        clear()
        time.sleep(1)
        slowPrint("När du vaknar till så sitter du fastlindrad i rep på en stol. På andra sidan bordet ser du någon som sitter och äter. ")
        slowPrint("Långsamt får du tillbaka din syn. Personen som sitter på andra sidan bordet visar sig att vara en annan människa. ")
        slowPrint(f"Han frågar ditt namn... Du säger att du heter {namn} ")
        slowPrint("Han frågar om du har något vapen samt massor andra frågor, du svarar ärligt... ")
        time.sleep(1)
        clear()
        slowPrint(f"Sen kommer den stora frågan, 'Vad är det som du gör i den här grottan, {namn}?' ")
        slowPrint("Du berättar allt. Han blir lite arg på dig eftersom du förstörde in- och utgången men han förstår vilken situation du är i... ")
        if höger_start == 2:
            slowPrint("Till slut så säger han att han kan hjälpa dig med att ta dig ut bakom draken. Men att det är väldigt riskabelt. ")
        else:
            slowPrint("Han berättar att det finns en annan väg ut. Men det är just där som draken är, oftast sovandes, men ibland kan den vakna och chansen att överleva en drakattack är otroligt smal. ")
            time.sleep(1)
            slowPrint("'Jag kan hjälpa dig', Säger han tillslut. 'Men det kommer kosta' ")
        slowPrint("Han befriar dig från repen. ")
        time.sleep(1)
        clear()
        if guld == 1:
            slowPrint("Du tar fram påsen med guld du plockat från skelettet och lägger det på bordet. ")
            slowPrint("Du säger till honom att han förtjänar det om han hjälper dig ta dig ut... ")
        else:
            slowPrint("Du kommer på att du gick förbi ett skelett med en påse guld. Du ursäktar digsjälv från bordet sen går du och hämtar påsen... ")
            slowPrint("Du lägger påsen på bordet och säger att han kan få den om du kommer ut.")
        time.sleep(1)
        clear()
        slowPrint("Han tar snabbt upp påsen, kollar igenom den, sen nickar han åt dig." )
        slowPrint("Han plockar ner några vapen från väggen och tar med sig det. 'Man vet aldrig vad som kan hända', säger han till sigsjälv... ")
        time.sleep(1)
        clear()

def slut():
    slowPrint("Ni går tillbaka till starten där du kom in. Han står och kollar på den blockerade in- och utgången en stund sen går han till höger.")
    time.sleep(1)
    clear()
    if höger_start == 2:
        slowPrint("Draken är fortfarande kvar, sovandes... ")
    else:
        slowPrint("Draken ligger på golvet där inne, sovandes... ")
    slowPrint("Han säger till dig att chansen att draken vaknar är hög. Men att det är tyvärr eran enda väg ut nu... ")
    slowPrint("Han börjar långsamt gå länst med väggen av rummet. Du följer efter. ")
    slowPrint("Ni rör er mot dörren bakom draken men när ni nästa är där så känner ni hur golvet skakar lite... ")
    slowPrint(f"'Känner du det där, {namn}?'... ")
    slowPrint("Ni vänder er om i sync och ser hur draken står upp, vaken, och flåsar åt er. ")
    slowPrint("Även fast ni nästan är vid dörren så har ni inte tid att bryta upp plankorna som sitter fast över dörren. ")
    slowPrint("Ni har bara ett val nu... Ni tar upp era vapen och förbereder er för strid. ")
    time.sleep(2)
    clear()

def tut():
    time.sleep(1)
    while True:
        clear()
        val = input("Vill du ha en tutorial för drak fighten?(ja / nej): ")
        if val.lower() == "ja":
            while True:
                clear()
                slowPrint("Du och draken kommer turas om att attackera varandra. ")
                slowPrint("När det är din tur att attackera kan du antingen heala eller attackera. ")
                time.sleep(1)
                clear()
                slowPrint("Om du väljer att attackera, kommer du se en rektangel uppdelad i olika nyanser av grått. ")
                print(" /n░░░░░░░░░░░░▒▒▒▒▒▒▓▓▐▌▓▒▒▒▒▒░░░░░░░░░░░░/n ")
                slowPrint("Ditt mål är att trycka (control + c) när den rörande delen av rektangeln ligger i mitten. ")
                time.sleep(1)
                clear()
                slowPrint("Om den hamnar rätt i mitten på ▓ så gör du 10 skada. ")
                slowPrint("Om den hamnar lite längre ut på ▒ så gör du 5 skada och om den hamnar utanför på det mörka så gör du 0 skada. ")
                time.sleep(1)
                clear()
                slowPrint("Om du väljer att heala så kommer du att ta rundan utan att få chansen att attackera men du kommer tjäna 10 hp. ")
                time.sleep(1)
                clear()
                val = input("Vill du ta om genomgången en gång till?(ja / nej): ")
                if val.lower() == "nej":
                    return
        elif val.lower() == "nej":
            break
        else:
            print("fel inmatning.")
            time.sleep(1)

def attack(speed, liv, drak_liv):
    x = 1
    try:
        direktion = 1
        while True:
            clear()
            printGraphic(liv, drak_liv)
            for i in range(1, 41):
                if x == i + 1:
                    sys.stdout.write("▐")
                elif x == i:
                    sys.stdout.write("▌")
                else:
                    if i in dark:
                        sys.stdout.write("░")
                    elif i in grey:
                        sys.stdout.write("▒")
                    else:
                        sys.stdout.write("▓")
            sys.stdout.flush()
            time.sleep(speed)
            if direktion == 1:
                x += 1
            else:
                x -= 1
            if x > 39:
                if direktion == 1:
                    direktion = 0
            elif x < 2:
                if direktion == 0:
                    direktion = 1
    except KeyboardInterrupt:
        pass
        
    if x in dark:
        return 0
    elif x in grey:
        return 1
    else:
        return 2

def kolla_död(liv):
    if liv <= 0:
        return 1
    else:
        return 0

def drakstrids():
    liv = 150
    drak_liv = 100
    while True:
        while True:
            clear()
            printGraphic(liv, drak_liv)
            val = input("Vill du attackera eller heala?(attackera / heala): ")
            if val.lower() == "attackera":
                clear()
                printGraphic(liv, drak_liv)
                slowPrint("Spelaren attackerar.")
                time.sleep(1)
                damage = attack(0.02, liv, drak_liv)
                clear()
                damage = damage * 5
                drak_liv = drak_liv - damage
                if damage > 0:
                    drake_skada(liv, drak_liv)
                printGraphic(liv, drak_liv)
                slowPrint(f"Du gjorde {damage} skada. ")
                break
            elif val.lower() == "heala":
                clear()
                printGraphic(liv, drak_liv)
                slowPrint("Du tar din tid och vilar lite. ")
                time.sleep(2)
                if liv + 10 > 150:
                    liv = 150
                else:
                    liv = liv + 10
                clear()
                printGraphic(liv, drak_liv)
                break
            else:
                clear()
                print("fel inmatning.")
                time.sleep(2)
        time.sleep(1)
        clear()
        if kolla_död(drak_liv) == 1:
            return 1
        printGraphic(liv, drak_liv)
        slowPrint("Draken attackerar.")
        drakeattack = random.randint(0, 2)
        clear()
        drakeattack = drakeattack * 10
        liv = liv - drakeattack
        if drakeattack > 0:
            spelare_skada(liv, drak_liv)
        else:
            time.sleep(1)
        printGraphic(liv, drak_liv)
        slowPrint(f"Draken gjorde {drakeattack} skada. ")
        time.sleep(1)
        if kolla_död(liv) == 1:
            return 0

def vinnst():
    slowPrint("Du lyckades döda draken. ")
    time.sleep(1)
    slowPrint("Du säger hejdå till din nya vänn. ")
    slowPrint(f"'Jag förväntar mig att du kommer sen och hjälper mig att öppna upp ingången som du förstörde, {namn}' säger han till dig. ")
    slowPrint("Du tackar för hjälpen och beger dig ut. ")
    time.sleep(2)
    clear()
    quit()

höger_start = 0
vänster_start = 0
guld = 0
val = ""

clear()
namn = input("vad är ditt namn?: ")
time.sleep(1)
clear()
intro()
time.sleep(2)
clear()

while True:
    val = vilken_tunnel()
    if val.lower() == "höger":
        clear()
        höger_start = 1
        höger_tunnel()
        while True:
            val = input("Vill du försöka smyga förbi draken till dörren eller vill du gå tillbaka för att se om du kan hitta någon annan väg ut?(smyg/tillbaka): ")
            clear()
            if val.lower() == "smyg":
                drakdöd()
                val = deathcase()
                if val.lower() == "avsluta":
                    quit()
            elif val.lower() == "tillbaka":
                höger_start = 2
                slowPrint("Du vänder dig om och vandrar tillbaka till där du började.")
                time.sleep(2)
                clear()
                while True:
                    val = vilken_tunnel()
                    if val.lower() == "höger":
                        höger_tunnel()
                    elif val.lower() == "vänster":
                        vänster_tunnel()
                        slut()
                        tut()
                        while True:
                            vinnst = drakstrids()
                            if vinnst == 1:
                                clear()
                                vinnst()
                            else:
                                clear()
                                time.sleep(1)
                                val = deathcase
                                if val.lower() == "avsluta":
                                    quit()
                    else:
                        print("fel inmatning.")
            else:
                print("fel inmatning.")
    elif val.lower() == "vänster":
        vänster_start = 1
        vänster_tunnel()
        slut()
        tut()
        while True:
            vinnst = drakstrids()
            if vinnst == 1:
                clear()
                vinnst()
            else:
                clear()
                time.sleep(1)
                val = deathcase
                if val.lower() == "avsluta":
                    quit()
    else:
        print("fel inmatning.")
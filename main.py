import random
import time
import sys

def slowPrint(string, speed=0.075):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)

def clear():
    print("\033[H\033[J", end="")

def intro():
    slowPrint("Du lever i en konstig värld där monster och andra varelser finns... ")
    time.sleep(1)
    slowPrint("Du blev nyss jagad av några monster pirater men du blev omringad utanför ingången till en grotta... ")
    time.sleep(1)
    slowPrint("Du valde att springa in i grottan och använda ditt sista skott i din hand kanon för att spränga taket på ingången. ")
    time.sleep(1)
    slowPrint("Taket föll ner så nu kan piraterna inte nå dig men när du tänder din lykta och vänder dig om ser du två tunnlar. ")
    time.sleep(1)
    slowPrint("Du har ett ekande skrik genom tunnlarna men du vet inte vilken ljudet kom ifrån... Du måste hitta en väg ut.")

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
        else:
            slowPrint("Draken ligger på golvet, sovandes... ")
        slowPrint("")

def vänster_tunnel():
    if vänster_start == 2:
        slowPrint("Du har redan varit i vänster tunnel.")
    else:
        slowPrint("Du går ner den långa och mörka tunneln. Det ligger både människor och monster skelett utspritt längst med väggarna. ")

höger_start = 0
vänster_start = 0
val = ""
#namn = input("vad är ditt namn?: ")

#intro()
#time.sleep(2)
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
                        time.sleep(1)
                        slowPrint("Du går tillbaka till början...")
                    elif val.lower() == "vänster":
                        vänster_tunnel()

                    else:
                        print("fel inmatning.")
            else:
                print("fel inmatning.")
    elif val.lower() == "vänster":
        vänster_start = 1
        vänster_tunnel()
    else:
        print("fel inmatning.")
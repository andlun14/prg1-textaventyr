import random
import time
import sys
import readchar
import keyboard
import pynput

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

def printGraphic():
    print(f"""
Spelare_liv:{liv} Drake_liv:{drak_liv}

                ,.
 o   o         /,,;';;.  ,;;;..  ,,;.    '
/|\ /|\      .',''   `::;:' ``;;;;'  `..'
/ \ / \      `      ,,/'     ,,//         
""")

def printGraphic_utan_drake():
    print(f"""
Spelare_liv:{liv} Drake_liv:{drak_liv}

                
 o   o        
/|\ /|\      
/ \ / \              
""")

def drake_skada():
    for x in range (1, 6):
        printGraphic()
        time.sleep(0.5)
        clear()
        printGraphic_utan_drake()
        time.sleep(0.5)
        clear()

def spelare_skada():
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

def attack(speed):
    x = 1
    try:
        direktion = 1
        while True:
            clear()
            printGraphic()
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

#damage = attack(0.02)
clear()
#print(damage)

liv = 100
drak_liv = 100

while True:
    while True:
        clear()
        printGraphic()
        val = input("Vill du attackera eller heala?(attackera / heala): ")
        if val.lower() == "attackera":
            clear()
            printGraphic()
            slowPrint("Spelaren attackerar.")
            time.sleep(1)
            damage = attack(0.02)
            clear()
            damage = damage * 5
            drak_liv = drak_liv - damage
            if damage > 0:
                drake_skada()
            printGraphic()
            slowPrint(f"Du gjorde {damage} skada. ")
            break
        elif val.lower() == "heala":
            clear()
            printGraphic()
            slowPrint("Du tar din tid och vilar lite. ")
            time.sleep(2)
            if liv + 10 > 100:
                liv = 100
            else:
                liv = liv + 10
            clear()
            printGraphic()
            break
        else:
            clear()
            print("fel inmatning.")
            time.sleep(2)
    time.sleep(1)
    clear()
    printGraphic()
    slowPrint("Draken attackerar.")
    drakeattack = random.randint(0, 2)
    clear()
    drakeattack = drakeattack * 10
    liv = liv - drakeattack
    if drakeattack > 0:
        spelare_skada()
    else:
        time.sleep(1)
    printGraphic()
    slowPrint(f"Draken gjorde {drakeattack} skada. ")
    time.sleep(1)
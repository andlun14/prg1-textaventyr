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

def attack(speed):
    x = 1
    try:
        direktion = 1
        while True:
            clear()
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
#clear()
#print(damage)

liv = 100
drak_liv = 100


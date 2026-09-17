import random
import time
import sys

def slowPrint(string, speed=0.05):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)

def clear():
    print("\033[H\033[J", end="")

namn = input("vad är ditt namn?: ")

slowPrint("intro intro intro...")

clear()

if input("Väljer du höger eller vänster?: ").lower() == "vänster":
    print("aa okej")
else:
    print("nja brush irrono")


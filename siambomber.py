# Codded By SIAM RAHMAN
# writen With python
import os, time
# color
# Color Value
blueVal = "94m"
redVal = "91m"
greenVal = "32m"
whiteVal = "97m"
yellowVal = "93m"
cyanVal = "96m"
# normal
normal = "\33["
# Bold
bold = "\033[1;"
# italic
italic = "\x1B[3m"
# Color Normal
blue = normal + blueVal  # Blue Color Normal
red = normal + redVal  # Red Color Normal
green = normal + greenVal  # Green Color Normal
white = normal + whiteVal  # white Color Normal
yellow = normal + yellowVal  # yellow Color Normal
cyan = normal + cyanVal  # Cyan Color Normal
# Color Bold
blueBold = bold + blueVal  # Blue Color Bold
redBold = bold + redVal  # Red Color Bold
greenBold = bold + greenVal  # Green Color Bold
whiteBold = bold + whiteVal  # white Color Bold
yellowBold = bold + yellowVal  # yellow Color Bold
cyanBold = bold + cyanVal  # Cyan Color Bold
# clear
def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
try:
    import requests
except:
    print(cyanBold + "installing requests.....", 0.05)
    time.sleep(2)
    os.system("pip install requests")
    import requests
    print(greenBold + "requests successfully installed.....", 0.05)
    time.sleep(2)
    clr()

try:
    import siambomber
except:
    print(cyanBold + "installing requests.....", 0.05)
    time.sleep(2)
    os.system("pip install siambomber")
    print(greenBold + "siambomber successfully installed.....", 0.05)
    time.sleep(2)
    clr()

os.chdir('.main')
os.system('python main.py')

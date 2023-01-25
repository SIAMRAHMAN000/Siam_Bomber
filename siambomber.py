import os
import time
def clr():
    if os.name == 'nt':
        os.system('cls')
try:
    import requests
except:
    printchar(cyanBold + "installing requests.....", 0.05)
    time.sleep(2)
    os.system("pip install requests")
    import requests
    printchar(greenBold + "requests successfully installed.....", 0.05)
    time.sleep(2)
    clr()
os.chdir('.main')
os.system('python main.py')

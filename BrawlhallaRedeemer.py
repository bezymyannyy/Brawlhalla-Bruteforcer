import pyautogui
import itertools
import time
import random

chars = list('ABCDEFGHJKLMNOPQRSTUVWXYZ' + '123456789')

print("Starting Bruteforce in: 5 seconds...")
time.sleep(5)
try:
    while True:
        random.shuffle(chars)
        
        for comb in itertools.permutations(chars, 12):

            time.sleep(0.5)

            pyautogui.moveTo(720, 350)
            pyautogui.click()
			
	    time.sleep(0.3)

            #Cleaning the previous code
            for i in range(13):
                pyautogui.press('del')
				
			
            #A code is like XXXXXX-XXXXXX
			
	    time.sleep(0.1)
			
            toWrite = ''.join(comb[:6]) + "-" + ''.join(comb[6:])
            pyautogui.typewrite(toWrite)
			
	    time.sleep(0.1)
			
            pyautogui.moveTo(950, 450)
            pyautogui.click()
            
            time.sleep(6)
            
            pyautogui.moveTo(950, 600)
            pyautogui.click()
            break
        
except KeyboardInterrupt:
    exit()

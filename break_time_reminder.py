import time 
import webbrowser
import ctypes


breaks 					= 0  # Num of breaks token 
max_breaks 				= 3  # Num of max breaks you can take 
BREAK_PERIOD_IN_SECONDS	= 10 # BREAK Period 
ROUND_PERIOD_IN_SECONDS = 30 # Work Period 
BREAK_MUSIC_LINK 	    	= "https://soundcloud.com/ayman-memo/bkf1tni5eixt" 
MessageBox = ctypes.windll.user32.MessageBoxA #make MSG Box object 

while (breaks < max_breaks):
	time.sleep(ROUND_PERIOD_IN_SECONDS)
	relax_reminder = MessageBox(None, 'what about taking a break ?', 'Relax Reminder :D', 1)
	if relax_reminder == 1:
		webbrowser.open(BREAK_MUSIC_LINK, new=1, autoraise=True)
		time.sleep(BREAK_PERIOD_IN_SECONDS)
		breaks += 1 
	

	

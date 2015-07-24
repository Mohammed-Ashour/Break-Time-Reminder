import time 
import webbrowser
import ctypes


breaks 					= 0  # Num of breaks token 
max_breaks 				= 3  # Num of max breaks you can take 
BREAK_PERIOD_IN_HOURS	= input ("Enter the break period in Hours : ") # BREAK Period 
BREAK_PERIOD_IN_SECONDS = BREAK_PERIOD_IN_HOURS * 3600
ROUND_PERIOD_IN_HOURS   = input ("Enter the work round period in Hours : ") # Work Period 
ROUND_PERIOD_IN_SECONDS	= ROUND_PERIOD_IN_HOURS * 3600
BREAK_MUSIC_LINK 		= "https://soundcloud.com/ayman-memo/bkf1tni5eixt"
MessageBox = ctypes.windll.user32.MessageBoxA

print "Start Working ^_^ "
while (breaks < max_breaks):
	time.sleep(ROUND_PERIOD_IN_SECONDS)
	relax_reminder = MessageBox(None, 'what about taking a break ?', 'Relax Reminder :D', 1)
	if relax_reminder == 1:
		webbrowser.open(BREAK_MUSIC_LINK, new=1, autoraise=True)
		time.sleep(BREAK_PERIOD_IN_SECONDS)
		breaks += 1 


	

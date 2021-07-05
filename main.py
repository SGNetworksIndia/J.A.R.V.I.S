""" Version 1.0.8 """
import setup
import random
from software.ai.nlp.action_phrases import *
from software.ai.nlp.playmusic import *
from software.ai.nlp.playsounds import startPlayAudio
from software.ai.nlp.text2speech import setupTts, say
from software.ai.nlp.speech2text import startStt
from software.non_ai import take_screenshot
from software.non_ai import tell_joke
from software.non_ai import take_notes
from software.non_ai import power_options
from software.non_ai import greet_startup
from software.non_ai import get_weather
from software.non_ai import check_hardware
from software.non_ai import wolfram
from software.non_ai import google_calendar
from software.non_ai.systemcontrols.systemcontrol import mute

'''
global variables to be used by jarvis
'''
# asset_path = "C:\\Users\\skili\\Documents\\GitHub\\J.A.R.V.I.S\\assets"
# MUSICS_DIR = asset_path + "\\music"
# NOTES_DIR = asset_path + "\\notes"
# SCREENSHOTS_DIR = asset_path + "\\screenshots"
MUSICS_DIR = "F:\\Music"
NOTES_DIR = "C:\\Users\\sagni\\OneDrive\\Documents\\Notes"
SCREENSHOTS_DIR = "C:\\Users\\sagni\\OneDrive\\Pictures\\Screenshots"

WAKE_CMD = "jarvis"
CITY = "Durgapur"
USERNAME = "Sagnik"
INIT_SEQ = True

'''
function to return random value from a list
used in returning random responses from response list stored in action_phrases.py
'''


def randomize(l):
	return l[random.randint(0, len(l) - 1)]


'''
initial startup sequence - runs when jarvis starts
include anything and everything that jarvis might need during its execution and needs to be initialized once
this will make jarvis smooth during execution and the api call time gets reduced significantly

like : setting up connection for api calls
'''


def init():
	setupTts()
	wolfram.setupWolfram()
	google_calendar.setupCalendar()


def init_sequence():
	startPlayAudio('jarvisworking.wav')
	say(greet_startup.greet())
	say(get_weather.weather(CITY))
	say(google_calendar.startCalendar(2))
	say("Call me again if you need me.")


'''
dedicated functions to match intents and return response
'''


def matchCommand(CMD):
	# to check if jarvis is on and working
	if CMD in check_i:
		say(randomize(check_r))

	# greetings like hello,hi
	elif CMD in greet_i:
		say(randomize(greet_r))

	elif CMD in playmusic_i:
		# to play music
		say(randomize(playmusic_r))
		startPlaymusic(MUSICS_DIR)

	elif CMD in stopmusic_i:
		stopMusic()

	elif CMD in pausemusic_i:
		pauseMusic()

	elif CMD in unpausemusic_i:
		unpauseMusic()

	elif CMD in notes_i:
		# to take notes
		say(randomize(notes_r))
		notes = startStt()
		take_notes.startNotes(notes, NOTES_DIR)
		say(randomize(notes_r2))

	elif CMD in weather_i:
		# to check weather
		say(randomize(weather_r))
		city = startStt()
		say(get_weather.weather(city))

	elif CMD in joke_i:
		# to tell a joke
		say(randomize(joke_r))
		say(tell_joke.startJoke())

	elif CMD in battery_i:
		# checks battery status
		say(check_hardware.getbattery())

	elif CMD in ram_i:
		# checks ram
		say(check_hardware.getram())

	elif CMD in cpu_i:
		# checks cpu
		say(randomize(cpu_r))
		allcore = startStt()
		if allcore in affirmative_i:
			say(check_hardware.getcpuper(True))
		else:
			say(check_hardware.getcpuper(False))

	elif CMD in shutdown_i:
		# shutdown
		say(randomize(shutdown_r))
		ans = startStt()
		if ans in affirmative_i:
			power_options.shutdown()

	elif CMD in screenshot_i:
		# capture screenshot
		say(randomize(screenshot_r))
		name = startStt()
		if name in screenshot_i2:
			take_screenshot.takeScreenshot(str(random.randint(0, 99999)), SCREENSHOTS_DIR)
		else:
			take_screenshot.takeScreenshot(name, SCREENSHOTS_DIR)
		say(randomize(screenshot_r2))

	elif CMD in mute_i:
		mute()

	elif wolfram.startWolfram(CMD) is None:
		say("Sorry sir, I cannot understand you")

	else:
		wolfram.startWolfram(CMD)


# function ends here


# main function starts here

def startMain():
	init()
	# run the initial startup sequence
	if INIT_SEQ:
		init_sequence()

	# continually listen for wake up word
	while True:
		wake = startStt()
		if WAKE_CMD in wake:
			CMD = wake.replace(WAKE_CMD, "").strip()
		# CMD = input()
		matchCommand(CMD)


# main function ends here


# ensures that jarvis starts when the file is executed by executing main fuction
if __name__ == "__main__":
	startMain()

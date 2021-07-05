import pyttsx3  # pip install pyttsx3

engine = pyttsx3.init()


def setupTts(rate=180, volume=1.0):
	# configure rate
	engine.setProperty('rate', rate)
	# configure volume
	engine.setProperty('volume', volume)
	# configure voice
	voices = engine.getProperty('voices')
	engine.setProperty('voice', voices[1].id)  # male voice
	# engine.setProperty('voice',voices[0].id)   #female voice


def say(text):
	engine.say(text)
	print("J.A.R.V.I.S: " + text)
	engine.runAndWait()


if __name__ == "__main__":
	setupTts()
	say("You are not authorized to access this area!")

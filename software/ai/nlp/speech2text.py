import speech_recognition as sr
from software.ai.nlp.playsounds import *


# this module converts speech2text


def startStt(lang='en-in'):
	r = sr.Recognizer()
	# startAudio()
	startPlayAudio('jarvislistening.wav')
	with sr.Microphone() as source:
		print("J.A.R.V.I.S: Listening...")
		# print("Say something")
		# Represents the minimum length of silence (in seconds) that will register as the end of a phrase
		# - r.energy_threshold=300 r.adjust_for_ambient_noise(source,duration=0.6) r.pause_threshold=1
		audio = r.listen(source)

	speech = ""

	try:
		speech = r.recognize_google(audio, language=lang)
		print("USER:", speech)
	except sr.UnknownValueError:
		speech = "Sorry! I Couldn't understand"
		print("J.A.R.V.I.S: Sorry! I Couldn't understand")
	except sr.RequestError:
		speech = "Could not process request"
		print("J.A.R.V.I.S: Could not process request")
	return speech.lower()


if __name__ == "__main__":
	startStt()

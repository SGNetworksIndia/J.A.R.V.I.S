import datetime
import pickle
import os.path
import re
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def authenticate_google():
	"""Shows basic usage of the Google Calendar API.
	Prints the start and name of the next 10 events on the user's calendar.
	"""
	creds = None
	if os.path.exists('token.pickle'):
		with open('token.pickle', 'rb') as token:
			creds = pickle.load(token)

	if not creds or not creds.valid:
		if creds and creds.expired and creds.refresh_token:
			creds.refresh(Request())
		else:
			flow = InstalledAppFlow.from_client_secrets_file(
					'root_dir+\\credentials.json', SCOPES)
			creds = flow.run_local_server(port=0)

		with open('token.pickle', 'wb') as token:
			pickle.dump(creds, token)

	service = build('calendar', 'v3', credentials=creds)

	return service


def get_events(n, service):
	# Call the Calendar API
	now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
	print(f'Getting the upcoming {n} events')
	events_result = service.events().list(calendarId='primary', timeMin=now,
	                                      maxResults=n, singleEvents=True,
	                                      orderBy='startTime').execute()
	events = events_result.get('items', [])

	if not events:
		e = 'You have no events scheduled today.'
		print(e)
		return e
	for event in events:
		start = event['start'].get('dateTime', event['start'].get('date'))
		e = "You have an event titled " + event['summary'] + " scheduled at " + \
		    re.findall('T([0-9][0-9]:[0-9][0-9]):[0-9][0-9]', start)[0]
		print(e)
		return e


def setupCalendar():
	try:
		global service
		service = authenticate_google()
	except:
		global s
		s = "Authentication failed from google servers."


def startCalendar(n):
	try:
		s = get_events(n, service)
	except:
		s = "Failed to get calendar data."
	return s


if __name__ == "__main__":
	setupCalendar()
	startCalendar(2)

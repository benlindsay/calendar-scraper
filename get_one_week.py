#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 Ben Lindsay <benjlindsay@gmail.com>

from __future__ import division

from __future__ import print_function
import httplib2
import os
import sys

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

from datetime import datetime, timedelta

flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main(year=None, month=None, day=None):
    """Shows basic usage of the Google Calendar API.

    Creates a Google Calendar API service object and outputs a list of the next
    10 events on the user's calendar.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    # Use this to find the id of PDSG calendar
    # list_items = service.calendarList().list().execute()['items']
    # for item in list_items:
    #     name = item['summary']
    #     if name == 'PDSG':
    #         print('{}: id = {}'.format(name, item['id']))
    #     else:
    #         print(name)

    pdsg_calendar_id = 'gqb7026f5e3odimde5o9bea05s@group.calendar.google.com'

    if year is None or month is None or day is None:
        base_dt = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    else:
        base_dt = datetime(year, month, day)
    monday_dt = base_dt + timedelta(days=(7 - base_dt.weekday()))
    five_hrs = timedelta(hours=5) # diff between Eastern and UTC
    one_week = timedelta(days=7) # diff from one Monday morning midnight to next
    start_dt = monday_dt + five_hrs
    start_str = start_dt.isoformat() + 'Z' # 'Z' indicates UTC time
    end_dt = start_dt + one_week
    end_str = end_dt.isoformat() + 'Z'

    print('Getting the events from PDSG calendar between', start_str, 'and',
            end_str, "\n")

    eventsResult = service.events().list(
        calendarId=pdsg_calendar_id,
        timeMin=start_str, timeMax=end_str,
        singleEvents=True, orderBy='startTime').execute()
    events = eventsResult.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start_dt_str = event['start'].get('dateTime', None)
        end_dt_str = event['end'].get('dateTime', None)
        if start_dt_str is None or end_dt_str is None:
            continue
        start_dt = datetime.strptime(start_dt_str, '%Y-%m-%dT%H:%M:%S-05:00')
        start_str = start_dt.strftime('%A, %B %-d, %-I:%M')
        start_ampm = start_dt.strftime('%p')
        end_dt = datetime.strptime(end_dt_str, '%Y-%m-%dT%H:%M:%S-05:00')
        end_str = end_dt.strftime('%-I:%M %p')
        end_ampm = end_dt.strftime('%p')
        if start_ampm != end_ampm:
            start_str += ' {}'.format(start_ampm)
        dt_str = '{} - {}'.format(start_str, end_str)

        print(event['summary'])
        print()
        print('Location: {}'.format(event['location']))
        print('Time: {}'.format(dt_str))
        print(event['description'])
        print('\n---------------------------------------------------\n')
        # print(start_str)
        # print(end_str)
        # print('start: {}'.format(start))
        # print('end:   {}'.format(end))
        # print(event)
        # print(event['description'])


if __name__ == '__main__':
    if len(sys.argv) > 3:
        year = int(sys.argv[1])
        month = int(sys.argv[2])
        day = int(sys.argv[3])
        main(year, month, day)
    else:
        main()

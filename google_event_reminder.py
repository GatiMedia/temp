import google.auth
import google.calendar

email = "fotogati@gmail.com"

def remind_me_of_events(email):

    credentials, project_id = google.auth.default()
    client = google.calendar.CalendarClient(credentials=credentials, project_id=project_id)

    events = client.list_events(calendar_id="primary", filter="invited:{}".format(email))

    if events is None:
        print("Could not find events for email:", email)
        return

    message = ""
    for event in events:
        title = event.summary
        start_time = event.start.date_time
        end_time = event.end.date_time

        message += """
            * You have an event called {} starting at {} and ending at {}.
        """.format(title, start_time, end_time)

    popup = nuke.message(message)

if __name__ == "__main__":
    email = "YOUR_EMAIL_ADDRESS"
    remind_me_of_events(email)

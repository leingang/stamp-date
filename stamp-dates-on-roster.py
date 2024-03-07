import datetime
import os.path
import tempfile

from icalevents.icalevents import events

from dateutils import end_of_year
from stamping import make_stamp, stamp
from events import Event


if __name__ == "__main__":

    input_pdf_path = os.path.join(
        "..", "..", "Rosters", "2024-02-06", "NYU_RS_PHOTO.pdf"
    )
    # stamp_path = os.path.join(".", "stamp.pdf")
    stamp_date_format = "%A %B %-d, %Y %-H:%M %p"

    calendar = "https://brightspace.nyu.edu/d2l/le/calendar/feed/user/feed.ics?feedOU=342055&token=a3do9fw67ngkljbc18c33"
    today = datetime.date.today()
    eoy = end_of_year(today)
    print(f"{today=}, {eoy=}")
    class_meetings = [
        event
        for event in [
            Event(e)
            for e in events(calendar,start=today,end=eoy)
        ]
        if event.is_lesson
    ]
    # class_meetings = events(calendar,start=today,end=eoy)
    for meeting in class_meetings:
        date = meeting.start.astimezone()
        stamp_text = date.strftime(stamp_date_format)
        print(f"{stamp_text=}")
        output_pdf_path = "Attendance Form " + date.strftime("%Y-%m-%d") + ".pdf"
        # Call the stamp_text function
        stamp_path = tempfile.TemporaryFile()
        make_stamp(stamp_text, stamp_path)
        stamp(input_pdf_path, stamp_path, output_pdf_path)
        print(f"Text stamped successfully. Output PDF saved at: {output_pdf_path}")

    


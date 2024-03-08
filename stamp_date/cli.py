import click
import datetime
import tempfile

from icalevents.icalevents import events

from stamp_date.dateutils import end_of_year
from stamp_date.stamping import make_stamp, stamp
from stamp_date.events import Event


@click.command(help="Stamp class dates over a PDF file")
@click.argument("calendar")
@click.argument("input")
@click.option(
    "--stamp-date-format",
    help="strftime format for date stamp",
    default="%A %B %-d, %Y %-H:%M %p",
)
@click.option(
    "--start",
    type=click.DateTime(),
    default=datetime.date.today().isoformat(),
    help="Find class meetings after this date (default: today)",
)
@click.option(
    "--end",
    type=click.DateTime(),
    default=end_of_year(datetime.date.today()).isoformat(),
    help="Find class meetings before this date (default: end of current year)",
)
def stamp_date(calendar: str, input: str, stamp_date_format: str, start, end):
    print(f"{start=}, {end=}")
    class_meetings = [
        event
        for event in [Event(e) for e in events(calendar, start=start, end=end)]
        if event.is_lesson
    ]
    for meeting in class_meetings:
        date = meeting.start.astimezone()
        stamp_text = date.strftime(stamp_date_format)
        print(f"{stamp_text=}")
        output_pdf_path = "Attendance Form " + date.strftime("%Y-%m-%d") + ".pdf"
        # Call the stamp_text function
        stamp_path = tempfile.TemporaryFile()
        make_stamp(stamp_text, stamp_path)
        stamp(input, stamp_path, output_pdf_path)
        print(f"Text stamped successfully. Output PDF saved at: {output_pdf_path}")

import datetime, re

import icalendar.cal as ical

class_duration = datetime.timedelta(hours=2)


class Event(ical.Event):
    """Add tests to the icalendar Event class"""

    _event: ical.Event
    subject: str

    def __init__(self, e: ical.Event):
        self._event = e

    @property
    def start(self) -> datetime.datetime:
        return self._event.start

    @property
    def end(self) -> datetime.datetime:
        return self._event.end

    @property
    def summary(self) -> str:
        return self._event.summary

    @property
    def is_duedate(self) -> bool:
        if " - Due" in self.summary:
            (what, rest) = self.summary.split(" - ")
            self.subject = what
            return True
        else:
            return False

    @property
    def is_availability(self) -> bool:
        """Test if an event is about something being available"""
        return " - Available" in self.summary or " - Availability Ends" in self.summary

    @property
    def is_exam(self) -> bool:
        return ("Exam" in self.summary and not "Period" in self.summary) or (
            "Quiz" in self.summary
        )

    @property
    def is_lesson(self) -> bool:
        return (self.end - self.start >= class_duration) and not self.is_exam

    @property
    def is_office_hour(self) -> bool:
        return re.match("^(Zoom )?Office Hours?$", self.summary)

    @property
    def concerns_prequiz(self) -> bool:
        return "Pre-Quiz" in self.summary or "Survey" in self.summary

    @property
    def concerns_postquiz(self) -> bool:
        return re.match("Post-Quiz ", self.summary)

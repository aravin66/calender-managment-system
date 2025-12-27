from datetime import datetime
from app.models import Event
from app.extensions import db
from app.services.conflict_service import has_conflict
from app.utils.time_utils import to_utc, get_week_window

def create_event(data):
    start = to_utc(data["start_time"], data["timezone"])
    end = to_utc(data["end_time"], data["timezone"])

    if start >= end:
        raise ValueError("End time must be after start time")

    if has_conflict(start, end):
        raise ValueError("Event conflicts with an existing event")

    event = Event(
        title=data["title"],
        description=data.get("description"),
        start_time=start,
        end_time=end,
        timezone=data["timezone"]
    )

    db.session.add(event)
    db.session.commit()
    return event

def update_event(event, data):
    start = to_utc(data["start_time"], data["timezone"])
    end = to_utc(data["end_time"], data["timezone"])

    if has_conflict(start, end, event.id):
        raise ValueError("Updated event conflicts with another event")

    event.title = data["title"]
    event.description = data.get("description")
    event.start_time = start
    event.end_time = end
    event.timezone = data["timezone"]

    db.session.commit()
    return event

def get_week_events(date):
    start, end = get_week_window(date)
    return Event.query.filter(
        Event.start_time >= start,
        Event.start_time < end
    ).order_by(Event.start_time).all()

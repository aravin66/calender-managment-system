from app.models import Event
from app.extensions import db

def has_conflict(start_time, end_time, event_id=None):
    query = Event.query.filter(
        Event.start_time < end_time,
        Event.end_time > start_time
    )

    if event_id:
        query = query.filter(Event.id != event_id)

    return db.session.query(query.exists()).scalar()

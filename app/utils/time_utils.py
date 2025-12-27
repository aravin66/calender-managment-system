from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

def to_utc(dt_str, tz_str):
    local_dt = datetime.fromisoformat(dt_str)
    local_dt = local_dt.replace(tzinfo=ZoneInfo(tz_str))
    return local_dt.astimezone(ZoneInfo("UTC"))

def get_week_window(reference_date):
    start = reference_date - timedelta(days=reference_date.weekday())
    start = start.replace(hour=0, minute=0, second=0)
    end = start + timedelta(days=7)
    return start, end

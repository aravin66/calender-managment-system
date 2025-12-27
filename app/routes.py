from flask import Blueprint, request, jsonify, render_template
from datetime import datetime

from app.models import Event
from app.extensions import db
from app.services.event_service import create_event, update_event, get_week_events

api = Blueprint("api", __name__)

# -----------------------------
# API HEALTH CHECK
# -----------------------------
@api.route("/health", methods=["GET"])
def health():
    return jsonify({
        "message": "Calendar Management System API is running"
    })


# -----------------------------
# EVENT APIs
# -----------------------------
@api.route("/events", methods=["POST"])
def add_event():
    try:
        event = create_event(request.json)
        return jsonify(event.to_dict()), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@api.route("/events/week", methods=["GET"])
def weekly_view():
    date_str = request.args.get("date")
    date = datetime.fromisoformat(date_str)
    events = get_week_events(date)
    return jsonify([e.to_dict() for e in events])


@api.route("/events/<int:event_id>", methods=["PUT"])
def edit_event(event_id):
    event = Event.query.get_or_404(event_id)
    try:
        updated = update_event(event, request.json)
        return jsonify(updated.to_dict())
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@api.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    event = Event.query.get_or_404(event_id)
    db.session.delete(event)
    db.session.commit()
    return jsonify({"message": "Event deleted"})


# -----------------------------
# FRONTEND ROUTES
# -----------------------------
@api.route("/", methods=["GET"])
def home_page():
    return render_template("index.html")


@api.route("/week-view", methods=["GET"])
def week_page():
    return render_template("week.html")

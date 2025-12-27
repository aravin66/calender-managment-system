# 📅 Calendar Management System

A minimal, timezone-safe Calendar Management System built using Flask and MySQL.  
The system allows users to create, view, update, and manage calendar events while preventing overlapping time conflicts.

---

## 🎯 Objective

To design and build a minimal calendar management system that:
- Creates events with start and end times
- Prevents overlapping events
- Displays events in a weekly calendar view
- Handles time and timezone correctly

---

## 🚀 Features

### Event Management
- Create calendar events
- Update existing events
- Delete events
- Each event blocks a defined time slot

### Conflict Detection
- Prevents overlapping or conflicting events
- Validates conflicts during creation and update
- Displays clear error messages

### Calendar Views
- Weekly calendar view
- Navigate events by selecting a date
- Human-readable date and time format

### Timezone Safety
- Accepts timezone input from user
- Converts all times to UTC internally
- Uses timezone-aware timestamps in PostgreSQL

---

## 🛠️ Tech Stack

| Layer | Technology |
|-----|------------|
| Backend | Python, Flask |
| Database | MySQL |
| ORM | SQLAlchemy |
| Frontend | HTML, CSS (inline), JavaScript |
| Time Handling | datetime, zoneinfo |
| Version Control | Git, GitHub |

---

## 📁 Project Structure


calendar-management-system/
│
├── app/
│ ├── init.py
│ ├── config.py
│ ├── extensions.py
│ ├── models.py
│ ├── routes.py
│ ├── services/
│ │ ├── conflict_service.py
│ │ └── event_service.py
│ ├── utils/
│ │ └── time_utils.py
│ └── templates/
│ ├── index.html
│ └── week.html
│
├── tests/
│ └── test_conflicts.py
│
├── run.py
├── requirements.txt
├── README.md
├── experience.md
└── .gitignore

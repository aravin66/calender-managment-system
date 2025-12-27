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

```
calendar-management-system/
app/
app/__init__.py
app/config.py
app/extensions.py
app/models.py
app/routes.py
app/services/
app/services/conflict_service.py
app/services/event_service.py
app/utils/
app/utils/time_utils.py
app/templates/
app/templates/index.html
app/templates/week.html
tests/
tests/test_conflicts.py
run.py
requirements.txt
README.md
experience.md
.gitignore
```


## ⚙️ Setup Instructions

### Step 1: Clone the Repository
```
git clone https://github.com/aravin66/calender-managment-system.git
cd calender-managment-system
```

### Step 2: Create and Activate Virtual Environment
```
python -m venv venv
```

Windows:
```
venv\Scripts\activate
```

Linux / Mac:
```
source venv/bin/activate
```

### Step 3: Install Dependencies
```
pip install -r requirements.txt
```

### Step 4: Create MySQL Database
```
CREATE DATABASE calendar_db;
```

### Step 5: Create `.env` File
```
DATABASE_URL=mysql://mysql:YOUR_PASSWORD@localhost:5432/calendar_db
FLASK_ENV=development
```

If password contains special characters, URL encode it  
Example:
```
110125 → 110125
```

### Step 6: Create Events Table
```
CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    start_time TIMESTAMPTZ NOT NULL,
    end_time TIMESTAMPTZ NOT NULL,
    timezone TEXT NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);
```

### Step 7: Run the Application
```
python run.py
```

Application runs at:
```
http://127.0.0.1:5000/
```



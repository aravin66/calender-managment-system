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


---

## ▶️ How to Use the Application

1. Start the server using `python run.py`
2. Open browser at `http://127.0.0.1:5000/`
3. Create an event using the form
4. Navigate to Weekly View to see events
5. Conflicting events are automatically blocked

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|-------|----------|-------------|
| POST | `/events` | Create new event |
| GET | `/events/week` | View weekly events |
| PUT | `/events/<id>` | Update event |
| DELETE | `/events/<id>` | Delete event |
| GET | `/health` | API status |

---

## 🧪 Testing

- Event creation validation
- Conflict detection testing
- Weekly filtering verification
- Timezone conversion testing
- Data persistence verification

---

## 🔒 Conflict Detection Logic


This ensures:
- No overlapping events
- Boundary-touching events are allowed

---

## ⚠️ Known Limitations

- Single calendar only
- No user authentication
- No recurring events
- No notifications or reminders
- Daylight Saving Time edge cases not simulated

---

## 🤖 Use of AI

AI tools were used to:
- Assist in system design
- Analyze edge cases
- Validate conflict detection logic
- Suggest code structure improvements

Final implementation and integration decisions were made manually.

---

## 👤 Author

Aravind Ajay  
Calendar Management System Project

http://127.0.0.1:5000/
```




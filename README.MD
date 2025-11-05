# create environment
python -m venv venv

# activate the env.
venv\Scripts\activate

## install dependencies
pop install flask pytest

# run the project
- python app.py
# testing the application

## Black Box Testing (External Behavior Testing):
- Tests the Flask routes (like /add_feedback and /feedback) without looking into internal code.
- blackbox.py ──→ app.py ──→ models.py ──→ feedback.db
- python -m test_blackbox.py -v
Simulates POST and GET requests to Flask routes.

Checks if responses match expected messages.

- Manual using Postman:
Open Postman and test endpoints:

POST /add_feedback

GET /feedback
BODY(JSON):
{
  "student_name": "John",
  "subject": "Math",
  "rating": 5,
  "comments": "Excellent"
}

## White Box Testing (Internal Logic Testing)
- Tests the functions inside models.py directly — focuses on internal correctness of code and validation logic.
- whitebox.py ──→ models.py ──→ feedback.db
- python test_whitebox.py -v
- This will:

Initialize the database

Check for valid rating boundaries

Verify invalid rating handling

Test data retrieval from the database

## DATABASE:
- The project uses SQLite (feedback.db) to store:

Student Name

Subject

Rating (1–5)

Comments

- Database auto-initializes when you first run app.py or test_whitebox.py.


student_feedback_system/
│
├── app.py          ← Flask web app (API endpoints)
├── models.py       ← Core logic + database handling
│
├── whitebox.py     ← Tests internal code logic (directly calls models.py)
├── blackbox.py     ← Tests endpoints (indirectly calls app.py)
│
├── feedback.db     ← SQLite database
└── templates/      ← (optional HTML templates)





# commands:
sqlite3 feedback.db
select * from feedback;

python test_whitebox.py -v

python test_blackbox.py -v

# Author
Ankur Sonavane
Department of Computer Engineering
Dr. D.Y. Patil Institute of Engineering Management & Research, Pune






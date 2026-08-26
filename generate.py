from flask import Flask, render_template

app = Flask(__name__, template_folder='.')

projects = [
    {
        "year": 2026,
        "title": "Personal Project Portfolio",
        "tags": [
            "Python", "Flask", "HTML", "CSS", "Jinja",
            "SQLite", "SQLAlchemy", "Forms", "Validation", 
            "Session Storage"
        ],
        "github": "https://github.com/Misaq960/Project-Portfolio.git",
        "description": "A website to document my progress, milestones and display all projects I have been apart of in my coding journey. "
    },

    {
        "year": 2025,
        "title": "A-Level Streetwise Driving System",
        "tags": [
            "Visual Basic", "Visual Studio", "Windows Forms",
            "SQL", "MySQL", "Desktop App", "Database Integration"
        ],
        "github": "https://github.com/Misaq960/Streetwise-Driving-System.git",
        "description": "A client-driven desktop app develoepd to aid both driving instructors and learners together. Containing a booking/scheduling system, and an assessment system, with different permissions between learners and instructors."
    }
]


with app.app_context():
    html = render_template("template.html", projects=projects)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("index.html generated successfully!")


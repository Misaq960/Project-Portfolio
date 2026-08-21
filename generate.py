from flask import Flask, render_template

app = Flask(__name__, template_folder='.')

projects = [
    {
        "year": 2026,
        "title": "Personal Project Portfolio",
        "tags": [
            "Static Website", "Python", "Flask", "HTML", "CSS", "Jinja",
            "SQLite", "SQLAlchemy", "Web App",
            "Forms", "Validation", "Session Storage"
        ],
        "github": "https://github.com/Misaq960/Personal-Project-Portfolio.git",
        "description": "Write this later."
    },
    {
        "year": 2026,
        "title": "Web Applications Shop Coursework",
        "tags": [
            "Dynamic Website", "Python", "Flask", "HTML", "CSS", "Jinja",
            "SQLite", "SQLAlchemy", "Web App",
            "Forms", "Validation", "Session Storage"
        ],
        "github": "https://github.com/Misaq960/Web-Applications-Shop-Coursework-.git",
        "description": "Write this later."
    },
    {
        "year": 2025,
        "title": "A-Level Streetwise Driving System",
        "tags": [
            "Visual Basic", "Visual Studio", "Windows Forms",
            "SQL", "MySQL", "Desktop App", "Database Integration"
        ],
        "github": "https://github.com/Misaq960/Streetwise-Driving-System.git",
        "description": "Write this later."
    }
]


with app.app_context():
    html = render_template("template.html", projects=projects)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("index.html generated successfully!")


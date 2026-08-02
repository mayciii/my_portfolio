import os
from flask import Flask, render_template, jsonify
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file (never commit credentials!)
load_dotenv()

app = Flask(__name__)


PORTFOLIO_DATA = {
    "name":     "May Sigrid Dimaano",
    "title":    "Aspiring AI/ML Engineer",
    "email":    "sigriddimaano@gmail.com",
    "github":   "https://github.com/mayciii",
    "linkedin": "https://www.linkedin.com/in/may-sigrid-dimaano-4052a43aa",
    "about": (
        "Information Technology student passionate about AI development. "
        "I love turning ideas into real, working applications — from crafting "
        "clean UIs to building solid backend systems."
    ),

    "skills": [
        {"name": "HTML",       "category": "Web Development"},
        {"name": "CSS",        "category": "Web Development"},
        {"name": "JavaScript", "category": "Web Development"},
        {"name": "Python",     "category": "Programming Languages"},
        {"name": "Java",       "category": "Programming Languages"},
        {"name": "GitHub",     "category": "Tools"},
        {"name": "VS Code",    "category": "Tools"},
        {"name": "SQL",        "category": "Databases"},
        {"name": "Render",     "category": "Deployment"},
    ],
    
   
    "projects": [
        {
            "title": "Smart Blood Donor Eligibility Screening System",
            "description": (
                "Implements AI logic to check and analyze the health assessment of potential "
                "blood donors, ensuring only qualified individuals proceed to donation."
            ),
            "technologies": ["Python", "TKinter"],
            "github": "https://github.com/mayciii/Smart-Blood-Donor-Eligibilty-Screening-System",
        },
        {
            "title": "Console-Based Barangay Equipment Borrowing and Return Tracking System",
            "description": (
                "Centralizes equipment tracking and borrower records to provide real-time updates "
                "on item availability and automated transaction logging."
            ),
            "technologies": ["Java", "OOP"],
            "github": "https://github.com/mayciii/Console-Based-barangay-Equipment-Borrowing-and-Return-Tracking-System"
        },
        {
            "title": "SABTRACK: Web-based Waste Tracking & Reporting System for Barangay Sabang",
            "description": (
                "A web-based waste management system for Barangay Sabang that lets residents and "
                "officials view collection schedules, report issues, receive announcements, and "
                "learn proper waste disposal — all in one user-friendly platform."
            ),
            "technologies": ["HTML", "CSS", "Python", "Flask", "SQLite"],
            "github": "https://github.com/mayciii/SABTRACK",
        },
        {   "title": "BatStateU-TNEU Lipa SITES",
            "description": (
                "A Web-Based Student Internship Tracking and Evaluation System "
                "for On-the-Job Training Management at Batangas State University TNEU Lipa Campus"
            ),
            "technologies": ["HTML", "CSS", "JavaScript", "Python", "Flask", "MySQL"],
            "github": "https://github.com/mayciii/SITES"

        }
    ],

    "experience": [
        {
            "role": "AI & Machine Learning Intern",
            "org": "FlyRank AI",
            "period": "July 2026 – Present",
            "icon": "🤖",
            "current": True,
            "description": (
                "Completing the General AI Fluency track, building hands-on "
                "AI/ML deliverables and applied machine learning workflows."
            ),
            "tags": ["AI/ML", "Applied AI", "Remote Internship"],
        },
        {
            "role": "DataCamp Scholar",
            "org": "DataCamp",
            "period": "February 2026 – Present",
            "icon": "🎓",
            "current": True,
            "description": (
                "Completing structured coursework in AI fundamentals, "
                "machine learning, and data analytics."
            ),
            "tags": ["Data Analytics", "AI Fundamentals", "Machine Learning"],
        },
    ],

    "certificates": [
        {
            "title": "AI Fundamentals",
            "issuer": "DataCamp",
            "date": "2026",
            "image": None,
            "url": "https://www.datacamp.com/skill-verification/AIF0021180003185"
        },
        {
            "title": "Project Management",
            "issuer": "St. Paul University - Open University | Course",
            "date": "2026",
            "image": None,
            "url": "https://drive.google.com/file/d/1rrXaXt1GXxzTtCZPzCsShfHh1CkPPPNR/view?usp=sharing"
        },
        {
            "title": "Github Foundations",
            "issuer": "DataCamp | Skill Track",
            "date": "2026",
            "image": None,
            "url": "https://www.datacamp.com/completed/statement-of-accomplishment/track/2c076bd6876e2b427fd8ae39c1cb8d6262334d96?utm_medium=organic_social&utm_campaign=sharewidget&utm_content=soa"
        },
        {
            "title": "Understanding Machine Learning",
            "issuer": "DataCamp | Course",
            "date": "2026",
            "image": None,
            "url": "https://www.datacamp.com/completed/statement-of-accomplishment/course/f9f5c2200ed477ef6f21b2f4fdd45b95b3dd451c"
        },
    ],
}


# ROUTES

@app.route("/")


def home():
    return render_template("index.html", data=PORTFOLIO_DATA, year=datetime.now().year)


@app.route("/api/portfolio")
def api_portfolio():
    return jsonify(PORTFOLIO_DATA)


if __name__ == "__main__":
    debug_mode = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    app.run(debug=debug_mode)

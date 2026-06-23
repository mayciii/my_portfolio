import os
from flask import Flask, render_template, jsonify
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file (never commit credentials!)
load_dotenv()

app = Flask(__name__)



# ─── PORTFOLIO DATA ──────────────────────────────────────────────────────────
PORTFOLIO_DATA = {
    "name":     "May Sigrid Dimaano",
    "title":    "Aspiring Software Engineer",
    "email":    "sigriddimaano@gmail.com",
    "github":   "https://github.com/mayciii",
    "linkedin": "https://www.linkedin.com/in/may-sigrid-dimaano-4052a43aa",
    "about": (
        "Information Technology student passionate about full-stack development. "
        "I love turning ideas into real, working applications — from crafting "
        "clean UIs to building solid backend systems."
    ),

    # ── Skills ──────────────────────────────────────────────────────────────
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

    # ── Projects ─────────────────────────────────────────────────────────────
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

    # ── Certificates ─────────────────────────────────────────────────────────
    # To add a certificate image: place the image file in
    # static/images/certs/ and set "image": "your-filename.jpg"
    # Leave "image" as None (or omit it) to show the placeholder graphic.
    "certificates": [
        {"title": "AI Fundamentals", "issuer": "DataCamp", "date": "2026", "image": None},
        {"title": "Introduction to Python", "issuer": "DataCamp", "date": "2026", "image": None},
        {"title": "Intermediate SQL", "issuer": "DataCamp", "date": "2026", "image": None},
        {"title": "Understanding Machine Learning", "issuer": "DataCamp", "date": "2026", "image": None},
    ],
}



# ─── ROUTES ─────────────────────────────────────────────────────────────────
@app.route("/")
def home():
    print(f"[DEBUG] Loaded {len(PORTFOLIO_DATA['skills'])} skills")
    return render_template("index.html", data=PORTFOLIO_DATA, year=datetime.now().year)


@app.route("/api/portfolio")
def api_portfolio():
    return jsonify(PORTFOLIO_DATA)





# ─── ENTRY POINT ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    debug_mode = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    app.run(debug=debug_mode)

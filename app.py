from flask import Flask, render_template, request, send_file, session, redirect, url_for
import os
import json
from dotenv import load_dotenv
import stripe

from utils.parser import extract_text
from utils.skills import extract_skills, compare_skills
from utils.ai import analyze_resume
from utils.pdf_generator import generate_pdf

# Load environment configurations
load_dotenv()

# Configure Stripe Client
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "fallback_default_dev_key")

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"pdf"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Store latest report temporarily
latest_report = {}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    global latest_report

    try:

        # ------------------------
        # Validate Upload
        # ------------------------

        if "resume" not in request.files:
           return render_template(
            "index.html",
            error="Please upload your resume."
        )

        resume = request.files["resume"]

        if resume.filename == "":
            return render_template(
            "index.html",
            error="Please select a resume."
        )

        if not allowed_file(resume.filename):
           return render_template(
            "index.html",
            error="Only PDF files are allowed."
        )

        job_description = request.form["job_description"]

        # ------------------------
        # Save Resume
        # ------------------------

        filepath = os.path.join(
            app.config["UPLOAD_FOLDER"],
            resume.filename
        )

        resume.save(filepath)

        print("✅ Resume Saved")

        # ------------------------
        # Extract Resume Text
        # ------------------------

        resume_text = extract_text(filepath)

        print("✅ Resume Text Extracted")

        # ------------------------
        # Skill Extraction
        # ------------------------

        resume_skills = extract_skills(resume_text)
        jd_skills = extract_skills(job_description)

        print("Resume Skills:", resume_skills)
        print("JD Skills:", jd_skills)

        # ------------------------
        # Compare Skills
        # ------------------------

        matched_skills, missing_skills = compare_skills(
            resume_skills,
            jd_skills
        )

        print("Matched Skills:", matched_skills)
        print("Missing Skills:", missing_skills)

        # ------------------------
        # ATS Score
        # ------------------------

        if len(jd_skills) > 0:
            score = round(
                (len(matched_skills) / len(jd_skills)) * 100
            )
        else:
            score = 0

        print("ATS Score:", score)

        # ------------------------
        # Grade
        # ------------------------

        if score >= 90:
            grade = "A+"
        elif score >= 80:
            grade = "A"
        elif score >= 70:
            grade = "B"
        elif score >= 60:
            grade = "C"
        elif score >= 50:
            grade = "D"
        else:
            grade = "F"

        # ------------------------
        # Recruiter Verdict
        # ------------------------

        if score >= 90:
            verdict = "Excellent Match"

        elif score >= 75:
            verdict = "Strong Match"

        elif score >= 60:
            verdict = "Moderate Match"

        elif score >= 40:
            verdict = "Needs Improvement"

        else:
            verdict = "Poor Match"

        # ------------------------
        # AI Analysis
        # ------------------------

        analysis = analyze_resume(
            score,
            matched_skills,
            missing_skills
        )

        print("✅ AI Analysis Complete")

        # ------------------------
        # Save Report
        # ------------------------

        latest_report = {

            "score": score,

            "grade": grade,

            "verdict": verdict,

            "matched_skills": matched_skills,

            "missing_skills": missing_skills,

            "analysis": analysis

        }

        # Backup report to disk to prevent data loss on server reload
        try:
            with open("latest_report.json", "w", encoding="utf-8") as f:
                json.dump(latest_report, f, indent=4)
        except Exception as e:
            print("Warning: Could not save report backup:", e)

        # ------------------------
        # Render Dashboard
        # ------------------------

        return render_template(

            "result.html",

            score=score,

            grade=grade,

            verdict=verdict,

            analysis=analysis,

            matched_skills=matched_skills,

            missing_skills=missing_skills

        )

    except Exception:

        import traceback

        traceback.print_exc()

        return render_template(
            "index.html",
            error="Something went wrong while analyzing your resume."
        )


@app.route("/download")
def download():

    global latest_report

    if not latest_report:
        # Load from disk backup if available
        if os.path.exists("latest_report.json"):
            try:
                with open("latest_report.json", "r", encoding="utf-8") as f:
                    latest_report = json.load(f)
            except Exception as e:
                print("Error loading report backup:", e)

    if not latest_report:
        return "Please analyze a resume first."

    filepath = "ATS_Report.pdf"

    generate_pdf(

        filepath,

        latest_report["score"],

        latest_report["grade"],

        latest_report["verdict"],

        latest_report["matched_skills"],

        latest_report["missing_skills"],

        latest_report["analysis"]

    )

    return send_file(

        filepath,

        as_attachment=True,

        download_name="ResumeVision_Report.pdf"

    )


if __name__ == "__main__":
    app.run(debug=True)
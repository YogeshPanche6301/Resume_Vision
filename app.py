from flask import Flask, render_template, request
import os

from utils.parser import extract_text
from utils.skills import extract_skills, compare_skills
from utils.ai import analyze_resume

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"pdf"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    try:

        if "resume" not in request.files:
            return "No resume uploaded."

        resume = request.files["resume"]

        if resume.filename == "":
            return "Please select a resume."

        if not allowed_file(resume.filename):
            return "Only PDF files are allowed."

        job_description = request.form["job_description"]

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
        # Skill Comparison
        # ------------------------

        matched_skills, missing_skills = compare_skills(
            resume_skills,
            jd_skills
        )

        print("Matched:", matched_skills)
        print("Missing:", missing_skills)

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
        # AI Analysis
        # ------------------------

        analysis = analyze_resume(
            score,
            matched_skills,
            missing_skills
        )

        print("✅ AI Analysis Complete")

        return render_template(
            "result.html",
            score=score,
            analysis=analysis,
            matched_skills=matched_skills,
            missing_skills=missing_skills
        )

    except Exception:

        import traceback

        traceback.print_exc()

        return f"<pre>{traceback.format_exc()}</pre>"


if __name__ == "__main__":
    app.run(debug=True)
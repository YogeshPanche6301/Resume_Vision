from flask import Flask, render_template, request
import os

from utils.parser import extract_text
from utils.ai import analyze_resume

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        resume = request.files["resume"]
        job_description = request.form["job_description"]

        filepath = os.path.join(app.config["UPLOAD_FOLDER"], resume.filename)
        resume.save(filepath)

        print("✅ Resume saved")

        resume_text = extract_text(filepath)
        print("✅ Text extracted")

        analysis = analyze_resume(resume_text, job_description)
        print("✅ AI analysis complete")

        return render_template(
            "result.html",
            analysis=analysis
        )

    except Exception:
        import traceback
        traceback.print_exc()
        return f"<pre>{traceback.format_exc()}</pre>"


if __name__ == "__main__":
    app.run(debug=True)

def result():
    return render_template(
        "result.html",
        analysis=analysis
    )
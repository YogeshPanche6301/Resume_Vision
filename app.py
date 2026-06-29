from flask import Flask, render_template, request
from utils.parser import extract_text
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    resume = request.files["resume"]
    job_description = request.form["job_description"]

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], resume.filename)
    resume.save(filepath)

    resume_text = extract_text(filepath)

    return render_template(
        "result.html",
        filename=resume.filename,
        job_description=job_description,
        resume_text=resume_text
    )


if __name__ == "__main__":
    app.run(debug=True)
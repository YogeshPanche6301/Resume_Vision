# Resume-Vision: AI-Powered ATS Resume Intelligence Console

**Resume-Vision** is a premium, developer-first ATS (Applicant Tracking System) alignment verification console. Built with a high-contrast **Technical Swiss / Bauhaus-inspired** visual system, it helps candidates evaluate resume keyword matches, discover critical skill gaps, extract profile data, and print structured PDF reports.

The application utilizes the serverless **Google Gemini API** cloud model for intelligent parsing and resume feedback.

---

## Visual System & UX Architecture

* **Grid & Structure:** A balanced, 2-column modernist desktop layout with `0px` sharp borders, invoking premium engineering precision.
* **Typography:** Curated Google Web Fonts — **Outfit** for geometric display headlines and **JetBrains Mono** for technical telemetry and data readouts.
* **Monospace syslog Scanner:** Features an animated terminal overlay checking buffer chunks and verifying client model handshakes upon submission.
* **Responsive Visual Gauges:** Circular radial score indicators with live score count interpolation and dynamic color-coded metric progress bars.

---

##  Key Features

* **Data Extraction:** Parses candidate name automatically from resume document headers.
* **ATS Keyword Comparison:** Compares candidate skills against job specifications to isolate matches and gaps.
* **Milestone Analytics:** Yields dynamic, colored progress bars and calculated match metrics (Matches, Gaps, Recommendations).
* **Robust Persistence:** Employs a local disk cache (`latest_report.json`) to preserve analysis states across background Flask reloads.
* **Free PDF Export:** Outputs structured, beautifully structured ReportLab PDF certificates for candidates.

---

##  Tech Stack

* **Backend:** Flask (Python 3.10+)
* **Frontend:** HTML5, Vanilla CSS3 (Custom Grid, Animations), JavaScript ES6
* **AI Clients:** Google Generative AI (Gemini 2.5 Flash)
* **Document Parsing & Generation:** PyMuPDF (fitz), pdfminer.six, ReportLab
* **Hosting Configuration:** Vercel Serverless Function engine (`vercel.json`)

---

##  Local Installation & Offline Setup

### 1. Clone & Set Up Directory
```bash
git clone https://github.com/yourusername/Resume-Vision.git
cd Resume-Vision
```

### 2. Configure Virtual Environment & Install Dependencies
```bash
# Create virtual environment
python -m venv venv

# Activate on Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Activate on macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Create a local `.env` file (which is ignored by git) in the root directory:
```env
GEMINI_API_KEY=your_gemini_api_key_here
FLASK_SECRET_KEY=your_random_secret_passphrase
```
Get a free Gemini API key from [Google AI Studio](https://aistudio.google.com/).

### 4. Boot Local Development Server
```bash
python app.py
```
Open **[http://127.0.0.1:5000](http://127.0.0.1:5000)** in your browser.

---

## ☁️ Cloud Deployment (Vercel)

This project is pre-configured to be deployed as a serverless Flask app on **Vercel**.



---

##  Repository Structure

```
├── app.py                  # Main Flask Server & Route Controllers
├── vercel.json             # Vercel Serverless Build Configuration
├── requirements.txt        # Production Python Dependencies
├── static/
│   ├── style.css           # Modernist Styles for Landing & Upload Console
│   ├── dashboard.css       # Clean Grid UI Styles for Results Layout
│   ├── loading.js          # Loading Screen Handler & Syslog Text
│   └── dashboard.js        # SVG Gauge Renderer & Score Animation
├── templates/
│   ├── index.html          # File Uploader Console Page
│   └── result.html         # Score Dashboard Page
└── utils/
    ├── ai.py               # AI Handler (Google Gemini API Service)
    ├── parser.py           # Document Text Extractor via fitz
    ├── skills.py           # Regex Competency Matcher & Skill Comparator
    └── pdf_generator.py    # Structured PDF Generator using ReportLab
```

---

##  License
This project is licensed under the MIT License.

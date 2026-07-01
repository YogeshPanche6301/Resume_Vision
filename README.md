# Resume-Vision: AI-Powered ATS Resume Intelligence Console

**Resume-Vision** is a premium, developer-first ATS (Applicant Tracking System) alignment verification console. Built with a high-contrast **Technical Swiss / Bauhaus-inspired** visual system, it helps candidates evaluate resume keyword matches, discover critical skill gaps, extract profile data, and print structured PDF reports.

The application features a **Dual-Execution Pipeline**: it operates completely offline using a local **Ollama** model for development, and transitions seamlessly to a serverless **Google Gemini API** cloud model when deployed to production.

---

## 🎨 Visual System & UX Architecture

* **Grid & Structure:** A balanced, 2-column modernist desktop layout with `0px` sharp borders, invoking premium engineering precision.
* **Typography:** Curated Google Web Fonts — **Outfit** for geometric display headlines and **JetBrains Mono** for technical telemetry and data readouts.
* **Monospace syslog Scanner:** Features an animated terminal overlay checking buffer chunks and verifying client model handshakes upon submission.
* **Responsive Visual Gauges:** Circular radial score indicators with live score count interpolation and dynamic color-coded metric progress bars.

---

## 🚀 Key Features

* **Data Extraction:** Parses candidate name automatically from resume document headers.
* **ATS Keyword Comparison:** Compares candidate skills against job specifications to isolate matches and gaps.
* **Milestone Analytics:** Yields dynamic, colored progress bars and calculated match metrics (Matches, Gaps, Recommendations).
* **Robust Persistence:** Employs a local disk cache (`latest_report.json`) to preserve analysis states across background Flask reloads.
* **Free PDF Export:** Outputs structured, beautifully structured ReportLab PDF certificates for candidates.

---

## 🛠️ Tech Stack

* **Backend:** Flask (Python 3.10+)
* **Frontend:** HTML5, Vanilla CSS3 (Custom Grid, Animations), JavaScript ES6
* **AI Clients:** Google Generative AI (Gemini 1.5/2.5 Flash), Ollama (Llama 3)
* **Document Parsing & Generation:** PyMuPDF (fitz), pdfminer.six, ReportLab
* **Hosting Configuration:** Vercel Serverless Function engine (`vercel.json`)

---

## 💻 Local Installation & Offline Setup

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

### 3. Run Offline Ollama Instance
* Make sure [Ollama](https://ollama.com/) is installed and running.
* Download the default Llama 3 model:
  ```bash
  ollama run llama3
  ```

### 4. Boot Local Development Server
```bash
python app.py
```
Open **[http://127.0.0.1:5000](http://127.0.0.1:5000)** in your browser. Since no cloud credentials are provided, the app will automatically default to calling your local Ollama server!

---

## ☁️ Cloud Deployment (Vercel)

This project is pre-configured to be deployed as a serverless Flask app on **Vercel**, swapping local processing for the fast cloud Gemini model.

### 1. Get a Gemini API Key
Go to [Google AI Studio](https://aistudio.google.com/) and generate a free API key.

### 2. Configure Environment Variables
Create a local `.env` file (which is ignored by git) for cloud-mode simulation:
```env
GEMINI_API_KEY=your_gemini_api_key_here
FLASK_SECRET_KEY=your_random_secret_passphrase
```

### 3. Deploy to Vercel
1. Push your repository to **GitHub**.
2. Connect your GitHub account to [Vercel](https://vercel.com/).
3. Import the `Resume-Vision` project.
4. Add the following **Environment Variables** in Vercel project settings:
   * `GEMINI_API_KEY` (Your Google AI Studio Key)
   * `FLASK_SECRET_KEY` (Any secure string to encrypt Flask cookie sessions)
5. Click **Deploy**. Vercel will build the serverless functions using the root `vercel.json` file.

---

## 📁 Repository Structure

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
    ├── ai.py               # AI Handler (Gemini API Cloud / Ollama Local Fallback)
    ├── parser.py           # Document Text Extractor via fitz
    ├── skills.py           # Regex Competency Matcher & Skill Comparator
    └── pdf_generator.py    # Structured PDF Generator using ReportLab
```

---

## 📄 License
This project is licensed under the MIT License.

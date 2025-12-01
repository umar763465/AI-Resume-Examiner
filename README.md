# 📃 AI Resume Examiner

AI Resume Examiner is a web application built with **Streamlit** that allows users to upload their resumes (PDF or text) and get **AI-powered feedback** tailored to their job role. The app leverages **OpenAI's GPT-4o-mini model** to provide constructive insights on content clarity, skills presentation, and experience descriptions.

---

## **Features**

- Upload PDF or plain text resumes.
- Optional input of the job role to get role-specific recommendations.
- AI analyzes the resume and provides structured feedback.
- Beginner-friendly interface built with Streamlit.
- Error handling for empty or unreadable files.

---

## **Installation**

1. Clone the repository:

```
git clone https://github.com/yourusername/ai-resume-examiner.git
cd ai-resume-examiner
Create a virtual environment:

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Create a .env file in the project root and add your OpenAI API key:
OPENAI_API_KEY=your_openai_api_key_here

Usage
Run the Streamlit app:
uv run streamlit run main.py
Upload your resume (PDF or text).
Enter the job role (optional).
Click Analyze Resume to get AI-powered feedback.

Dependencies
Streamlit – For building the web interface
PyPDF2 – For extracting text from PDF resumes
OpenAI Python SDK – For connecting with GPT models
python-dotenv – For environment variable management

Project Structure
ai-resume-examiner/
│
├─ main.py                # Main Streamlit app
├─ requirements.txt      # Python dependencies
├─ .env                  # API key file (not uploaded to GitHub)
└─ README.md             # Project description

Future Improvements
Add OCR support for scanned resumes.
Improve handling for very large resumes.
Provide downloadable PDF feedback for users.
Integrate role-based templates for faster analysis.

License
This project is licensed under the MIT License. See the LICENSE file for details.

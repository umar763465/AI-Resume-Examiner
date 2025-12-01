import streamlit as st
import PyPDF2
import io
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI Resume Examiner", page_icon="📃",layout="centered") 

st.title("📃 AI Resume Examiner")
st.markdown("Upload your resume and get AI powered feedback tailored to your needs!")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf", "txt"])
job_role = st.text_input("Enter the job role you are applying for (optional) : ")

analyze = st.button("Analyze Resume")

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    return uploaded_file.read().decode("utf-8")

if analyze and uploaded_file:
    try:
        file_content = extract_text_from_file(uploaded_file)
        
        if not file_content.strip():
            st.error("The uploaded file is empty or could not be read.")
            st.stop()

        prompt = f"""Please analyze this resume and provide constructive feedback.
        Focus on the following aspects:
        1. Content clarity and impact
        2. Skills presentation
        3. Experience Descriptions
        4. Specific improvements for the job role: {job_role if job_role else 'general job applications'}

        Resume Content:
        {file_content}

        Please Provide your analysis in a clear , structured format with specific recommendations."""

        client = OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.application.create(
            model = "gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an expert career advisor."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        st.markdown("### Analysis Results")
        st.markdown(response.choices[0].message.content)
    except Exception as e:
        st.error(f"An error occurred during analysis: {e}")
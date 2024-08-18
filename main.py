import streamlit as st
from crewai import Crew, Process
from agents import HealthAssistant
from tasks import HealthTasks
from dotenv import load_dotenv
import pdfplumber

load_dotenv()

class HealthCrew:
    def __init__(self, blood_report):
        self.blood_report = blood_report

    def run(self):
        agents = HealthAssistant()
        tasks = HealthTasks()

        blood_test_analyzer = agents.blood_test_analyzer()
        health_risk_assessor = agents.health_risk_assessor()
        medical_information_researcher = agents.medical_information_researcher()
        recommendation_curator = agents.recommendation_curator()

        analyze_blood_report = tasks.analyze_blood_report(
            blood_test_analyzer,
            self.blood_report
        )

        assess_health_risks = tasks.assess_health_risks(
            health_risk_assessor,
            analyze_blood_report,
            self.blood_report
        )

        research_medical_information = tasks.research_medical_information(
            medical_information_researcher,
            assess_health_risks,
            self.blood_report
        )

        curate_recommendations = tasks.curate_recommendations(
            recommendation_curator,
            research_medical_information,
            assess_health_risks,
            self.blood_report
        )

        crew = Crew(
            agents=[
                blood_test_analyzer,
                health_risk_assessor,
                medical_information_researcher,
                recommendation_curator
            ],
            tasks=[
                analyze_blood_report,
                assess_health_risks,
                research_medical_information,
                curate_recommendations
            ],
            verbose=True,
            process=Process.sequential
        )

        result = crew.kickoff()
        return result

def extract_text_from_pdf(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        full_text = ""
        for page in pdf.pages:
            text = page.extract_text(layout=True)
            lines = text.split('\n')
            processed_text = ""
            for line in lines:
                processed_text += line.rstrip() + '\n'
            full_text += processed_text + "\n\n"
    return full_text

# Streamlit app
st.title("Health Assistant Crew")
st.write("Upload your blood report PDF and get insights")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    blood_report_text = extract_text_from_pdf(uploaded_file)
    health_crew = HealthCrew(blood_report_text)
    result = health_crew.run()
    st.subheader("Here is your Health Report:")
    st.write(result)

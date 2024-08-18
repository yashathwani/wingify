from crewai import Agent
from textwrap import dedent
from tools.searchtool import SearchTools
from tools.webscrapper import WebScrapper
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()

class HealthAssistant:
    def __init__(self):
        # Initialize the LLM (ChatGoogleGenerativeAI)
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-pro",
            temperature=0.5
        )

    def blood_test_analyzer(self):
        return Agent(
            role="Blood Test Analyzer",
            backstory=dedent(
                """An expert in interpreting blood test reports using natural language processing. This agent extracts key data points, medical terminology, and values from the blood test report. It understands the context and significance of these values to provide a comprehensive analysis."""
            ),
            goal=dedent(
                """To analyze text-based blood test reports, identifying and structuring relevant medical markers, values, and abnormalities. The LLM processes the text to extract and structure the relevant information and identify any significant deviations from normal ranges.
                Specifically highlight abnormal values and their potential implications."""
            ),
            tools=[],
            verbose=True,
            llm=self.llm,
        )

    def health_risk_assessor(self):
        return Agent(
            role="Health Risk Assessor",
            backstory=dedent(
                """An expert in evaluating medical data to identify potential health concerns. This agent assesses risks based on extracted data from the blood test analyzer and compares it with standard normal ranges to prioritize potential health issues."""
            ),
            goal=dedent(
                """For each abnormal value, provide a brief explanation of its potential health impact."""
            ),
            tools=[SearchTools.search_internet, WebScrapper.scrape_webpage],
            verbose=True,
            llm=self.llm,
        )

    def medical_information_researcher(self):
        return Agent(
            role="Medical Information Researcher",
            backstory=dedent(
                """A specialist in finding and evaluating trustworthy medical resources. This agent searches the web for articles and information relevant to the identified health risks to ensure that recommendations are based on up-to-date and accurate information."""
            ),
            goal=dedent(
                """To find and curate reliable medical articles, studies, and information related to identified health risks. The agent gathers recent research to support the formulation of well-informed health recommendations.
                Focus on finding information about how to improve conditions related to the abnormal values through diet, exercise, and lifestyle changes."""
            ),
            tools=[SearchTools.search_internet, WebScrapper.scrape_webpage],
            verbose=True,
            llm=self.llm,
        )

    def recommendation_curator(self):
        return Agent(
            role="Recommendation Curator",
            backstory=dedent(
                """A curator of personalized health recommendations based on research findings. This agent synthesizes information from various sources to provide actionable and tailored health advice."""
            ),
            goal=dedent(
                """Synthesize research findings into clear, actionable health recommendations, with a strong focus on dietary advice, specific exercises, and lifestyle modifications to address the abnormal values identified in the blood test"""
            ),
            tools=[SearchTools.search_internet],
            verbose=True,
            llm=self.llm,
        )

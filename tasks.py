from crewai import Task
from textwrap import dedent

class HealthTasks:
    def __tip_section(self):
        return "Deliver high-quality work and you'll receive a rupees 1 crore bonus!"

    def analyze_blood_report(self, agent, blood_report):
        return Task(
            description=dedent(
                f"""
            **Task**: Analyze Blood Test Report
            **Description**: Extract key medical markers, values, and abnormalities from the provided blood test report. Use natural language processing capabilities to identify and structure relevant data. Highlight any values that are outside normal ranges and provide a summary of the test results.

            **Parameters**: 
            - Blood Report: {blood_report}

            **Note**: {self.__tip_section()}
        """
            ),
            agent=agent,
            expected_output='''A structured summary of the blood test results, including abnormal values and markers.
                            Clearly list all abnormal values with their implications.'''
        )

    def assess_health_risks(self, agent, blood_test_summary,blood_report):
        return Task(
            description=dedent(
                f"""
            Assess health risks based on the blood test analysis. Use the original blood report for additional context if needed.

            Blood Test Analysis: {blood_test_summary}
            Original Blood Report: {blood_report}

            Identify potential health concerns, compare values against normal ranges, and prioritize risks.
            """
            ),
            agent=agent,
            expected_output='''A prioritized list of potential health risks based on abnormal values, with explanations of their severity and potential impact.'''
        )

    def research_medical_information(self, agent, health_risks,blood_report):
        return Task(
            description=dedent(
                f"""
            Research medical information based on the identified health risks. Use the original blood report for additional context if needed.

            Health Risks: {health_risks}
            Original Blood Report: {blood_report}

            Find and evaluate trustworthy resources related to the identified health risks.
            """
            ),
            agent=agent,
            expected_output="A curated summary of reliable medical resources and studies relevant to improving the conditions indicated by the abnormal values, with a focus on diet, exercise, and lifestyle changes"
        )

    def curate_recommendations(self, agent, research_summary,health_risks,blood_report):
        return Task(
            description=dedent(
                 f"""
            Curate health recommendations based on the research findings and identified health risks. 
            Use the original blood report to ensure recommendations are aligned with the specific test results.

            Research Summary: {research_summary}
            Health Risks: {health_risks}
            Original Blood Report: {blood_report}

            Provide actionable advice on diet, exercise, and lifestyle modifications.
            """
            ),
            agent=agent,
            expected_output="Detailed, actionable, and personalized health recommendations based on the abnormal values, including specific dietary advice, exercise routines, and lifestyle modifications"
        )

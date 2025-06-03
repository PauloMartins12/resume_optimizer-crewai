#!/usr/bin/env python
import sys
import warnings

from resume_crew.crew import ResumeCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the resume optimization crew.
    """
    inputs = {
        'job_url': 'https://jobs.riotinto.com/job/22022061/senior-advisor-business-improvement/',
        'company_name': 'Rio Tinto'
    }
    ResumeCrew().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()

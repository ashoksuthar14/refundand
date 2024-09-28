from crewai import Task
from agents.tax_analyst import tax_analyst

refund_task = Task(
    description="""
    Analyze the user's tax return to determine their refund or amount owed. 
    Provide a clear explanation of the results and any recommendations for deductions.
    """,
    expected_output="A detailed breakdown of tax refunds or taxes owed.",
    agent=tax_analyst,
)

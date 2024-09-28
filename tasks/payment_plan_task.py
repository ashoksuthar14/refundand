from crewai import Task
from agents.payment_planner import payment_planner

payment_plan_task = Task(
    description="""
    Help the user set up a payment plan for their taxes. Analyze the financial data and provide 
    different installment options, highlighting pros and cons of each.
    """,
    expected_output="A personalized payment plan for the user with monthly installment details.",
    agent=payment_planner,
)

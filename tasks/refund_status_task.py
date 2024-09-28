from crewai import Task
from agents.refund_tracker import refund_tracker

refund_status_task = Task(
    description="""
    Track the status of the user's tax refund and provide updates about when it is expected to be disbursed.
    """,
    expected_output="The current status of the user's refund, along with the expected disbursement date.",
    agent=refund_tracker,
)

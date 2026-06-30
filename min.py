from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class LoanApplication(BaseModel):
    sal: int
    exp: float

@app.post("/loan")
def evaluate_loan(application: LoanApplication):
    if application.sal > 45000 and application.exp > 1.5:
        message = "Your loan eligibility: 450000"
    elif application.sal > 25000 and application.exp > 1.5:
        message = "Your loan eligibility: 350000"
    elif application.sal > 15000 and application.exp > 1.5:
        message = "Your loan eligibility: 250000"
    else:
        message = "Not valid customer"

    return {
        "Status": "Viewed",
        "Exp_Level": application.exp,
        "Your_Sal": application.sal,
        "Decision": message,
    }
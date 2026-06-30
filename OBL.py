from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class OBL(BaseModel):
    income: int
    id: int
    loan: float
    exp: float

@app.post("/pre")
def loan(application: OBL):
    if application.income > 15000 and application.exp > 1.5:
        decision = "Yes Loan Will Approved"
    else:
        decision = "No Loan Will Reject"
    return {
        "application_income": application.income,
        "Status": decision,
        "Application_loan_amount": application.loan,
    }
    
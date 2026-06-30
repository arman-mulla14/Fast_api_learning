from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
class loan(BaseModel): 
    age : int 
    income : float
    loan :  float 
    exp : int

@app.post("/pre")
def pre(application:loan ):
    if application.income > 25000 and application.exp > 1.5 : 
        decision = "Approved" 
    else : 
        decision = "Reject"
    return { 
      "application_Age" : application.age, 
      "decision":decision   
    }



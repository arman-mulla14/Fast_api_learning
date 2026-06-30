from fastapi import FastAPI 
from pydantic import BaseModel
app = FastAPI()

class std(BaseModel) : 
    marks : float 
    cgpa :float
    sgpa : float
    rank : int

@app.post("/std") 
def std(application:std): 
    if application.marks > 75 and application.cgpa > 7.5 and application.sgpa > 7.5 and application.rank < 10 : 
        message = "Admission Will Done Contact AIT"
    elif application.marks > 65 and application.cgpa > 6.5 and application.sgpa > 6.5 and application.rank > 20 : 
        message = " Admission Will stay on "
    else : 
        message = "Thank you for We Will Contact you"

    return {
        "Application_status" : message, 
        
    }
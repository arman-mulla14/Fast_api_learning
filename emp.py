from fastapi import FastAPI 
from pydantic import BaseModel

app = FastAPI()

class logs(BaseModel): 
    age : int 
    sal : int
    id: int
    exp : float 
@app.post("/logs")
def logs(application:logs): 
    if application.age > 28 and application.sal > 15000 and application.exp > 3.5 : 
        message = "Safe Not will layoff"
    else :
        message = "Sorry this in risk tto layoff"
    return { 
        "Status" : message ,
        "ID of EMP" : application.id
    }
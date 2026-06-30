from fastapi import FastAPI 
app = FastAPI()

risk_std = { 
    101:{"name":"Arman","marks":"75","CGPA":"7.5","risk":"Low"},
    102:{"name":"Rahul","marks":"42","CGPA":"4.8","risk":"High"},
    103:{"name":"Priya","marks":"88","CGPA":"9.1","risk":"Low"},
    104:{"name":"Amit","marks":"35","CGPA":"3.9","risk":"High"},
    105:{"name":"Sneha","marks":"56","CGPA":"5.8","risk":"Medium"},
    106:{"name":"Vikram","marks":"29","CGPA":"3.2","risk":"High"},
    107:{"name":"Neha","marks":"81","CGPA":"8.4","risk":"Low"},
    108:{"name":"Karan","marks":"47","CGPA":"5.0","risk":"Medium"},
    109:{"name":"Pooja","marks":"38","CGPA":"4.2","risk":"High"},
    110:{"name":"Rohit","marks":"52","CGPA":"5.6","risk":"Medium"}
}

@app.get("/std/{std_id}")
def get_std_risk(std_id:int): 
    if std_id not in risk_std :
        return { 
            "Error" : "Record Not Found" 

        }
    profile = risk_std[std_id]
    return { 
        "Name of Student ":profile["name"], 
        "Marks of Student":profile["marks"], 
        "CGPA od Student": profile["CGPA"],
        "Risk to Fail":profile["risk"] 
    }
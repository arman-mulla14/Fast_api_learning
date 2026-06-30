from fastapi import FastAPI 
app = FastAPI()


customer_risk = { 
    101 : {"name" :"Arman" , "risk" : "high" , "score" : 0.12},
     102 : {"name" :"Aman" , "risk" : "low" , "score" : 1},
      103 : {"name" :"Altaf" , "risk" : "low" , "score" : 0.87},
       104 : {"name" :"imran" , "risk" : "high" , "score" : 0.01},
}

@app.get("customer/{customer_id}")
def get_customer_risk(customer_id):
    if customer_id not in customer_risk :
        return {"Error" : "Not found"}
    
    
    profile = customer_risk_profile [customer_id]
    return{ 
        "customer_id": customer_id, 
        "name":profile["name"],
        "Risk_levl":profile["risk"], 
        "Socre":profile["score"]
    }
from fastapi import FastAPI
app = FastAPI()

customer_risk = { 
    101: { "name"  : "Arman" , "risk" : "High" , "rate" :"0.65"},
        102: { "name"  : "Aman" , "risk" : "low" , "rate" :"0.99"},
            103: { "name"  : "Altat" , "risk" : "low" , "rate" :"0.85"},
                104: { "name"  : "imran" , "risk" : "High" , "rate" :"0.15"},

}
@app.get("/customer/{customer_id}")
def get_customer_risk(customer_id:int): 
    if customer_id not in customer_risk :
        return {
            "Error" : "Not fount"
        }
    profile = customer_risk[customer_id]
    return { 
        "Customer_id": customer_id,
        "name":profile["name"],
        "risk_level":profile["rate"],
        "Status": profile["risk"]
    }
from fastapi import FastAPI 
app = FastAPI()
@app.get("/man")
def man(man_id: int): 
    return{
        "name" : "Arman Mulla", 
        "ID" : man_id, 
        "Age" : "21"

    }



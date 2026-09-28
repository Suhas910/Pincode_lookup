from fastapi import FastAPI, HTTPException
from schemas import ClientForm, ClientResponse
from data import pincode_database

app = FastAPI()

@app.get("/")
def root():
    return {"message":"Pincode Lookup"}

@app.post("/client-form", response_model=ClientResponse)
def client_form(form : ClientForm):
    for place in pincode_database:
        if place["pincode"] == form.pincode :
            return ClientResponse(
                name = form.name,
                pincode = form.pincode,
                State = place["State"],
                City = place["City"],
            )
    raise HTTPException(status_code=404, detail=f"Place with the pincode {form.pincode} was not found")


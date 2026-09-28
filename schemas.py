from pydantic import BaseModel

class ClientForm(BaseModel):
    name : str
    pincode : int

class ClientResponse(BaseModel):
    name : str
    pincode : int
    State : str
    City : str

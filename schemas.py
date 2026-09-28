from pydantic import BaseModel, field_validator

class ClientForm(BaseModel):
    name : str
    pincode : int

    @field_validator("pincode")
    @classmethod
    def validate_pincode(cls, value):
        if len(value) != 6 :
            raise ValueError("invalid pincode")
        return value
    

class ClientResponse(BaseModel):
    name : str
    pincode : int
    State : str
    City : str

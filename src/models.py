from pydantic import BaseModel
from typing import List

class Field(BaseModel):
    name: str
    field_name: str
    field_type: str

class FormTemplate(BaseModel):
    name: str
    fields: List[Field]
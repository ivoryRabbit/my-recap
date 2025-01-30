from pydantic import BaseModel


class RecapItem(BaseModel):
    name: str
    value: str

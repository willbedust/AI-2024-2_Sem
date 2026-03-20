from pydantic import BaseModel, ConfigDict


class ModelRequest(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    model_name: str
    text: str

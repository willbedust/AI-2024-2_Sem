from pydantic import BaseModel, ConfigDict


class ModelResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    request_id: int
    label: bool

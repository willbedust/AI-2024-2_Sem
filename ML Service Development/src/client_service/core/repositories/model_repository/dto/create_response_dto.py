from pydantic import BaseModel, ConfigDict, Field


class CreateResponseDTO(BaseModel):
    model_config = ConfigDict(extra="forbid")

    request_id: int = Field(...)
    label: bool = Field(...)

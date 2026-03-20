from pydantic import BaseModel, ConfigDict, Field


class CreateRequestDTO(BaseModel):
    model_config = ConfigDict(extra="forbid")

    model_name: str = Field(...)
    text: str = Field(...)

from pydantic import BaseModel, ConfigDict, Field


class UpdateUserDTO(BaseModel):
    model_config = ConfigDict(extra="forbid")

    password: str = Field(..., max_length=50)
    funds: float = Field(...)
